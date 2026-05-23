# Workflow

## End-to-End Flow

```text
thinking-harness
  ↓
strategy / center_pin / hypothesis
  ↓
execution-harness
  ↓
yearly
  ↓
quarterly
  ↓
monthly
  ↓
weekly
  ↓
daily
  ↓
KPT / YWT
  ↓
improvement
  ↓
restart
  ↓
(必要なら thinking-harness に戻る)
```

## Operational Guidance

1. 戦略入力を `templates/strategy_to_execution.md` で構造化
2. 年間方針を `plans/yearly/` に確定
3. 四半期・月次・週次に順次分解
4. 日次ログで実行実績と障害を記録
5. KPT/YWT で改善点と学習を抽出
6. 改善施策を次週/月の計画へ反映
7. 進めない場合は Companion Layer で再始動

## Restart Triggers

- 2週連続で最重要タスク未達
- KPI が連続悪化
- 実行負荷が高すぎる
- 目的と行動の接続が曖昧

上記のいずれかが発生したら、止まる前に再設計します。
