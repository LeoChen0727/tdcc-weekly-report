# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-07-05 04:40:39 Asia/Taipei
- purpose: convert parameter backtests into program-side reporting recommendations
- entry_basis: signal date next trading day open
- close_return: D+n close divided by next open minus 1
- high_return: max intraday high through D+n divided by next open minus 1
- rule: recommendations affect reporting and model research priority only; do not silently change core weights

## Usage Summary

| recommended_usage | count |
| --- | --- |
| intraday_target_watch | 56 |
| research_only | 28 |
| promote_to_pdf_core | 2 |

## Top Recommendations

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w_bottom_right_side | w_bottom_early_entry_operation_v2 | promote_to_pdf_core | D+20/D+40 | 58.0645 | 11.2532 |  |  | 44 | Approved operation w_bottom_early_entry_operation_v2_20260629; positive-return rate 58.0645 uses positive exits over evaluated rows. Average return 11.2532; min return -12.7202 after W-structure-low close stop. buy_filter_id=smooth_core_mainstream_right_rebound_5_20_bull. |
| neckline_volume_breakout_confirmation | neckline_strict_45_signal_90_score_v1 | promote_to_pdf_core | D+20 | 63.8889 | 4.3784 |  |  | 51 | Approved operation neckline_strict_45_signal_90_score_v1_20260629; pure win rate 63.8889 uses win/(win+loss). Inclusive success 74.5098 includes neutral rows and must not be labeled as pure win rate. buy_filter_id=broad_45_non_bearish_with_90_warning; 90d bearish context remains eligible as score/risk adjustment. |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | intraday_target_watch | D+10 | 51.03 | 3.92 | D+20 | 79.05 | 348 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | intraday_target_watch | D+10 | 47.5 | 2.9 | D+20 | 75.68 | 1960 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | intraday_target_watch | D+10 | 45.17 | 2.15 | D+20 | 73.89 | 3417 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | intraday_target_watch | D+10 | 44.46 | 1.93 | D+20 | 72.96 | 3101 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 47.76 | 1.84 | D+20 | 69.04 | 2139 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | production_current_proxy | intraday_target_watch | D+10 | 45.87 | 1.84 | D+20 | 68.82 | 87366 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | intraday_target_watch | D+10 | 43.33 | 1.84 | D+20 | 71.19 | 2309 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 46.25 | 1.8 | D+20 | 69.56 | 1340 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | intraday_target_watch | D+10 | 44.23 | 1.77 | D+20 | 71.68 | 3832 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | intraday_target_watch | D+10 | 44.22 | 1.74 | D+20 | 70.27 | 4824 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | production_current_proxy | intraday_target_watch | D+10 | 50.94 | 1.73 | D+20 | 62.96 | 38487 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 47.58 | 1.73 | D+20 | 69.25 | 3061 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | production_current | intraday_target_watch | D+10 | 44.23 | 1.69 | D+20 | 72.31 | 4370 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | intraday_target_watch | D+10 | 42.99 | 1.69 | D+20 | 69.39 | 3321 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | intraday_target_watch | D+10 | 42.99 | 1.68 | D+20 | 70.4 | 2754 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | intraday_target_watch | D+10 | 51.38 | 1.66 | D+20 | 61.95 | 27995 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | intraday_target_watch | D+10 | 50.02 | 1.61 | D+20 | 63.24 | 43725 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | intraday_target_watch | D+10 | 44.14 | 1.61 | D+20 | 70.62 | 3799 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | intraday_target_watch | D+10 | 43.89 | 1.6 | D+20 | 72.13 | 3035 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | intraday_target_watch | D+10 | 42.92 | 1.56 | D+20 | 69.73 | 2560 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | intraday_target_watch | D+10 | 43.72 | 1.55 | D+20 | 72.96 | 2487 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | intraday_target_watch | D+10 | 42.55 | 1.46 | D+20 | 70.85 | 2137 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | intraday_target_watch | D+10 | 42.45 | 1.45 | D+20 | 71.17 | 1808 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 43.83 | 1.71 | D+20 | 72.15 | 12186 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1.2 | research_only | D+10 | 44.82 | 1.06 | D+20 | 55.66 | 87135 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1 | research_only | D+10 | 44.72 | 1.06 | D+20 | 55.63 | 75599 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1.5 | research_only | D+10 | 44.82 | 1.05 | D+20 | 55.57 | 98184 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1 | research_only | D+10 | 44.45 | 0.96 | D+20 | 53.99 | 67318 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near5_vol1.5 | research_only | D+10 | 43.04 | 0.96 | D+20 | 57.06 | 13472 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near3_vol1.5 | research_only | D+10 | 42.94 | 0.95 | D+20 | 56.41 | 8113 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | research_only | D+10 | 44.5 | 0.94 | D+20 | 53.97 | 77217 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | research_only | D+10 | 44.48 | 0.93 | D+20 | 53.78 | 86476 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near3_vol1.2 | research_only | D+10 | 43.15 | 0.9 | D+20 | 54.43 | 11166 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near5_vol1.2 | research_only | D+10 | 43.22 | 0.88 | D+20 | 55.39 | 18946 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1 | research_only | D+10 | 44.31 | 0.85 | D+20 | 51.49 | 52526 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | research_only | D+10 | 44.32 | 0.82 | D+20 | 51.35 | 59707 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | research_only | D+10 | 44.23 | 0.81 | D+20 | 51.06 | 66210 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.95 | 0.74 | D+20 | 63.48 | 8203 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.5 | research_only | D+10 | 42.69 | 0.43 | D+20 | 46.97 | 7944 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | solid_volume_red_k_vol1.2 | research_only | D+10 | 42.68 | 0.4 | D+20 | 47.62 | 16206 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | volume_red_k_vol1.2 | research_only | D+10 | 42.46 | 0.39 | D+20 | 48.7 | 30879 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.2 | research_only | D+10 | 42.48 | 0.37 | D+20 | 45.69 | 11548 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 42.48 | 0.34 | D+20 | 44.97 | 8757 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.5 | research_only | D+10 | 42.23 | 0.34 | D+20 | 46.43 | 6220 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | solid_volume_red_k_vol1.5 | research_only | D+10 | 42.2 | 0.25 | D+20 | 47.27 | 10435 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.65 | 0.25 | D+20 | 63.94 | 3396 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 41.56 | 0.21 | D+20 | 41.99 | 5914 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 41.65 | 0.2 | D+20 | 42.28 | 8198 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
