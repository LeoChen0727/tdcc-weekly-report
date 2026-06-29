# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-06-29 08:37:45 Asia/Taipei
- purpose: convert parameter backtests into program-side reporting recommendations
- entry_basis: signal date next trading day open
- close_return: D+n close divided by next open minus 1
- high_return: max intraday high through D+n divided by next open minus 1
- rule: recommendations affect reporting and model research priority only; do not silently change core weights

## Usage Summary

| recommended_usage | count |
| --- | --- |
| intraday_target_watch | 72 |
| research_only | 9 |
| promote_to_pdf_core | 2 |
| pdf_secondary_watch | 2 |

## Top Recommendations

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| neckline_volume_breakout_confirmation | neckline_strict_45_signal_90_score_v1 | promote_to_pdf_core | D+20 | 63.8889 | 4.3784 |  |  | 51 | Approved operation neckline_strict_45_signal_90_score_v1_20260629; pure win rate 63.8889 uses win/(win+loss). Inclusive success 74.5098 includes neutral rows and must not be labeled as pure win rate. buy_filter_id=broad_45_non_bearish_with_90_warning; 90d bearish context remains eligible as score/risk adjustment. |
| w_bottom_right_side | w_bottom_early_entry_operation_v1 | promote_to_pdf_core | D+40 | 65.0000 | 2.9504 |  |  | 44 | Approved operation w_bottom_early_entry_operation_v1_20260629; pure win rate 65.0000 uses win/(win+loss). Inclusive success 77.4194 includes neutral rows and must not be labeled as pure win rate. buy_filter_id=smooth_core_mainstream_right_rebound_5_20_bull. |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | pdf_secondary_watch | D+10 | 59.08 | 2.09 | D+20 | 88.5 | 1150 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | production_current_proxy | pdf_secondary_watch | D+10 | 52.88 | 2.0 | D+20 | 64.09 | 33728 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | intraday_target_watch | D+10 | 51.84 | 4.53 | D+20 | 87.5 | 325 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | intraday_target_watch | D+10 | 47.96 | 3.24 | D+20 | 82.72 | 1867 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | intraday_target_watch | D+10 | 45.2 | 2.43 | D+20 | 79.04 | 3260 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 48.0 | 1.96 | D+20 | 69.52 | 2090 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 46.43 | 1.95 | D+20 | 70.06 | 1303 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | intraday_target_watch | D+10 | 53.69 | 1.94 | D+20 | 63.1 | 24411 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | production_current_proxy | intraday_target_watch | D+10 | 46.17 | 1.91 | D+20 | 69.19 | 85294 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | intraday_target_watch | D+10 | 44.28 | 1.88 | D+20 | 73.78 | 3043 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 48.05 | 1.86 | D+20 | 69.51 | 2996 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | intraday_target_watch | D+10 | 51.78 | 1.85 | D+20 | 64.53 | 38642 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | intraday_target_watch | D+10 | 43.09 | 1.8 | D+20 | 71.75 | 2265 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | intraday_target_watch | D+10 | 44.14 | 1.72 | D+20 | 70.84 | 4744 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | intraday_target_watch | D+10 | 44.09 | 1.72 | D+20 | 72.41 | 3765 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | intraday_target_watch | D+10 | 42.85 | 1.67 | D+20 | 69.79 | 3261 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | production_current | intraday_target_watch | D+10 | 44.13 | 1.65 | D+20 | 73.07 | 4288 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | intraday_target_watch | D+10 | 42.74 | 1.63 | D+20 | 70.99 | 2703 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | intraday_target_watch | D+10 | 56.33 | 1.58 | D+20 | 88.56 | 1383 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | intraday_target_watch | D+10 | 44.03 | 1.58 | D+20 | 71.09 | 3740 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | intraday_target_watch | D+10 | 43.74 | 1.54 | D+20 | 72.79 | 2984 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | intraday_target_watch | D+6 | 53.21 | 1.53 | D+20 | 76.73 | 2126 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | intraday_target_watch | D+10 | 42.73 | 1.51 | D+20 | 69.93 | 2516 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 43.76 | 1.74 | D+20 | 73.0 | 11973 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.9 | 0.73 | D+20 | 63.85 | 8033 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 42.62 | 0.36 | D+20 | 44.87 | 8630 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.67 | 0.24 | D+20 | 64.32 | 3341 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 41.92 | 0.23 | D+20 | 42.23 | 8089 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 41.74 | 0.23 | D+20 | 41.91 | 5834 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.5 | research_only | D+10 | 41.97 | 0.22 | D+20 | 43.58 | 5686 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.5 | research_only | D+10 | 41.91 | 0.2 | D+20 | 43.38 | 4193 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol10_solid_red | research_only | D+8 | 39.72 | -0.16 | D+20 | 64.57 | 830 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
