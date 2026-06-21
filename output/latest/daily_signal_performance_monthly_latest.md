# 每日候選股模型績效月報

- generated_at: `2026-06-21 21:30:16 Asia/Taipei`
- latest_signal_date: `20260618`
- signal_count: `5211`
- period: latest signal month

## 市場背景摘要

- TWSE: close=46465.2, 5d=+7.68%, 10d=+1.72%, 20d=+12.32%, above_ma20=True, above_ma60=True
- TPEX: close=447.06, 5d=+9.82%, 10d=+1.58%, 20d=+9.09%, above_ma20=True, above_ma60=True

## 絕對報酬 vs 相對報酬：分類

| category | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d5 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pattern | 2291 | 0.40972563403138434 | 2.989304862270274 | 3.0438289653298876 | 3.479493165659199 | 52.749719416386085 | 54.7699214365881 | 9.874395489883 | -5.026101044521757 |
| revenue_breakout_low_response | 160 | 1.9939729359842513 | 2.195725547633788 | 2.121307178812429 | 3.447943624757878 | 63.63636363636363 | 63.63636363636363 | 6.532050217189644 | -3.413151554323771 |
| range_rebound | 1075 | -1.8399754286956214 | -0.7888027799109768 | 1.0407571668247309 | -0.7678242113971173 | 43.89312977099237 | 45.61068702290076 | 7.426921542534263 | -6.726419853763716 |
| true_breakout | 436 | -3.0393369919143307 | -3.2483781000629217 | -0.6940492840188485 | -3.1659556390853334 | 31.63265306122449 | 31.122448979591837 | 10.360737686756115 | -8.838666298036555 |
| pullback_rebound | 152 | 0.1707126288975147 | 4.3737932298337405 |  |  | 75.0 |  | 8.446957956029705 | -4.422381791602117 |
| revenue_pullback | 1097 | -0.18002159384705438 | 0.4453946639131219 |  |  | 54.330708661417326 |  | 7.693225114654569 | -4.709487851322978 |

## TDCC 分層效果

| tdcc_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | avg_mfe_d10 | avg_mae_d10 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 無TDCC資料 | 1 | 8.824823943661976 | 13.3362676056338 | 13.205957231820808 | 100.0 | 18.39788732394365 | 4.84154929577465 |
| mild_accumulation | 2170 | -0.43428746791659106 | 1.2892134150949686 | 1.806620837834943 | 50.75566750629723 | 9.353000914427103 | -5.4561345725136885 |
|  | 26 | 0.8550719031985242 | 1.6404376887033336 | 1.6892530315988663 | 33.33333333333333 | 4.167561674100997 | -2.1395982911137295 |
| strong_accumulation | 777 | 0.03221669073508291 | 1.832715209553724 | 1.6450683553158372 | 53.04659498207885 | 8.229445254501073 | -5.2788017584889735 |
| distribution_warning | 2203 | -0.696876497399057 | 0.6766808920553687 | 0.872072057291101 | 47.251461988304094 | 8.458633769138965 | -5.613944091005009 |
| neutral | 34 | -5.312161705740297 | -5.11807563173266 | -5.511830356917452 | 25.0 | 8.091542261302898 | -8.425536019752721 |

## 權證分層效果

| warrant_status | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- |
| put_inflow | 38 | 8.994295109901557 | 15.959729435615191 | 17.84824911155163 | 50.0 |
|  | 2343 | -0.014719303456702477 | 2.332588191623062 | 2.6970183001720054 | 54.42260442260442 |
| call_strong_inflow | 241 | 0.043881379394961305 | 0.964527430000639 | 1.4884007394015735 | 45.63106796116505 |
| no_signal | 1977 | -1.3443768697700926 | 0.14469797122464317 | 0.13900767903120367 | 47.07379134860051 |
| call_inflow | 444 | -1.2137507349083403 | -0.6497575579596477 | -0.1983523364940904 | 41.05263157894737 |
| call_put_bullish | 142 | -1.054129115178865 | -1.920133942233106 | -2.337970178294873 | 40.0 |
| mixed_flow | 26 | 3.7566732886232685 | -2.2427360695906415 | -2.373046443403633 | 33.33333333333333 |

## 族群表現

