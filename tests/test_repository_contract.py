from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT_FILES = [
    "README.md",
    "AGENTS.md",
    ".gitignore",
    "pyproject.toml",
    "requirements-dev.txt",
]

REQUIRED_DOCS = [
    "concept.md",
    "workflow.md",
    "pdca_ywt_kpt.md",
    "thinking_harness_integration.md",
    "companion_layer.md",
    "quality_bar.md",
    "repository_settings.md",
]

REQUIRED_EXAMPLES = [
    "sample_strategy_input.md",
    "sample_yearly_plan.md",
    "sample_monthly_plan.md",
    "sample_weekly_plan.md",
    "sample_kpt_review.md",
    "sample_ywt_review.md",
    "sample_companion_checkin.md",
    "sample_stuck_recovery.md",
]


def test_required_root_files_exist() -> None:
    for relative_path in REQUIRED_ROOT_FILES:
        assert (ROOT / relative_path).exists(), f"Missing root file: {relative_path}"


def test_required_docs_exist_and_are_not_empty() -> None:
    for name in REQUIRED_DOCS:
        path = ROOT / "docs" / name
        assert path.exists(), f"Missing doc: {name}"
        assert path.read_text(encoding="utf-8").strip(), f"Doc is empty: {name}"


def test_required_examples_exist_and_are_not_empty() -> None:
    for name in REQUIRED_EXAMPLES:
        path = ROOT / "examples" / name
        assert path.exists(), f"Missing example: {name}"
        assert path.read_text(encoding="utf-8").strip(), f"Example is empty: {name}"


def test_generated_outputs_are_ignored() -> None:
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "outputs/generated_plan.md" in gitignore
    assert "outputs/generated_review.md" in gitignore


def test_github_actions_runs_required_pytest_command() -> None:
    workflow = (ROOT / ".github" / "workflows" / "pytest.yml").read_text(encoding="utf-8")
    assert "python3 -m pytest -q" in workflow
    assert "requirements-dev.txt" in workflow


def test_readme_numbered_sections_are_sequential() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    section_numbers = []
    for line in readme.splitlines():
        if not line.startswith("## "):
            continue
        marker = line.split(" ", 2)[1]
        if marker.endswith(".") and marker[:-1].isdigit():
            section_numbers.append(int(marker[:-1]))

    assert section_numbers == list(range(1, len(section_numbers) + 1))
