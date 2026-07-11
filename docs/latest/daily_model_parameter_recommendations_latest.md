# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-07-11 16:08:22 Asia/Taipei
- purpose: convert parameter backtests into program-side reporting recommendations
- entry_basis: signal date next trading day open
- close_return: D+n close divided by next open minus 1
- high_return: max intraday high through D+n divided by next open minus 1
- rule: recommendations affect reporting and model research priority only; do not silently change core weights

## Usage Summary

| recommended_usage | count |
| --- | --- |
| intraday_target_watch | 56 |
| research_only | 29 |
| promote_to_pdf_core | 3 |

## Top Recommendations

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w_bottom_right_side | w_bottom_early_entry_operation_v2 | promote_to_pdf_core | D+20/D+40 | 58.0645 | 11.2532 |  |  | 44 | Approved operation w_bottom_early_entry_operation_v2_20260629; positive-return rate 58.0645 uses positive exits over evaluated rows. Average return 11.2532; min return -12.7202 after W-structure-low close stop. buy_filter_id=smooth_core_mainstream_right_rebound_5_20_bull. |
| volume_range_breakout_v2_high_position_volume_attack | volume_range_breakout_v2_high_position_operation_v1 | promote_to_pdf_core | D+15_operation | 62.34 | 9.48 | D+1 |  | 231 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| neckline_volume_breakout_confirmation | neckline_strict_45_signal_90_score_v1 | promote_to_pdf_core | D+20 | 63.8889 | 4.3784 |  |  | 51 | Approved operation neckline_strict_45_signal_90_score_v1_20260629; pure win rate 63.8889 uses win/(win+loss). Inclusive success 74.5098 includes neutral rows and must not be labeled as pure win rate. buy_filter_id=broad_45_non_bearish_with_90_warning; 90d bearish context remains eligible as score/risk adjustment. |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | intraday_target_watch | D+10 | 47.38 | 2.84 | D+20 | 80.22 | 371 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | intraday_target_watch | D+10 | 45.02 | 2.36 | D+20 | 76.74 | 2163 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout_v2_low_position_volume_attack | volume_range_breakout_v2_low_position_operation_v1 | intraday_target_watch | D+10 | 45.02 | 2.25 | D+20 | 68.79 | 523 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | intraday_target_watch | D+10 | 44.33 | 1.92 | D+20 | 73.0 | 3160 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 47.99 | 1.84 | D+20 | 68.95 | 2185 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | production_current_proxy | intraday_target_watch | D+10 | 45.73 | 1.78 | D+20 | 69.11 | 89287 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 46.35 | 1.76 | D+20 | 69.35 | 1364 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | intraday_target_watch | D+10 | 44.13 | 1.76 | D+20 | 71.7 | 3906 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | intraday_target_watch | D+10 | 44.16 | 1.74 | D+20 | 70.22 | 4927 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | intraday_target_watch | D+10 | 43.05 | 1.74 | D+20 | 71.32 | 2352 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 47.78 | 1.73 | D+20 | 69.26 | 3121 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| price_pullback_23ema | price_pullback_23ema_prev20_breakout_stop_v1 | intraday_target_watch | D+10 | 50.38 | 1.72 | D+20 | 61.17 | 9612 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | intraday_target_watch | D+10 | 43.12 | 1.66 | D+20 | 75.0 | 3804 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | intraday_target_watch | D+10 | 42.82 | 1.64 | D+20 | 69.42 | 3389 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | intraday_target_watch | D+10 | 44.06 | 1.62 | D+20 | 70.56 | 3880 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | production_current_proxy | intraday_target_watch | D+10 | 50.84 | 1.61 | D+20 | 63.85 | 41834 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | intraday_target_watch | D+10 | 42.77 | 1.61 | D+20 | 70.5 | 2804 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | intraday_target_watch | D+10 | 43.78 | 1.59 | D+20 | 72.1 | 3093 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | intraday_target_watch | D+10 | 43.62 | 1.56 | D+20 | 72.95 | 2536 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | intraday_target_watch | D+10 | 51.23 | 1.54 | D+20 | 63.22 | 30805 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | intraday_target_watch | D+10 | 42.74 | 1.52 | D+20 | 69.7 | 2615 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | intraday_target_watch | D+10 | 49.76 | 1.47 | D+20 | 64.11 | 47726 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 43.56 | 1.65 | D+20 | 72.31 | 12521 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1.2 | research_only | D+10 | 44.86 | 1.03 | D+20 | 56.13 | 89480 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1 | research_only | D+10 | 44.77 | 1.03 | D+20 | 56.09 | 77683 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-4_7_volmax1.5 | research_only | D+10 | 44.86 | 1.02 | D+20 | 56.01 | 100803 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near5_vol1.5 | research_only | D+10 | 42.94 | 0.94 | D+20 | 57.04 | 13756 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1 | research_only | D+10 | 44.53 | 0.93 | D+20 | 54.43 | 69135 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1.2 | research_only | D+10 | 44.57 | 0.92 | D+20 | 54.4 | 79244 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-2.5_5_volmax1.5 | research_only | D+10 | 44.55 | 0.91 | D+20 | 54.2 | 88731 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near3_vol1.5 | research_only | D+10 | 42.77 | 0.91 | D+20 | 56.34 | 8289 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near3_vol1.2 | research_only | D+10 | 43.0 | 0.86 | D+20 | 54.34 | 11391 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| near_high_neckline_challenge | near5_vol1.2 | research_only | D+10 | 43.12 | 0.85 | D+20 | 55.38 | 19330 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1 | research_only | D+10 | 44.43 | 0.82 | D+20 | 51.88 | 53892 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1.2 | research_only | D+10 | 44.43 | 0.8 | D+20 | 51.73 | 61229 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | ema-1.5_3_volmax1.5 | research_only | D+10 | 44.34 | 0.78 | D+20 | 51.45 | 67874 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.78 | 0.74 | D+20 | 63.62 | 8365 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.5 | research_only | D+10 | 42.7 | 0.44 | D+20 | 46.98 | 8090 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | solid_volume_red_k_vol1.2 | research_only | D+10 | 42.62 | 0.38 | D+20 | 47.96 | 16502 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.2 | research_only | D+10 | 42.53 | 0.38 | D+20 | 45.66 | 11746 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | volume_red_k_vol1.2 | research_only | D+10 | 42.42 | 0.38 | D+20 | 49.07 | 31433 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 42.51 | 0.34 | D+20 | 44.92 | 8902 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.5 | research_only | D+10 | 42.26 | 0.34 | D+20 | 46.41 | 6331 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| price_pullback_23ema | solid_volume_red_k_vol1.5 | research_only | D+10 | 42.07 | 0.24 | D+20 | 47.6 | 10622 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 41.78 | 0.21 | D+20 | 42.23 | 8365 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 41.64 | 0.21 | D+20 | 41.94 | 6033 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near5_vol1.5 | research_only | D+10 | 41.82 | 0.19 | D+20 | 43.55 | 5887 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