| sector | sub_theme | signal_count | avg_return_d5 | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
| neutral | neutral | 65 | 5.112265303095408 | 9.52394362101682 | 10.77616169814091 | 100.0 |
|  |  | 5051 | -0.5655873925534678 | 1.04018086020758 | 1.2894855484602923 | 49.14463452566096 |
| cyclical_turnaround | cyclical_turnaround | 11 | -0.7101348639583434 | -0.9567039138428527 | 0.2955141632812371 | 33.33333333333333 |
| mainstream_growth | mainstream_growth | 84 | -0.04893346534790309 | -3.453941879967948 | -2.2017238028438575 | 40.0 |

## 營收類型比較

| revenue_signal_type | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | win_rate_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
| 營建認列型 / 交屋認列型 | 308 | 4.9042175984095495 | 4.970970045723987 | 87.34177215189874 | 83.33333333333334 |
| 出貨型營收 / 其他 | 1111 | -0.03791339686949989 | 1.652424635626975 | 50.20242914979757 | 42.857142857142854 |
|  | 3792 | 1.0318438523943245 | 1.2039945711143702 | 47.323076923076925 | 48.12221514958625 |

## 財報 / 事件催化層績效

### 類事欣科型

| similar_to_shihsinko_flag | signal_count | avg_return_d5 | avg_return_d10 | avg_return_d20 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- | --- |
| False | 5194 | -0.5018676228037557 | 1.0532110924594387 |  | 1.318564591741705 | 49.11206368646663 |
| True | 17 |  |  |  |  |  |

### EPS / 毛利率 / 營收待確認

| eps_surprise_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 5211 | 1.0532110924594387 | 1.318564591741705 | 49.11206368646663 |

| margin_improvement_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 5211 | 1.0532110924594387 | 1.318564591741705 | 49.11206368646663 |

| revenue_good_eps_unconfirmed_flag | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| True | 1148 | -0.561115427672826 | 3.4479436247578787 | 63.63636363636363 |
| False | 4063 | 1.2807272862324655 | 1.2894855484602923 | 48.9137181874612 |

### 利多反應程度

| low_reaction_after_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| True | 4449 | 2.1665348570944127 | 2.657210957454229 | 53.89408099688473 |
| False | 762 | -3.374522961280164 | -3.6064266219399004 | 31.51862464183381 |

| already_reacted_to_catalyst | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- |
| False | 4923 | 1.5473352463719976 | 1.96973668458644 | 51.356852103120765 |
| True | 288 | -4.057526522717555 | -4.718087388466717 | 28.30188679245283 |

## 不同市場背景下的分類表現

| category | market_regime | signal_count | avg_return_d10 | avg_relative_return_vs_benchmark_d10 | benchmark_outperform_rate_d10 |
| --- | --- | --- | --- | --- | --- |
| pattern | strong_bull | 2172 | 2.989304862270274 | 3.4794931656591985 | 54.7699214365881 |
| revenue_breakout_low_response | strong_bull | 135 | 2.195725547633788 | 3.447943624757878 | 63.63636363636363 |
| range_rebound | strong_bull | 1034 | -0.7888027799109767 | -0.7678242113971173 | 45.61068702290076 |
| true_breakout | strong_bull | 405 | -3.2483781000629217 | -3.1659556390853334 | 31.122448979591837 |
| pattern | correction | 119 |  |  |  |
| pullback_rebound | correction | 10 |  |  |  |
| pullback_rebound | strong_bull | 142 | 4.3737932298337405 |  |  |
| range_rebound | correction | 41 |  |  |  |
| revenue_breakout_low_response | correction | 25 |  |  |  |
| revenue_pullback | correction | 158 |  |  |  |
| revenue_pullback | strong_bull | 939 | 0.4453946639131218 |  |  |
| true_breakout | correction | 31 |  |  |  |

## 判讀規則

- 不只看個股絕對報酬，必須同時看是否跑贏 benchmark。
- 大盤大漲時，個股小漲但落後 benchmark，應視為相對弱勢。
- 大盤下跌時，個股小跌但明顯跑贏 benchmark，可標示為相對抗跌。
- MFE 高但收盤報酬低，代表訊號可能有效但需要後續出場規則。
- 最新未成熟批次不視為正面或負面，等 D+N 交易日成熟後再納入判斷。
