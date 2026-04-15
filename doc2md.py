#!/usr/bin/env python3
# doc2md — Word (and other Pandoc-supported) documents to Markdown.
# Copyright (C) 2026 brockcraft
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <https://www.gnu.org/licenses/>.
# SPDX-License-Identifier: GPL-2.0-or-later

import argparse
from pathlib import Path

import pypandoc


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a document to Markdown using Pandoc (via pypandoc)."
    )
    parser.add_argument(
        "input_file",
        help="Input document path (e.g. example.docx)",
    )
    parser.add_argument(
        "output_file",
        nargs="?",
        default=None,
        help="Output Markdown path (default: same basename as input with .md)",
    )
    args = parser.parse_args()

    input_path = Path(args.input_file)
    if not input_path.is_file():
        parser.error(f"not a file or does not exist: {input_path}")

    if args.output_file is not None:
        output_path = Path(args.output_file)
    else:
        output_path = input_path.with_suffix(".md")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    media_dir = output_path.parent / "images"

    input_resolved = input_path.resolve()
    output_resolved = output_path.resolve()
    media_resolved = media_dir.resolve()

    print(f"Converting: {input_resolved}")
    print(f"Output:     {output_resolved}")
    print(f"Media dir:  {media_resolved}")

    pypandoc.convert_file(
        str(input_path),
        "markdown",
        outputfile=str(output_path),
        extra_args=[f"--extract-media={media_dir}"],
    )

    md_bytes = output_resolved.stat().st_size
    if media_resolved.is_dir():
        image_count = sum(1 for p in media_resolved.iterdir() if p.is_file())
    else:
        image_count = 0
    print(
        f"Done. Wrote {md_bytes:,} bytes to {output_resolved.name}; "
        f"{image_count} file(s) under {media_resolved.name}/"
    )


if __name__ == "__main__":
    main()
