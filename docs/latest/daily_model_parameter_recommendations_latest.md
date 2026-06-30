# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-06-30 11:06:11 Asia/Taipei
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
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | intraday_target_watch | D+10 | 51.45 | 4.31 | D+20 | 86.86 | 332 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | intraday_target_watch | D+10 | 47.69 | 3.08 | D+20 | 82.21 | 1888 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | intraday_target_watch | D+10 | 45.03 | 2.33 | D+20 | 78.73 | 3288 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 47.79 | 1.91 | D+20 | 69.48 | 2105 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | production_current_proxy | intraday_target_watch | D+10 | 52.19 | 1.9 | D+20 | 64.36 | 34681 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | intraday_target_watch | D+10 | 44.31 | 1.9 | D+20 | 73.78 | 3050 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | production_current_proxy | intraday_target_watch | D+10 | 46.06 | 1.89 | D+20 | 69.2 | 85716 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 46.27 | 1.88 | D+20 | 70.02 | 1311 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | intraday_target_watch | D+10 | 52.85 | 1.83 | D+20 | 63.47 | 25125 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 47.8 | 1.81 | D+20 | 69.56 | 3021 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | intraday_target_watch | D+10 | 43.11 | 1.81 | D+20 | 71.68 | 2272 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | intraday_target_watch | D+10 | 51.12 | 1.75 | D+20 | 64.73 | 39655 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | intraday_target_watch | D+10 | 44.18 | 1.74 | D+20 | 70.86 | 4752 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | intraday_target_watch | D+10 | 44.1 | 1.74 | D+20 | 72.46 | 3773 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | intraday_target_watch | D+10 | 42.85 | 1.68 | D+20 | 69.77 | 3269 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | production_current | intraday_target_watch | D+10 | 44.12 | 1.65 | D+20 | 73.14 | 4297 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | intraday_target_watch | D+10 | 42.74 | 1.64 | D+20 | 70.97 | 2711 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | intraday_target_watch | D+10 | 44.08 | 1.59 | D+20 | 71.1 | 3747 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | intraday_target_watch | D+10 | 43.76 | 1.55 | D+20 | 72.81 | 2991 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | intraday_target_watch | D+10 | 42.73 | 1.52 | D+20 | 69.9 | 2523 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | intraday_target_watch | D+10 | 43.58 | 1.51 | D+20 | 73.6 | 2451 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol500 | intraday_target_watch | D+10 | 43.34 | 1.41 | D+20 | 70.28 | 5865 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | intraday_target_watch | D+10 | 43.12 | 1.41 | D+20 | 73.13 | 3705 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 43.72 | 1.72 | D+20 | 72.98 | 12018 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1.2 | research_only | D+10 | 44.95 | 1.08 | D+20 | 55.76 | 85325 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1 | research_only | D+10 | 44.84 | 1.08 | D+20 | 55.72 | 73932 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1.5 | research_only | D+10 | 44.98 | 1.07 | D+20 | 55.67 | 96237 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1 | research_only | D+10 | 44.56 | 0.97 | D+20 | 54.05 | 65836 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near5_vol1.5 | research_only | D+10 | 43.07 | 0.97 | D+20 | 57.48 | 13276 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near3_vol1.5 | research_only | D+10 | 42.97 | 0.96 | D+20 | 56.71 | 7994 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | research_only | D+10 | 44.63 | 0.95 | D+20 | 53.85 | 84767 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | research_only | D+10 | 44.62 | 0.95 | D+20 | 54.03 | 75617 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near3_vol1.2 | research_only | D+10 | 43.28 | 0.92 | D+20 | 54.59 | 11001 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near5_vol1.2 | research_only | D+10 | 43.31 | 0.89 | D+20 | 55.62 | 18677 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1 | research_only | D+10 | 44.44 | 0.85 | D+20 | 51.53 | 51382 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | research_only | D+10 | 44.46 | 0.83 | D+20 | 51.39 | 58478 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | research_only | D+10 | 44.39 | 0.82 | D+20 | 51.11 | 64913 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.85 | 0.72 | D+20 | 63.96 | 8054 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.5 | research_only | D+10 | 42.77 | 0.45 | D+20 | 47.14 | 7835 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.2 | research_only | D+10 | 42.59 | 0.39 | D+20 | 45.75 | 11402 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | volume_red_k_vol1.2 | research_only | D+10 | 42.58 | 0.39 | D+20 | 48.78 | 30382 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | solid_volume_red_k_vol1.2 | research_only | D+10 | 42.79 | 0.38 | D+20 | 47.63 | 15913 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 42.53 | 0.35 | D+20 | 44.98 | 8639 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.5 | research_only | D+10 | 42.26 | 0.34 | D+20 | 46.54 | 6134 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | solid_volume_red_k_vol1.5 | research_only | D+10 | 42.29 | 0.26 | D+20 | 47.44 | 10239 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 41.89 | 0.23 | D+20 | 42.29 | 8100 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.61 | 0.23 | D+20 | 64.47 | 3348 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 41.7 | 0.22 | D+20 | 41.97 | 5838 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
