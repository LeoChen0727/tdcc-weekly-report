# 每日候選股模型績效月報

- generated_at: `2026-05-25 22:25:00 Asia/Taipei`
- latest_signal_date: `20260525`
- signal_count: `1542`
- period: latest signal month

## 市場背景摘要

- TWSE: close=43644.4, 5d=+6.73%, 10d=+4.44%, 20d=+12.10%, above_ma20=True, above_ma60=True
- TPEX: close=434.99, 5d=+6.19%, 10d=+3.08%, 20d=+14.01%, above_ma20=True, above_ma60=True

## 絕對報酬 vs 相對報酬：分類

| category | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d5 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pattern | 744 |  |  |  |  |  |  | 7.544435659223723 | 0.9379156139076672 |
| pullback_rebound | 16 |  |  |  |  |  |  |  |  |
| range_rebound | 224 |  |  |  |  |  |  | 5.5456086413809995 | -2.1454708344092697 |
| revenue_breakout_low_response | 58 |  |  |  |  |  |  | 2.5441044164695836 | -2.059571210176799 |
| revenue_pullback | 426 |  |  |  |  |  |  | 4.267051093887376 | -1.4594145639153333 |
| true_breakout | 74 |  |  |  |  |  |  |  |  |

## TDCC 分層效果

| tdcc_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| distribution_warning | 679 |  |  |  |  | 6.46857386717098 | -0.173490362400749 |
| mild_accumulation | 630 |  |  |  |  | 5.729112429055061 | -0.6467777250424832 |
| neutral | 7 |  |  |  |  | 5.969823307524319 | -0.29382568989477775 |
| strong_accumulation | 223 |  |  |  |  | 5.301493334969054 | -0.7035673340218805 |
| 無TDCC資料 | 3 |  |  |  |  | 6.536091549295775 | 2.5198063380281632 |

## 權證分層效果

| warrant_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 719 |  |  |  |  |
| call_inflow | 67 |  |  |  |  |
| call_put_bullish | 39 |  |  |  |  |
| call_strong_inflow | 71 |  |  |  |  |
| mixed_flow | 14 |  |  |  |  |
| no_signal | 632 |  |  |  |  |

## 族群表現

| sector | sub_theme | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | 1484 |  |  |  |  |
| cyclical_turnaround | cyclical_turnaround | 10 |  |  |  |  |
| mainstream_growth | mainstream_growth | 23 |  |  |  |  |
| neutral | neutral | 25 |  |  |  |  |

## 營收類型比較

| revenue_signal_type | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 1039 |  |  |  |  |
| 出貨型營收 / 其他 | 436 |  |  |  |  |
| 營建認列型 / 交屋認列型 | 67 |  |  |  |  |

## 財報 / 事件催化層績效

### 類事欣科型

| similar_to_shihsinko_flag | signal_count | avg_return_d5 | avg_return_d10 | avg_return_d20 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
|  | 565 |  |  |  |  |  |
| False | 977 |  |  |  |  |  |

### EPS / 毛利率 / 營收待確認

| eps_surprise_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 977 |  |  |  |

| margin_improvement_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 977 |  |  |  |

| revenue_good_eps_unconfirmed_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 742 |  |  |  |
| True | 235 |  |  |  |

### 利多反應程度

| low_reaction_after_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 192 |  |  |  |
| True | 785 |  |  |  |

| already_reacted_to_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 862 |  |  |  |
| True | 115 |  |  |  |

## 不同市場背景下的分類表現

| category | market_regime | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
| pattern | strong_bull | 744 |  |  |  |
| pullback_rebound | strong_bull | 16 |  |  |  |
| range_rebound | strong_bull | 224 |  |  |  |
| revenue_breakout_low_response | strong_bull | 58 |  |  |  |
| revenue_pullback | strong_bull | 426 |  |  |  |
| true_breakout | strong_bull | 74 |  |  |  |

## 判讀規則

- 不只看個股絕對報酬，必須同時看是否跑贏 benchmark。
- 大盤大漲時，個股小漲但落後 benchmark，應視為相對弱勢。
- 大盤下跌時，個股小跌但明顯跑贏 benchmark，可標示為相對抗跌。
- MFE 高但收盤報酬低，代表訊號可能有效但需要後續出場規則。
- 最新未成熟批次不視為正面或負面，等 D+N 交易日成熟後再納入判斷。
