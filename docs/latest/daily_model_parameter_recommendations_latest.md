# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-05-30 20:22:42 Asia/Taipei
- purpose: convert parameter backtests into program-side reporting recommendations
- entry_basis: signal date next trading day open
- close_return: D+n close divided by next open minus 1
- high_return: max intraday high through D+n divided by next open minus 1
- rule: recommendations affect reporting and model research priority only; do not silently change core weights

## Usage Summary

| recommended_usage | count |
| --- | --- |
| intraday_target_watch | 56 |
| research_only | 14 |
| promote_to_pdf_core | 2 |
| score_component_only | 2 |

## Top Recommendations

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | promote_to_pdf_core | D+10 | 76.71 | 15.56 | D+10 | 89.04 | 161 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | promote_to_pdf_core | D+10 | 63.23 | 9.18 | D+10 | 71.43 | 903 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | score_component_only | D+7 | 48.17 | 1.09 | D+20 | 44.94 | 11599 | 單獨模型勝率不足，但平均報酬略正；可當 TDCC、營收、族群或權證共振的加分項。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | score_component_only | D+9 | 45.46 | 1.07 | D+20 | 43.79 | 20547 | 單獨模型勝率不足，但平均報酬略正；可當 TDCC、營收、族群或權證共振的加分項。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 48.96 | 2.69 | D+20 | 69.36 | 1480 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 49.67 | 2.59 | D+20 | 68.91 | 2326 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 49.29 | 2.26 | D+20 | 68.14 | 3282 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | intraday_target_watch | D+10 | 44.18 | 1.76 | D+20 | 71.22 | 12006 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| w_bottom_right_side | wproxy_vol1 | intraday_target_watch | D+10 | 43.44 | 1.0 | D+20 | 58.32 | 48061 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| w_bottom_right_side | wproxy_vol1.2 | intraday_target_watch | D+10 | 43.13 | 1.0 | D+20 | 59.03 | 38800 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| w_bottom_right_side | wproxy_vol1.5 | intraday_target_watch | D+10 | 42.69 | 0.97 | D+20 | 60.2 | 29059 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-4_7_volmax1.5 | intraday_target_watch | D+10 | 43.65 | 0.81 | D+20 | 52.13 | 94922 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-4_7_volmax1.2 | intraday_target_watch | D+10 | 43.56 | 0.79 | D+20 | 52.09 | 84445 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-4_7_volmax1 | intraday_target_watch | D+10 | 43.42 | 0.79 | D+20 | 51.95 | 73468 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| near_high_neckline_challenge | near5_vol1.5 | intraday_target_watch | D+10 | 42.03 | 0.74 | D+20 | 53.43 | 12793 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| near_high_neckline_challenge | near3_vol1.5 | intraday_target_watch | D+10 | 42.16 | 0.73 | D+20 | 52.76 | 7657 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| near_high_neckline_challenge | near3_vol1.2 | intraday_target_watch | D+10 | 42.39 | 0.7 | D+20 | 50.55 | 10503 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | intraday_target_watch | D+10 | 43.32 | 0.69 | D+20 | 50.67 | 83867 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | intraday_target_watch | D+10 | 43.25 | 0.68 | D+20 | 50.72 | 75056 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-2.5_5_volmax1 | intraday_target_watch | D+10 | 43.16 | 0.68 | D+20 | 50.64 | 65600 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | w10_vol1.2_width25 | intraday_target_watch | D+10 | 41.42 | 0.68 | D+20 | 58.84 | 13789 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | w10_vol1.5_width25 | intraday_target_watch | D+10 | 40.98 | 0.65 | D+20 | 59.59 | 12129 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | w10_vol2_width25 | intraday_target_watch | D+10 | 40.76 | 0.65 | D+20 | 60.83 | 9607 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| near_high_neckline_challenge | near5_vol1.2 | intraday_target_watch | D+10 | 42.07 | 0.64 | D+20 | 51.52 | 17960 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | ema-1.5_3_volmax1 | intraday_target_watch | D+10 | 43.04 | 0.6 | D+20 | 48.47 | 51372 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.35 | 0.6 | D+20 | 62.65 | 7382 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.2 | research_only | D+10 | 41.27 | 0.26 | D+20 | 44.7 | 10946 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 41.27 | 0.23 | D+20 | 43.61 | 8275 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| revenue_unreacted_range_proxy | range23_tol5 | research_only | D+10 | 42.78 | 0.17 | D+20 | 36.06 | 325154 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| revenue_unreacted_range_proxy | range23_tol10 | research_only | D+10 | 42.76 | 0.17 | D+20 | 36.16 | 326700 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 40.94 | 0.16 | D+20 | 41.45 | 7969 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 40.94 | 0.15 | D+20 | 40.9 | 5714 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.5 | research_only | D+10 | 40.81 | 0.15 | D+20 | 42.87 | 5606 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.5 | research_only | D+10 | 40.89 | 0.12 | D+20 | 42.6 | 4104 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.07 | -0.0 | D+20 | 63.66 | 3113 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| tdcc_stealth_accumulation | tdcc_up3_range10 | research_only | D+9 | 44.3 | -0.01 | D+20 | 46.8 | 6423 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| volume_range_breakout | w30_vol1.2_width12 | research_only | D+1 | 35.27 | -0.48 | D+20 | 42.51 | 2172 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| volume_range_breakout | w30_vol1.5_width12 | research_only | D+1 | 34.15 | -0.53 | D+20 | 43.07 | 1930 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol10_solid_red | research_only | D+8 | 38.39 | -0.62 | D+20 | 63.95 | 789 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
