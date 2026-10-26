#!/usr/bin/env python3
"""Inspect, verify, render, and build one Advanced Algebra lecture at a time."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
COURSE_ROOT = ROOT.parent.parent
MANIFEST = COURSE_ROOT / "sources" / "manifest.json"
SOURCE_DIR = (COURSE_ROOT / "sources" / "lectures").resolve()


class LectureError(Exception):
    pass


def lecture_id(value):
    if not re.fullmatch(r"[0-9]{1,2}", value) or not 1 <= int(value) <= 20:
        raise argparse.ArgumentTypeError("lecture ID must be a number from 1 to 20")
    return f"{int(value):02d}"


def manifest_lectures():
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise LectureError(f"Cannot read {MANIFEST}: {exc}") from exc
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise LectureError("Expected manifest schema_version 1")
    lectures = data.get("lectures")
    if not isinstance(lectures, list) or not all(isinstance(item, dict) for item in lectures):
        raise LectureError("Manifest lectures must be a list of records")
    return lectures


def find_lecture(lectures, ident):
    matches = [item for item in lectures if item.get("id") == ident]
    if len(matches) != 1:
        raise LectureError(f"Expected one manifest record for lecture {ident}; found {len(matches)}")
    return matches[0]


def sources_for(lecture):
    sources = lecture.get("sources")
    if not isinstance(sources, list) or not sources or not all(isinstance(item, dict) for item in sources):
        raise LectureError(f"Lecture {lecture.get('id')} has no valid source list")
    return sources


def source_path(source):
    value = source.get("path")
    if not isinstance(value, str) or Path(value).is_absolute():
        raise LectureError("Source paths must be relative to the repository")
    path = (COURSE_ROOT / value).resolve()
    if not path.is_relative_to(SOURCE_DIR) or path.suffix.lower() != ".pdf":
        raise LectureError(f"Source path must be a PDF inside sources/lectures/: {value}")
    return path


def candidate_section(ident):
    return ROOT / "sections" / f"section{int(ident)}.tex"


def ledger_path(ident):
    return ROOT / "docs" / "editorial" / f"{ident}.md"


def selected_source(lecture, variant):
    sources = sources_for(lecture)
    names = [source.get("variant") for source in sources]
    if variant is None and len(sources) > 1:
        raise LectureError(
            f"Lecture {lecture['id']} has multiple source versions. Specify --variant "
            f"with one of: {', '.join(map(str, names))}. This does not settle which version is authoritative."
        )
    matches = sources if variant is None else [item for item in sources if item.get("variant") == variant]
    if len(matches) != 1:
        raise LectureError(f"Unknown or nonunique variant {variant!r}; available: {', '.join(map(str, names))}")
    source = matches[0]
    if not isinstance(source.get("variant"), str) or not re.fullmatch(r"[A-Za-z0-9_-]+", source["variant"]):
        raise LectureError("Source variant must contain only letters, digits, underscores, and hyphens")
    return source


def require_tool(command, advice):
    found = shutil.which(command)
    if found is None:
        raise LectureError(f"Cannot find {command!r} on PATH. {advice}")
    return found


def run(command, **kwargs):
    try:
        return subprocess.run(command, check=True, **kwargs)
    except FileNotFoundError as exc:
        raise LectureError(f"Cannot run {command[0]!r}; check the executable path") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or "").strip() if isinstance(exc.stderr, str) else ""
        raise LectureError(f"{Path(command[0]).name} failed with exit code {exc.returncode}" + (f": {detail}" if detail else "")) from exc


def list_lectures(lectures):
    for lecture in lectures:
        ident = lecture["id"]
        pages = "+".join(str(source["pages"]) for source in sources_for(lecture))
        section = candidate_section(ident)
        state = "exists; consult ledger" if section.is_file() else "not started"
        print(f"{ident}  {lecture['title']} ({pages} source pages)")
        print(f"    Candidate: {section.relative_to(ROOT)} [{state}]; ledger: docs/editorial/{ident}.md")


def show_lecture(lecture):
    ident = lecture["id"]
    print(f"Lecture {ident}: {lecture['title']}")
    print(f"Source selection: {lecture.get('variant_selection', 'unspecified')}")
    for source in sources_for(lecture):
        print(f"  {source['variant']}: {source_path(source)} ({source['pages']} pages)")
    print(f"Candidate section: {candidate_section(ident)}")
    print(f"Editorial decisions and source coverage: {ledger_path(ident)}")
    print("File existence does not establish mathematical-edit or review status. Consult the editorial ledger and independent review record.")


def check_sources(lectures):
    expected_ids = [f"{number:02d}" for number in range(1, 21)]
    if [item.get("id") for item in lectures] != expected_ids:
        raise LectureError("Manifest must contain exactly 20 sequential lecture IDs, 01 through 20")
    entries = [(lecture["id"], source) for lecture in lectures for source in sources_for(lecture)]
    if len(entries) != 21:
        raise LectureError(f"Expected 21 source PDFs; manifest has {len(entries)}")
    paths = [source_path(source) for _, source in entries]
    if len(set(paths)) != len(paths):
        raise LectureError("Manifest repeats a source path")
    actual_files = [path for path in SOURCE_DIR.rglob("*") if path.is_file() and path.suffix.lower() == ".pdf"]
    if len(actual_files) != 21:
        raise LectureError(f"Expected exactly 21 PDFs in sources/lectures/; found {len(actual_files)}")
    actual_paths = {path.resolve() for path in actual_files}
    if set(paths) != actual_paths:
        missing = sorted(str(path) for path in set(paths) - actual_paths)
        extras = sorted(str(path) for path in actual_paths - set(paths))
        raise LectureError(f"Source inventory mismatch. Missing: {missing}; unlisted PDFs: {extras}")
    info_tool = shutil.which("pdfinfo")
    errors = []
    for (ident, source), path in zip(entries, paths):
        label = f"Lecture {ident}, {path.name}"
        if path.stat().st_size != source.get("bytes"):
            errors.append(f"{label}: byte count differs")
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        if digest.hexdigest() != source.get("sha256"):
            errors.append(f"{label}: SHA-256 differs")
        if type(source.get("pages")) is not int or source["pages"] < 1:
            errors.append(f"{label}: invalid manifest page count")
        elif info_tool:
            try:
                info = run([info_tool, str(path)], capture_output=True, text=True).stdout
                match = re.search(r"^Pages:\s+(\d+)\s*$", info, re.MULTILINE)
                if match is None or int(match.group(1)) != source["pages"]:
                    errors.append(f"{label}: PDF page count differs")
            except LectureError as exc:
                errors.append(f"{label}: {exc}")
    if errors:
        raise LectureError("Source verification failed:\n" + "\n".join(errors))
    total_pages = sum(source["pages"] for _, source in entries)
    total_bytes = sum(source["bytes"] for _, source in entries)
    print(f"Verified 20 lectures, 21 PDFs, {total_pages} pages, {total_bytes:,} bytes; all SHA-256 checks match.")
    if info_tool:
        print("PDF page counts verified with pdfinfo.")
    else:
        print("pdfinfo unavailable: page counts are manifest values; hashes and byte counts verified. Install Poppler to verify page counts.")


def render_lecture(lecture, args):
    source = selected_source(lecture, args.variant)
    path = source_path(source)
    last_page = args.last_page if args.last_page is not None else args.page
    if not 1 <= args.page <= last_page <= source["pages"]:
        raise LectureError(f"Pages must satisfy 1 <= --page <= --last-page <= {source['pages']}")
    if not 50 <= args.dpi <= 600:
        raise LectureError("--dpi must be from 50 to 600")
    if not path.is_file():
        raise LectureError(f"Source PDF is missing: {path}")
    tool = require_tool("pdftoppm", "Install Poppler (macOS: brew install poppler; Debian/Ubuntu: apt install poppler-utils).")
    directory = ROOT / "build" / "source-pages" / f"lecture-{lecture['id']}" / source["variant"]
    directory.mkdir(parents=True, exist_ok=True)
    prefix = directory / "page"
    run([tool, "-f", str(args.page), "-l", str(last_page), "-r", str(args.dpi), "-png", str(path), str(prefix)])
    rendered = []
    for output in directory.glob("page-*.png"):
        match = re.fullmatch(r"page-(\d+)\.png", output.name)
        if match and args.page <= int(match.group(1)) <= last_page:
            rendered.append((int(match.group(1)), output))
    if len(rendered) != last_page - args.page + 1:
        raise LectureError("Renderer did not produce all requested page images")
    for _, output in sorted(rendered):
        print(output)


def build_lecture(lecture, args):
    ident = lecture["id"]
    section = candidate_section(ident)
    if not section.is_file():
        raise LectureError(f"Lecture {ident} has not been started: create {section} with actual lecture frames first")
    active_text = "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in section.read_text(encoding="utf-8").splitlines())
    if not re.search(r"\\begin\s*\{frame\}", active_text):
        raise LectureError(f"Lecture {ident} has no active frames; it has not been started")
    try:
        command = shlex.split(args.latexmk)
    except ValueError as exc:
        raise LectureError(f"Invalid --latexmk command: {exc}") from exc
    if not command:
        raise LectureError("--latexmk must name an executable")
    command[0] = require_tool(command[0], "Install a TeX distribution with XeLaTeX and latexmk, or pass --latexmk /path/to/latexmk.")
    directory = ROOT / "build"
    directory.mkdir(exist_ok=True)
    wrapper = directory / f"lecture-{ident}-entry.tex"
    wrapper.write_text(
        "% Generated by scripts/lectures.py; edit the lecture section, not this wrapper.\n"
        f"\\def\\AlgebraLectureNumber{{{int(ident)}}}\n"
        "\\input{main.tex}\n", encoding="utf-8"
    )
    run(command + ["-outdir=build", f"-jobname=lecture-{ident}", str(wrapper.relative_to(ROOT))], cwd=ROOT)
    print(ROOT / "build" / f"lecture-{ident}.pdf")


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="list lecture PDFs, candidate sections, and progress ledgers")
    show = commands.add_parser("show", help="show exact source paths for one lecture")
    show.add_argument("id", type=lecture_id)
    commands.add_parser("check", help="verify all imported source files against the manifest")
    render = commands.add_parser("render", help="render selected source PDF pages for visual transcription")
    render.add_argument("id", type=lecture_id)
    render.add_argument("--page", type=int, required=True)
    render.add_argument("--last-page", type=int)
    render.add_argument("--dpi", type=int, default=150)
    render.add_argument("--variant")
    build = commands.add_parser("build", help="compile only one lecture's existing frames")
    build.add_argument("id", type=lecture_id)
    build.add_argument("--latexmk", default=os.environ.get("LATEXMK", "latexmk"))
    return result


def main():
    args = parser().parse_args()
    try:
        lectures = manifest_lectures()
        if args.command == "list":
            list_lectures(lectures)
        elif args.command == "check":
            check_sources(lectures)
        else:
            lecture = find_lecture(lectures, args.id)
            if args.command == "show":
                show_lecture(lecture)
            elif args.command == "render":
                render_lecture(lecture, args)
            else:
                build_lecture(lecture, args)
    except (LectureError, OSError, KeyError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
