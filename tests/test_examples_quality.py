from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"

NEXT_STEP_EXAMPLES = [
    "sample_yearly_plan.md",
    "sample_monthly_plan.md",
    "sample_weekly_plan.md",
    "sample_kpt_review.md",
    "sample_ywt_review.md",
    "sample_companion_checkin.md",
    "sample_stuck_recovery.md",
]


def test_strategy_input_contains_thinking_harness_contract() -> None:
    content = (EXAMPLES_DIR / "sample_strategy_input.md").read_text(encoding="utf-8")
    for required in ["## strategy", "## center_pin", "## hypothesis"]:
        assert required in content


def test_execution_examples_include_next_step() -> None:
    for name in NEXT_STEP_EXAMPLES:
        content = (EXAMPLES_DIR / name).read_text(encoding="utf-8")
        assert "## 次の一歩" in content, f"{name} must end in a next action"
