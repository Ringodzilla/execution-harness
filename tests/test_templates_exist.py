from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TEMPLATES = [
    "yearly_plan.md",
    "quarterly_plan.md",
    "monthly_plan.md",
    "weekly_plan.md",
    "daily_log.md",
    "habit_tracker.md",
    "kpi_dashboard.md",
    "action_item.md",
    "strategy_to_execution.md",
    "kpt_review.md",
    "ywt_review.md",
    "companion_checkin.md",
    "stuck_recovery.md",
    "gentle_progress_review.md",
    "goal_guidance.md",
    "motivation_reset.md",
    "next_step_coaching.md",
]

REQUIRED_PROMPTS = [
    "system_prompt.md",
    "yearly_planning_prompt.md",
    "quarterly_planning_prompt.md",
    "monthly_planning_prompt.md",
    "weekly_planning_prompt.md",
    "daily_execution_prompt.md",
    "kpt_review_prompt.md",
    "ywt_review_prompt.md",
    "progress_review_prompt.md",
    "strategy_to_execution_prompt.md",
    "companion_prompt.md",
    "stuck_recovery_prompt.md",
    "progress_coaching_prompt.md",
    "goal_guidance_prompt.md",
    "motivation_reset_prompt.md",
]


def test_templates_exist() -> None:
    for name in REQUIRED_TEMPLATES:
        path = ROOT / "templates" / name
        assert path.exists(), f"Missing template: {name}"


def test_prompts_exist() -> None:
    for name in REQUIRED_PROMPTS:
        path = ROOT / "prompts" / name
        assert path.exists(), f"Missing prompt: {name}"
