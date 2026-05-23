from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "prompts"

REQUIRED_PROMPT_SECTIONS = [
    "## Role",
    "## Goal",
    "## Input",
    "## Process",
    "## Output Format",
    "## Tone",
    "## Constraints",
    "## Quality Criteria",
]


def test_all_prompts_follow_required_structure() -> None:
    for path in sorted(PROMPTS_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        missing = [section for section in REQUIRED_PROMPT_SECTIONS if section not in content]
        assert not missing, f"{path.name} is missing prompt sections: {missing}"

        positions = [content.index(section) for section in REQUIRED_PROMPT_SECTIONS]
        assert positions == sorted(positions), f"{path.name} prompt sections are out of order"


def test_all_prompts_end_in_next_step_behavior() -> None:
    for path in sorted(PROMPTS_DIR.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        assert "次の一歩" in content, f"{path.name} must drive output toward 次の一歩"
