# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-06-30 18:04:14 Asia/Taipei
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
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | intraday_target_watch | D+10 | 50.9 | 4.1 | D+20 | 85.35 | 333 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | intraday_target_watch | D+10 | 47.57 | 2.99 | D+20 | 81.79 | 1901 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | intraday_target_watch | D+10 | 45.01 | 2.28 | D+20 | 78.48 | 3311 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | intraday_target_watch | D+10 | 44.34 | 1.91 | D+20 | 73.73 | 3059 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | production_current_proxy | intraday_target_watch | D+10 | 45.99 | 1.87 | D+20 | 69.16 | 86122 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 47.75 | 1.86 | D+20 | 69.33 | 2114 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 46.33 | 1.84 | D+20 | 69.94 | 1319 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | intraday_target_watch | D+10 | 43.12 | 1.82 | D+20 | 71.62 | 2281 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | production_current_proxy | intraday_target_watch | D+10 | 51.59 | 1.81 | D+20 | 64.17 | 35662 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 47.7 | 1.76 | D+20 | 69.49 | 3033 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | intraday_target_watch | D+10 | 44.22 | 1.75 | D+20 | 70.83 | 4765 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | intraday_target_watch | D+10 | 44.16 | 1.75 | D+20 | 72.41 | 3782 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | intraday_target_watch | D+10 | 52.17 | 1.74 | D+20 | 63.36 | 25843 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | intraday_target_watch | D+10 | 42.9 | 1.7 | D+20 | 69.72 | 3281 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | intraday_target_watch | D+10 | 50.59 | 1.68 | D+20 | 64.57 | 40677 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | production_current | intraday_target_watch | D+10 | 44.14 | 1.66 | D+20 | 73.13 | 4308 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | intraday_target_watch | D+10 | 42.8 | 1.66 | D+20 | 70.89 | 2720 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | intraday_target_watch | D+10 | 44.12 | 1.6 | D+20 | 71.15 | 3756 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | intraday_target_watch | D+10 | 43.82 | 1.57 | D+20 | 72.87 | 2998 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | intraday_target_watch | D+10 | 42.77 | 1.54 | D+20 | 69.95 | 2531 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | intraday_target_watch | D+10 | 43.6 | 1.52 | D+20 | 73.63 | 2458 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | intraday_target_watch | D+10 | 43.38 | 1.43 | D+20 | 70.29 | 5881 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | intraday_target_watch | D+10 | 42.33 | 1.43 | D+20 | 71.26 | 2111 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 43.74 | 1.72 | D+20 | 72.93 | 12045 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1.2 | research_only | D+10 | 44.88 | 1.07 | D+20 | 55.77 | 85860 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1 | research_only | D+10 | 44.77 | 1.07 | D+20 | 55.72 | 74419 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1.5 | research_only | D+10 | 44.89 | 1.06 | D+20 | 55.68 | 96805 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near5_vol1.5 | research_only | D+10 | 43.07 | 0.97 | D+20 | 57.44 | 13313 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1 | research_only | D+10 | 44.48 | 0.96 | D+20 | 54.05 | 66252 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near3_vol1.5 | research_only | D+10 | 42.95 | 0.96 | D+20 | 56.68 | 8015 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | research_only | D+10 | 44.54 | 0.94 | D+20 | 53.86 | 85250 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | research_only | D+10 | 44.54 | 0.94 | D+20 | 54.04 | 76073 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near3_vol1.2 | research_only | D+10 | 43.22 | 0.91 | D+20 | 54.61 | 11026 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near5_vol1.2 | research_only | D+10 | 43.27 | 0.88 | D+20 | 55.62 | 18722 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1 | research_only | D+10 | 44.35 | 0.84 | D+20 | 51.54 | 51709 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | research_only | D+10 | 44.37 | 0.82 | D+20 | 51.4 | 58834 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | research_only | D+10 | 44.29 | 0.81 | D+20 | 51.12 | 65289 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.9 | 0.73 | D+20 | 63.84 | 8083 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.5 | research_only | D+10 | 42.71 | 0.44 | D+20 | 47.19 | 7857 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | solid_volume_red_k_vol1.2 | research_only | D+10 | 42.73 | 0.39 | D+20 | 47.77 | 15962 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.2 | research_only | D+10 | 42.52 | 0.38 | D+20 | 45.87 | 11428 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | volume_red_k_vol1.2 | research_only | D+10 | 42.51 | 0.38 | D+20 | 48.88 | 30465 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 42.46 | 0.34 | D+20 | 45.11 | 8657 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.5 | research_only | D+10 | 42.19 | 0.34 | D+20 | 46.61 | 6149 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | solid_volume_red_k_vol1.5 | research_only | D+10 | 42.26 | 0.26 | D+20 | 47.49 | 10276 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.67 | 0.24 | D+20 | 64.29 | 3357 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 41.76 | 0.22 | D+20 | 42.41 | 8113 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 41.59 | 0.21 | D+20 | 42.14 | 5850 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
