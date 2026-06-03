# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-06-03 20:26:19 Asia/Taipei
- purpose: convert parameter backtests into program-side reporting recommendations
- entry_basis: signal date next trading day open
- close_return: D+n close divided by next open minus 1
- high_return: max intraday high through D+n divided by next open minus 1
- rule: recommendations affect reporting and model research priority only; do not silently change core weights

## Usage Summary

| recommended_usage | count |
| --- | --- |
| intraday_target_watch | 55 |
| research_only | 14 |
| score_component_only | 3 |
| promote_to_pdf_core | 2 |

## Top Recommendations

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | promote_to_pdf_core | D+10 | 75.28 | 14.28 | D+10 | 87.64 | 200 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | promote_to_pdf_core | D+10 | 65.86 | 10.88 | D+10 | 73.54 | 1052 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | score_component_only | D+10 | 48.79 | 1.78 | D+20 | 44.1 | 22504 | 單獨模型勝率不足，但平均報酬略正；可當 TDCC、營收、族群或權證共振的加分項。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | score_component_only | D+10 | 51.03 | 1.65 | D+20 | 45.17 | 13028 | 單獨模型勝率不足，但平均報酬略正；可當 TDCC、營收、族群或權證共振的加分項。 |
| tdcc_stealth_accumulation | tdcc_up3_range10 | score_component_only | D+6 | 45.84 | 0.31 | D+20 | 46.99 | 7477 | 單獨模型勝率不足，但平均報酬略正；可當 TDCC、營收、族群或權證共振的加分項。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 48.96 | 2.7 | D+20 | 69.72 | 1488 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 49.71 | 2.6 | D+20 | 69.22 | 2340 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 49.37 | 2.28 | D+20 | 68.44 | 3305 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| w_bottom_right_side | wproxy_vol1 | intraday_target_watch | D+10 | 43.67 | 1.07 | D+20 | 58.52 | 48575 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| w_bottom_right_side | wproxy_vol1.2 | intraday_target_watch | D+10 | 43.36 | 1.07 | D+20 | 59.23 | 39236 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| w_bottom_right_side | wproxy_vol1.5 | intraday_target_watch | D+10 | 42.93 | 1.05 | D+20 | 60.4 | 29383 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-4_7_volmax1.5 | intraday_target_watch | D+10 | 44.0 | 0.89 | D+20 | 52.3 | 95953 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-4_7_volmax1.2 | intraday_target_watch | D+10 | 43.94 | 0.88 | D+20 | 52.26 | 85371 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-4_7_volmax1 | intraday_target_watch | D+10 | 43.84 | 0.88 | D+20 | 52.14 | 74311 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| near_high_neckline_challenge | near5_vol1.5 | intraday_target_watch | D+10 | 42.32 | 0.82 | D+20 | 53.58 | 12920 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| near_high_neckline_challenge | near3_vol1.5 | intraday_target_watch | D+10 | 42.42 | 0.81 | D+20 | 52.85 | 7747 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-2.5_5_volmax1 | intraday_target_watch | D+10 | 43.56 | 0.78 | D+20 | 50.8 | 66268 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | intraday_target_watch | D+10 | 43.67 | 0.77 | D+20 | 50.8 | 84688 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | intraday_target_watch | D+10 | 43.62 | 0.77 | D+20 | 50.86 | 75791 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| near_high_neckline_challenge | near3_vol1.2 | intraday_target_watch | D+10 | 42.63 | 0.76 | D+20 | 50.68 | 10635 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| near_high_neckline_challenge | near5_vol1.2 | intraday_target_watch | D+10 | 42.33 | 0.71 | D+20 | 51.68 | 18150 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | w10_vol1.2_width25 | intraday_target_watch | D+10 | 41.52 | 0.71 | D+20 | 59.06 | 14041 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-1.5_3_volmax1 | intraday_target_watch | D+10 | 43.41 | 0.68 | D+20 | 48.59 | 51829 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | w10_vol2_width25 | intraday_target_watch | D+10 | 40.9 | 0.68 | D+20 | 60.96 | 9746 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | intraday_target_watch | D+10 | 43.44 | 0.67 | D+20 | 48.55 | 58784 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 44.53 | 1.87 | D+20 | 71.32 | 12136 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.57 | 0.67 | D+20 | 62.73 | 7473 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.2 | research_only | D+10 | 41.37 | 0.28 | D+20 | 44.76 | 11155 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 41.3 | 0.23 | D+20 | 43.7 | 8424 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| revenue_unreacted_range_proxy | range23_tol5 | research_only | D+10 | 42.95 | 0.2 | D+20 | 36.14 | 327127 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| revenue_unreacted_range_proxy | range23_tol10 | research_only | D+10 | 42.92 | 0.19 | D+20 | 36.24 | 328692 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 41.03 | 0.17 | D+20 | 41.55 | 8113 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.5 | research_only | D+10 | 40.97 | 0.17 | D+20 | 42.96 | 5707 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 40.99 | 0.16 | D+20 | 41.03 | 5809 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.5 | research_only | D+8 | 40.73 | 0.14 | D+20 | 42.73 | 4178 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.37 | 0.08 | D+20 | 63.62 | 3144 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| volume_range_breakout | w30_vol1.2_width12 | research_only | D+1 | 35.61 | -0.46 | D+20 | 42.89 | 2199 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| volume_range_breakout | w30_vol1.5_width12 | research_only | D+1 | 34.44 | -0.52 | D+20 | 43.5 | 1954 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol10_solid_red | research_only | D+8 | 38.45 | -0.63 | D+20 | 63.75 | 794 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
