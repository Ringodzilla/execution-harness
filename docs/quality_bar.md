# Quality Bar

execution-harness は、計画をきれいに保つためではなく、実行・学習・改善・再始動を壊さず回すためのOSです。

## Non-Negotiables

1. すべてのテンプレートは必須セクションを維持する。
2. すべてのプロンプトは `Role / Goal / Input / Process / Output Format / Tone / Constraints / Quality Criteria` を維持する。
3. すべての実行系変更は `python3 -m pytest -q` を通す。
4. すべての計画・レビュー・伴走テンプレートは「次の一歩」へ収束する。
5. KPTのProblem/Tryは、必要に応じて `dashboards/improvement_backlog.md` へ転記する。

## Release Readiness

本番運用可能とみなす最低条件:

- GitHub Actions が成功している
- テンプレート契約テストが成功している
- プロンプト構造テストが成功している
- スクリプト実行テストが成功している
- README / AGENTS / docs が現在の運用と矛盾していない

## Weekly Quality Loop

1. 週次KPTを作成する。
2. `Problem` を仕組みの課題として読み替える。
3. `Try` を改善バックログへ追加する。
4. `High` 優先度から翌週計画へ1件だけ移す。
5. 実行後に `Result` と `Next Step` を更新する。

## Definition of Perfect Enough

完璧とは、失敗しない計画ではなく、失敗・停滞・変更が起きても早く検知し、責めずに再設計して、次の一歩へ戻れる状態です。
