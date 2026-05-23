from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = ROOT / "templates"

# Required headers based on repository spec.
REQUIRED_SECTIONS = {
    "yearly_plan.md": [
        "## 年間テーマ",
        "## North Star",
        "## 重点領域",
        "## KPI",
        "## やらないこと",
        "## リスク",
        "## 四半期テーマ",
        "## 次の一歩",
    ],
    "quarterly_plan.md": [
        "## 四半期テーマ",
        "## 重点目標",
        "## KPI",
        "## 成功条件",
        "## 月次マイルストーン",
        "## 次の一歩",
    ],
    "monthly_plan.md": [
        "## 月間テーマ",
        "## 最重要ゴール",
        "## 習慣",
        "## KPI",
        "## 週次計画",
        "## 月末KPT",
        "## 月末YWT",
        "## 次の一歩",
    ],
    "weekly_plan.md": [
        "## 今週のテーマ",
        "## 最重要タスク3つ",
        "## 捨てること",
        "## 習慣",
        "## KPT",
        "## YWT",
        "## 次週への申し送り",
        "## 次の一歩",
    ],
    "daily_log.md": [
        "## 今日の最重要行動",
        "## 実行ログ",
        "## 気づき",
        "## 障害",
        "## 明日やること",
        "## 次の一歩",
    ],
    "kpt_review.md": [
        "## Keep",
        "## Problem",
        "## Try",
        "## 次アクション",
        "## 優先度",
        "## 次の一歩",
    ],
    "ywt_review.md": [
        "## やったこと",
        "## わかったこと",
        "## 次やること",
        "## 学習ポイント",
        "## 次の一歩",
    ],
    "strategy_to_execution.md": [
        "## Input (from thinking-harness)",
        "## 年間変換",
        "## 四半期変換",
        "## 月次変換",
        "## 週次変換",
        "## 次の一歩",
    ],
    "companion_checkin.md": [
        "## 今の状態",
        "## 気分",
        "## 進んだこと",
        "## 止まっていること",
        "## 今日できる最小行動",
        "## 次の一歩",
    ],
    "stuck_recovery.md": [
        "## どこで止まっているか",
        "## 原因",
        "## 小さくできるか",
        "## 捨てられること",
        "## 10分でできる再開アクション",
        "## 次の一歩",
    ],
    "gentle_progress_review.md": [
        "## 前進したこと",
        "## できなかった理由",
        "## 責めずに改善すること",
        "## 明日の最小行動",
        "## 次の一歩",
    ],
    "goal_guidance.md": [
        "## 最終ゴール",
        "## 現在地",
        "## ギャップ",
        "## 今週やること",
        "## 今日やること",
        "## 最初の5分",
        "## 次の一歩",
    ],
    "motivation_reset.md": [
        "## なぜ始めたか",
        "## 今しんどい理由",
        "## 再開する最小単位",
        "## 今日の勝ち条件",
        "## 次の一歩",
    ],
    "next_step_coaching.md": [
        "## 目的",
        "## 障害",
        "## 選択肢",
        "## 一番軽い行動",
        "## 完了条件",
        "## 次の一歩",
    ],
}


def test_templates_have_required_sections() -> None:
    for template_name, required_headers in REQUIRED_SECTIONS.items():
        path = TEMPLATES_DIR / template_name
        content = path.read_text(encoding="utf-8")

        missing = [header for header in required_headers if header not in content]
        assert not missing, f"{template_name} is missing required sections: {missing}"
