# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-06-29 05:03:50 Asia/Taipei
- purpose: convert parameter backtests into program-side reporting recommendations
- entry_basis: signal date next trading day open
- close_return: D+n close divided by next open minus 1
- high_return: max intraday high through D+n divided by next open minus 1
- rule: recommendations affect reporting and model research priority only; do not silently change core weights

## Usage Summary

| recommended_usage | count |
| --- | --- |
| intraday_target_watch | 70 |
| research_only | 9 |
| pdf_secondary_watch | 4 |
| promote_to_pdf_core | 1 |

## Top Recommendations

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| w_bottom_right_side | w_bottom_early_entry_operation_v1 | promote_to_pdf_core | D+40 | 65.0000 | 2.9504 |  |  | 44 | Approved operation w_bottom_early_entry_operation_v1_20260629; pure win rate 65.0000 uses win/(win+loss). Inclusive success 77.4194 includes neutral rows and must not be labeled as pure win rate. buy_filter_id=smooth_core_mainstream_right_rebound_5_20_bull. |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | pdf_secondary_watch | D+9 | 63.75 | 3.11 | D+10 | 72.68 | 1109 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | pdf_secondary_watch | D+9 | 60.24 | 2.57 | D+10 | 70.69 | 1336 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | production_current_proxy | pdf_secondary_watch | D+10 | 53.78 | 2.1 | D+20 | 62.88 | 31187 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | pdf_secondary_watch | D+10 | 54.85 | 2.04 | D+20 | 61.62 | 22466 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | intraday_target_watch | D+10 | 50.76 | 4.17 | D+20 | 90.23 | 297 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | intraday_target_watch | D+10 | 47.85 | 3.24 | D+20 | 83.98 | 1722 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | intraday_target_watch | D+10 | 44.83 | 2.29 | D+20 | 81.38 | 2995 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 48.51 | 2.05 | D+20 | 69.12 | 2049 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 46.81 | 2.01 | D+20 | 69.85 | 1275 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | intraday_target_watch | D+4 | 57.78 | 1.94 | D+10 | 65.52 | 1676 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | intraday_target_watch | D+10 | 52.57 | 1.94 | D+20 | 63.5 | 35719 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 48.47 | 1.91 | D+20 | 69.11 | 2933 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | production_current_proxy | intraday_target_watch | D+10 | 46.18 | 1.89 | D+20 | 69.07 | 83552 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | intraday_target_watch | D+10 | 44.36 | 1.87 | D+20 | 73.7 | 3003 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | production_current_proxy | intraday_target_watch | D+4 | 57.57 | 1.79 | D+10 | 68.4 | 2785 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | intraday_target_watch | D+4 | 57.57 | 1.79 | D+10 | 68.4 | 2785 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | intraday_target_watch | D+10 | 43.14 | 1.79 | D+20 | 71.65 | 2232 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | intraday_target_watch | D+10 | 44.21 | 1.74 | D+20 | 70.87 | 4691 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | intraday_target_watch | D+10 | 44.17 | 1.74 | D+20 | 72.47 | 3721 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | intraday_target_watch | D+10 | 42.82 | 1.66 | D+20 | 69.72 | 3219 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | production_current | intraday_target_watch | D+10 | 44.17 | 1.65 | D+20 | 73.07 | 4240 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | intraday_target_watch | D+10 | 42.76 | 1.63 | D+20 | 70.94 | 2668 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | intraday_target_watch | D+4 | 55.86 | 1.61 | D+10 | 64.4 | 2233 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | intraday_target_watch | D+10 | 44.09 | 1.59 | D+20 | 71.11 | 3699 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 43.68 | 1.67 | D+20 | 72.93 | 11687 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.99 | 0.74 | D+20 | 63.87 | 7912 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 42.68 | 0.38 | D+20 | 44.81 | 8577 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 42.05 | 0.25 | D+20 | 42.22 | 8036 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 41.84 | 0.25 | D+20 | 41.87 | 5794 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.79 | 0.24 | D+20 | 64.53 | 3277 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near5_vol1.5 | research_only | D+10 | 42.07 | 0.23 | D+20 | 43.62 | 5657 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.5 | research_only | D+10 | 41.96 | 0.21 | D+20 | 43.42 | 4168 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol10_solid_red | research_only | D+8 | 39.69 | -0.22 | D+20 | 64.97 | 812 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
