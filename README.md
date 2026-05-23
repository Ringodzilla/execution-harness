# execution-harness

execution-harness は、戦略を日々の行動へ変換し、前進・学習・改善・再始動を回し続けるための伴走型実行OSです。

このリポジトリの目的は、完璧な計画を作ることではありません。目的は一貫して、**ユーザーが止まらず前進できる状態を作ること**です。

## 1. 目的

execution-harness は以下を一体化します。

- 実行
- 進捗管理
- 学習
- 振り返り
- 改善
- 再設計
- 再始動

すべての出力は最終的に「次の一歩」へ収束します。

## 2. thinking-harness との役割分担

- `thinking-harness`: 考える・分析する・検証する・言語化する
- `execution-harness`: 実行する・測定する・振り返る・改善する・再開する

連携の基本は次の通りです。

1. thinking-harness で `strategy / center_pin / hypothesis` を定義
2. execution-harness で年次〜日次へ落とし込み
3. KPT / YWT で学習し、必要なら thinking-harness に戻って再設計

## 3. 年間→四半期→月次→週次→日次の流れ

1. 年間計画: North Star・重点領域・KPI を定義
2. 四半期計画: 年間テーマを 90 日単位に変換
3. 月次計画: 実行可能なマイルストーンに分解
4. 週次計画: 最重要タスク 3 つを確定
5. 日次ログ: 最重要行動を実行し、障害と学びを記録

## 4. KPT / YWT

- `KPT`: Keep / Problem / Try で実行システムを改善
- `YWT`: やったこと / わかったこと / 次やること で学習を言語化

KPT は運用改善、YWT は学習改善に強みがあります。

## 5. Companion Layer

Companion Layer は、ユーザーを責めずに並走する支援レイヤーです。

- 進んだことを可視化
- 止まっている理由を整理
- タスクを最小行動に分解
- 再開しやすい 10 分アクションに落とす

関連テンプレート:

- `templates/companion_checkin.md`
- `templates/stuck_recovery.md`
- `templates/gentle_progress_review.md`
- `templates/goal_guidance.md`
- `templates/motivation_reset.md`
- `templates/next_step_coaching.md`

## 6. 止まったときの使い方

1. `templates/stuck_recovery.md` を開く
2. 「どこで止まっているか」「原因」を言語化
3. 10 分で終わる再開アクションを決める
4. `templates/daily_log.md` に今日の最小行動として登録

## 7. 実行OSとしての思想

- 評価ではなく学習
- 反省ではなく改善
- 根性論ではなく再設計
- 管理ではなく伴走

## 8. CLIの使い方

### プラン生成

```bash
python scripts/generate_plan.py
```

- 入力: `plans/yearly/*.md`, `plans/monthly/*.md`, `plans/weekly/*.md`
- 出力: `outputs/generated_plan.md`

### レビュー生成

```bash
python scripts/generate_review.py
```

- 入力: `reviews/kpt/*.md`, `reviews/ywt/*.md`
- 出力: `outputs/generated_review.md`

### テスト

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest -q
```

### CI（GitHub Actions）

- Push / Pull Request（`main` 向け）で自動的に `python3 -m pytest -q` を実行
- Python `3.11` / `3.12` の両方で検証
- 定義ファイル: `.github/workflows/pytest.yml`
- 依存定義: `requirements-dev.txt`

## 9. 実行コマンド

初回運用の推奨フロー:

```bash
cp templates/yearly_plan.md plans/yearly/2026.md
cp templates/monthly_plan.md plans/monthly/2026-01.md
cp templates/weekly_plan.md plans/weekly/2026-W01.md
python scripts/generate_plan.py
python scripts/generate_review.py
python3 -m pip install -r requirements-dev.txt
python3 -m pytest -q
```

## 10. KPT改善バックログ運用

週次で詰まりを改善へ接続するため、`dashboards/improvement_backlog.md` を運用します。

1. `reviews/kpt/` の `Problem` / `Try` を抽出
2. `dashboards/improvement_backlog.md` に追加
3. `Priority=High` を翌週 `plans/weekly/` の最重要タスクへ反映
4. 実行結果を `Result` と `Next Step` に記録

## 11. 品質バー

運用品質の基準は `docs/quality_bar.md` にまとめています。

- テンプレート必須セクションを維持
- プロンプトの8項目構造を維持
- すべてのテンプレートを「次の一歩」へ収束
- GitHub Actions とローカル `pytest` を通過
- GitHub側の保護設定は `docs/repository_settings.md` に記録

## 12. examples の説明

`examples/` には、以下テーマの実例を収録しています。

**テーマ:** 2026年、自社EC売上責任者に近づくための年間実行計画

- `sample_strategy_input.md`: thinking-harness 由来の戦略入力
- `sample_yearly_plan.md`: 年間計画サンプル
- `sample_monthly_plan.md`: 月次計画サンプル
- `sample_weekly_plan.md`: 週次行動サンプル
- `sample_kpt_review.md`: 改善ベース振り返り
- `sample_ywt_review.md`: 学習ベース振り返り
- `sample_companion_checkin.md`: 並走チェックイン例
- `sample_stuck_recovery.md`: 再始動テンプレート例

## 13. 将来的な拡張案

1. 指標の時系列ダッシュボード自動更新
2. KPT / YWT から改善提案を自動抽出
3. thinking-harness 連携の差分比較レポート
4. 再始動支援（stuck recovery）の優先度推奨
5. 週次計画から日次タスク候補を自動生成

## 14. 次の一歩

1. `templates/strategy_to_execution.md` を使って戦略を年次計画へ変換
2. `plans/yearly/` に当年計画を1本作成
3. 今週分の `plans/weekly/` を作成し、最重要タスク3つを確定
