# 每日候選股模型績效月報

- generated_at: `2026-07-05 05:07:40 Asia/Taipei`
- latest_signal_date: `20260703`
- signal_count: `1844`
- period: latest signal month

## 市場背景摘要

- TWSE: close=46780.62, 5d=+4.96%, 10d=+0.68%, 20d=+2.42%, above_ma20=True, above_ma60=True
- TPEX: close=445.38, 5d=+7.25%, 10d=-0.38%, 20d=+1.20%, above_ma20=True, above_ma60=True

## 絕對報酬 vs 相對報酬：分類

| category | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d5 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pattern | 649 |  |  |  |  |  |  | 4.133390952036044 | -2.2651959037352234 |
| pullback_rebound | 64 |  |  |  |  |  |  | 3.0384131385206583 | -2.4024730873144744 |
| range_rebound | 450 |  |  |  |  |  |  | 4.472087993537121 | -2.5406871066185452 |
| revenue_breakout_low_response | 116 |  |  |  |  |  |  | 3.384300530891292 | -1.734888507640917 |
| revenue_pullback | 431 |  |  |  |  |  |  | 3.283679383724748 | -2.2203178838199866 |
| true_breakout | 134 |  |  |  |  |  |  | 8.550941680637292 | -2.5525020281594575 |

## TDCC 分層效果

| tdcc_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 9 |  |  |  |  | -0.0036377240870484975 | -2.342954440525874 |
| distribution_warning | 782 |  |  |  |  | 4.071536980337341 | -2.3756171374940145 |
| mild_accumulation | 787 |  |  |  |  | 4.659211705813044 | -2.2027923509363214 |
| neutral | 23 |  |  |  |  | 1.697068532900917 | -4.0407101768178695 |
| strong_accumulation | 243 |  |  |  |  | 3.580241281654058 | -2.1982314321345684 |

## 權證分層效果

| warrant_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 1033 |  |  |  |  |
| call_inflow | 130 |  |  |  |  |
| call_put_bullish | 51 |  |  |  |  |
| call_strong_inflow | 90 |  |  |  |  |
| mixed_flow | 11 |  |  |  |  |
| no_signal | 506 |  |  |  |  |
| put_inflow | 23 |  |  |  |  |

## 族群表現

| sector | sub_theme | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | 1728 |  |  |  |  |
| cyclical_turnaround | cyclical_turnaround | 7 |  |  |  |  |
| mainstream_growth | mainstream_growth | 76 |  |  |  |  |
| neutral | neutral | 33 |  |  |  |  |

## 營收類型比較

| revenue_signal_type | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 1269 |  |  |  |  |
| 出貨型營收 / 其他 | 500 |  |  |  |  |
| 營建認列型 / 交屋認列型 | 75 |  |  |  |  |

## 財報 / 事件催化層績效

### 類事欣科型

| similar_to_shihsinko_flag | signal_count | avg_return_d5 | avg_return_d10 | avg_return_d20 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
| False | 1830 |  |  |  |  |  |
| True | 14 |  |  |  |  |  |

### EPS / 毛利率 / 營收待確認

| eps_surprise_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 1844 |  |  |  |

| margin_improvement_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 1844 |  |  |  |

| revenue_good_eps_unconfirmed_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 1353 |  |  |  |
| True | 491 |  |  |  |

### 利多反應程度

| low_reaction_after_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 1167 |  |  |  |
| True | 677 |  |  |  |

| already_reacted_to_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 692 |  |  |  |
| True | 1152 |  |  |  |

## 不同市場背景下的分類表現

| category | market_regime | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
| pattern | mild_bull | 649 |  |  |  |
| pullback_rebound | mild_bull | 64 |  |  |  |
| range_rebound | mild_bull | 450 |  |  |  |
| revenue_breakout_low_response | mild_bull | 116 |  |  |  |
| revenue_pullback | mild_bull | 431 |  |  |  |
| true_breakout | mild_bull | 134 |  |  |  |

## 判讀規則

- 不只看個股絕對報酬，必須同時看是否跑贏 benchmark。
- 大盤大漲時，個股小漲但落後 benchmark，應視為相對弱勢。
- 大盤下跌時，個股小跌但明顯跑贏 benchmark，可標示為相對抗跌。
- MFE 高但收盤報酬低，代表訊號可能有效但需要後續出場規則。
- 最新未成熟批次不視為正面或負面，等 D+N 交易日成熟後再納入判斷。
