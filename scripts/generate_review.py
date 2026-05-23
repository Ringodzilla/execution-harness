#!/usr/bin/env python3
"""Generate a consolidated review document from KPT/YWT review files."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWS_DIR = ROOT / "reviews"
OUTPUT_PATH = ROOT / "outputs" / "generated_review.md"

SOURCES = [
    ("KPT Reviews", REVIEWS_DIR / "kpt"),
    ("YWT Reviews", REVIEWS_DIR / "ywt"),
]


def read_markdown_files(directory: Path) -> list[tuple[str, str]]:
    files: list[tuple[str, str]] = []
    for path in sorted(directory.glob("*.md")):
        if path.name.startswith("."):
            continue
        content = path.read_text(encoding="utf-8").strip()
        files.append((path.name, content))
    return files


def render_section(title: str, files: list[tuple[str, str]]) -> str:
    lines = [f"## {title}", ""]
    if not files:
        lines.append("- No entries found")
        lines.append("")
        return "\n".join(lines)

    for filename, content in files:
        lines.append(f"### {filename}")
        lines.append("")
        lines.append(content if content else "(empty)")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Generated Review",
        "",
        f"- Generated at: {datetime.now().isoformat(timespec='seconds')}",
        "",
    ]

    for title, directory in SOURCES:
        lines.append(render_section(title, read_markdown_files(directory)))

    OUTPUT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Generated: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
