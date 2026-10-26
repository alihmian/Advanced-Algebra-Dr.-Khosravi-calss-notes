#!/usr/bin/env python3
"""Build one lecture's separate ambiguity/question PDF from its editable source."""

import argparse
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent.parent


def lecture_id(value):
    if not re.fullmatch(r"[0-9]{1,2}", value) or not 1 <= int(value) <= 20:
        raise argparse.ArgumentTypeError("lecture ID must be a number from 1 to 20")
    return f"{int(value):02d}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("id", type=lecture_id, help="lecture number, for example 04")
    parser.add_argument("--latexmk", default=os.environ.get("LATEXMK", "latexmk"))
    args = parser.parse_args()
    source_dir = ROOT / "docs" / "ambiguities" / f"lecture{args.id}"
    source = source_dir / "main.tex"
    if not source.is_file():
        print(
            f"Error: Questions source does not exist: {source}\n"
            f"Create {source_dir}, copy docs/ambiguities/template.tex to its main.tex, "
            "and add the lecture's actual questions before building.",
            file=sys.stderr,
        )
        return 1

    try:
        command = shlex.split(args.latexmk)
        if not command:
            raise ValueError("--latexmk must name an executable")
        executable = shutil.which(command[0])
        if executable is None:
            raise ValueError(
                f"Cannot find {command[0]!r}; install latexmk and XeLaTeX, "
                "or pass --latexmk /path/to/latexmk"
            )
        command[0] = executable
        build_dir = ROOT / "build" / "questions" / f"lecture-{args.id}"
        build_dir.mkdir(parents=True, exist_ok=True)
        jobname = f"lecture-{args.id}-questions"
        subprocess.run(
            command + [
                "-norc", "-xelatex", "-interaction=nonstopmode",
                "-halt-on-error", "-file-line-error",
                f"-outdir={build_dir}", f"-jobname={jobname}", "main.tex",
            ],
            cwd=source_dir,
            check=True,
        )
        built_pdf = build_dir / f"{jobname}.pdf"
        if not built_pdf.is_file() or built_pdf.stat().st_size == 0:
            raise ValueError(f"Build did not produce a nonempty PDF: {built_pdf}")
        output_dir = ROOT / "output" / "pdf"
        output_dir.mkdir(parents=True, exist_ok=True)
        destination = output_dir / built_pdf.name
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=output_dir, suffix=".pdf", delete=False) as stream:
                temporary = Path(stream.name)
            shutil.copy2(built_pdf, temporary)
            temporary.replace(destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        print(destination)
    except subprocess.CalledProcessError as exc:
        print(
            f"Error: Questions PDF build failed (exit {exc.returncode}). "
            "The previously exported PDF was preserved.",
            file=sys.stderr,
        )
        return 1
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
