from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run_script(script_name: str) -> None:
    script_path = ROOT / "scripts" / script_name
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"Script failed: {script_name}\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )


def test_generate_plan_script_runs_and_generates_output() -> None:
    run_script("generate_plan.py")
    output = ROOT / "outputs" / "generated_plan.md"
    assert output.exists(), "generated_plan.md was not created"
    content = output.read_text(encoding="utf-8")
    assert "# Generated Plan" in content


def test_generate_review_script_runs_and_generates_output() -> None:
    run_script("generate_review.py")
    output = ROOT / "outputs" / "generated_review.md"
    assert output.exists(), "generated_review.md was not created"
    content = output.read_text(encoding="utf-8")
    assert "# Generated Review" in content
