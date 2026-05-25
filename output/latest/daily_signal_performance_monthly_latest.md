# 每日候選股模型績效月報

- generated_at: `2026-05-26 05:56:31 Asia/Taipei`
- latest_signal_date: `20260526`
- signal_count: `2343`
- period: latest signal month

## 市場背景摘要

- TWSE: close=43644.4, 5d=+6.73%, 10d=+4.44%, 20d=+12.10%, above_ma20=True, above_ma60=True
- TPEX: close=434.99, 5d=+6.19%, 10d=+3.08%, 20d=+14.01%, above_ma20=True, above_ma60=True

## 絕對報酬 vs 相對報酬：分類

| category | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d5 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pattern | 1107 |  |  |  |  |  |  | 7.507448364998513 | 1.4865090054454704 |
| pullback_rebound | 21 |  |  |  |  |  |  | 0.8328934120737626 | -4.682682434397762 |
| range_rebound | 474 |  |  |  |  |  |  | 4.824232281789252 | -2.610062946772949 |
| revenue_breakout_low_response | 83 |  |  |  |  |  |  | 2.3997652379198877 | -1.7499303532685129 |
| revenue_pullback | 584 |  |  |  |  |  |  | 3.733029960430295 | -1.611343175688837 |
| true_breakout | 74 |  |  |  |  |  |  | 0.9188187457053245 | -4.483926709012415 |

## TDCC 分層效果

| tdcc_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 4 |  |  |  |  |  |  |
| distribution_warning | 1030 |  |  |  |  | 6.0580631722372456 | -0.014828597044639269 |
| mild_accumulation | 955 |  |  |  |  | 5.208407032477182 | -0.6899114047229125 |
| neutral | 11 |  |  |  |  | 5.047978293958044 | -0.8321588697460977 |
| strong_accumulation | 339 |  |  |  |  | 4.606637651490633 | -1.0421982275407153 |
| 無TDCC資料 | 4 |  |  |  |  | 6.536091549295775 | 3.198356807511734 |

## 權證分層效果

| warrant_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 1025 |  |  |  |  |
| call_inflow | 166 |  |  |  |  |
| call_put_bullish | 115 |  |  |  |  |
| call_strong_inflow | 193 |  |  |  |  |
| mixed_flow | 30 |  |  |  |  |
| no_signal | 814 |  |  |  |  |

## 族群表現

| sector | sub_theme | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | 2260 |  |  |  |  |
| cyclical_turnaround | cyclical_turnaround | 13 |  |  |  |  |
| mainstream_growth | mainstream_growth | 35 |  |  |  |  |
| neutral | neutral | 35 |  |  |  |  |

## 營收類型比較

| revenue_signal_type | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
|  | 1650 |  |  |  |  |
| 出貨型營收 / 其他 | 601 |  |  |  |  |
| 營建認列型 / 交屋認列型 | 92 |  |  |  |  |

## 財報 / 事件催化層績效

### 類事欣科型

| similar_to_shihsinko_flag | signal_count | avg_return_d5 | avg_return_d10 | avg_return_d20 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
|  | 565 |  |  |  |  |  |
| False | 1778 |  |  |  |  |  |

### EPS / 毛利率 / 營收待確認

| eps_surprise_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 1778 |  |  |  |

| margin_improvement_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 1778 |  |  |  |

| revenue_good_eps_unconfirmed_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 1381 |  |  |  |
| True | 397 |  |  |  |

### 利多反應程度

| low_reaction_after_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 391 |  |  |  |
| True | 1387 |  |  |  |

| already_reacted_to_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
|  | 565 |  |  |  |
| False | 1571 |  |  |  |
| True | 207 |  |  |  |

## 不同市場背景下的分類表現

| category | market_regime | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
| pattern | strong_bull | 1107 |  |  |  |
| pullback_rebound | strong_bull | 21 |  |  |  |
| range_rebound | strong_bull | 474 |  |  |  |
| revenue_breakout_low_response | strong_bull | 83 |  |  |  |
| revenue_pullback | strong_bull | 584 |  |  |  |
| true_breakout | strong_bull | 74 |  |  |  |

## 判讀規則

- 不只看個股絕對報酬，必須同時看是否跑贏 benchmark。
- 大盤大漲時，個股小漲但落後 benchmark，應視為相對弱勢。
- 大盤下跌時，個股小跌但明顯跑贏 benchmark，可標示為相對抗跌。
- MFE 高但收盤報酬低，代表訊號可能有效但需要後續出場規則。
- 最新未成熟批次不視為正面或負面，等 D+N 交易日成熟後再納入判斷。
