# AGENTS.md

## Mission

execution-harness の目的は、ユーザーを責めずに前進可能な状態を作ることです。抽象論で終わらせず、常に「次の行動」に落とし込んでください。

## Operating Rules

1. テンプレート構造を壊さない
2. テンプレート変更時は `README.md` も必要に応じて更新する
3. 実行可能なコードは必ずテストする
4. 変更後は `pytest` を実行して結果を確認する
5. 抽象論で終わらせない
6. 出力は必ず「次の行動」を含める
7. ユーザーを責めない（評価より学習、反省より改善）
8. タスクが重い場合は、最小実行単位へ分解する
9. 止まりを検知したら `Companion Layer` テンプレートを優先提案する

## Change Management

- 既存ファイルを更新する際は、運用中ユーザーがそのまま使える後方互換を意識する
- 命名規則はシンプル・一貫・検索可能を優先する
- 追加したテンプレートやプロンプトには、実行導線（次の一歩）を明示する

## Minimum QA Checklist

- 必須ディレクトリ/ファイルが存在する
- templates/prompts/examples が要件を満たす
- templates は必須セクションバリデータを通過する
- prompts は8項目構造バリデータを通過する
- scripts が単体で実行できる
- outputs が生成される
- `pytest` が通る

## CI Rule

- `main` 向け Push/PR では GitHub Actions の `python3 -m pytest -q` を通過させる
- CI は Python 3.11 / 3.12 の両方で検証する
- テストが失敗している状態でのマージは行わない

## Quality Bar

- `docs/quality_bar.md` を品質基準の一次情報として扱う
- テンプレート、プロンプト、スクリプト、README/AGENTS の運用説明が矛盾しないように保つ
- KPTで見つけた仕組みの課題は `dashboards/improvement_backlog.md` に転記し、翌週計画へ接続する

## Companion Behavior

- トーンは丁寧・率直・前向き
- 曖昧さを残さない
- 進捗の詰問をしない
- 失敗を人格ではなくシステム課題として扱う

## Definition of Done

- 実行・測定・振り返り・改善・再始動の循環が設計されている
- thinking-harness との接続が明文化されている
- すべての主要テンプレートに「次の一歩」がある
- テストが通過している
