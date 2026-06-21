# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-06-21 21:06:50 Asia/Taipei
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
| pdf_secondary_watch | 2 |
| score_component_only | 1 |

## Top Recommendations

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | pdf_secondary_watch | D+9 | 63.75 | 3.11 | D+10 | 71.05 | 1074 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | pdf_secondary_watch | D+9 | 60.24 | 2.57 | D+10 | 68.52 | 1295 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | tdcc_up3_range10 | score_component_only | D+8 | 51.87 | 1.08 | D+20 | 49.93 | 13614 | 單獨模型勝率不足，但平均報酬略正；可當 TDCC、營收、族群或權證共振的加分項。 |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | intraday_target_watch | D+10 | 49.61 | 3.7 | D+20 | 92.59 | 289 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | intraday_target_watch | D+10 | 46.57 | 3.0 | D+20 | 86.03 | 1586 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 48.29 | 2.05 | D+20 | 69.14 | 2014 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 46.8 | 2.02 | D+20 | 69.93 | 1252 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | intraday_target_watch | D+10 | 43.43 | 1.98 | D+20 | 82.89 | 2715 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | strict_mainstream_overheated_ema-2.5_5_support8 | intraday_target_watch | D+2 | 61.56 | 1.93 | D+9 | 64.42 | 1261 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | production_current_proxy | intraday_target_watch | D+10 | 52.81 | 1.91 | D+20 | 62.05 | 29748 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 48.31 | 1.91 | D+20 | 69.18 | 2886 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | intraday_target_watch | D+10 | 44.23 | 1.88 | D+20 | 73.69 | 2965 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | intraday_target_watch | D+10 | 53.92 | 1.82 | D+20 | 60.38 | 21191 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | production_current_proxy | intraday_target_watch | D+10 | 45.82 | 1.78 | D+20 | 68.93 | 82199 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | intraday_target_watch | D+10 | 42.91 | 1.78 | D+20 | 71.57 | 2212 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | intraday_target_watch | D+10 | 51.63 | 1.76 | D+20 | 62.74 | 33826 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | intraday_target_watch | D+10 | 44.1 | 1.74 | D+20 | 70.79 | 4635 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | intraday_target_watch | D+10 | 44.04 | 1.74 | D+20 | 72.43 | 3675 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | strict_mainstream_overheated_ema-4_7_support10 | intraday_target_watch | D+2 | 59.06 | 1.73 | D+9 | 63.45 | 1688 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | production_current_proxy | intraday_target_watch | D+5 | 57.78 | 1.67 | D+9 | 67.08 | 2335 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | intraday_target_watch | D+5 | 57.78 | 1.67 | D+9 | 67.08 | 2335 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | intraday_target_watch | D+10 | 42.73 | 1.66 | D+20 | 69.62 | 3187 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | production_current | intraday_target_watch | D+10 | 44.05 | 1.64 | D+20 | 73.03 | 4180 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | intraday_target_watch | D+10 | 42.58 | 1.63 | D+20 | 70.85 | 2644 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | intraday_target_watch | D+10 | 43.98 | 1.58 | D+20 | 71.01 | 3659 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 43.53 | 1.65 | D+20 | 72.87 | 11466 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.85 | 0.71 | D+20 | 63.89 | 7768 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 42.5 | 0.37 | D+20 | 44.62 | 8518 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 41.9 | 0.25 | D+20 | 41.99 | 7980 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 41.77 | 0.25 | D+20 | 41.59 | 5760 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.5 | research_only | D+10 | 41.95 | 0.24 | D+20 | 43.4 | 5615 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.71 | 0.23 | D+20 | 64.65 | 3224 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w30_near3_vol1.5 | research_only | D+10 | 41.92 | 0.22 | D+20 | 43.16 | 4141 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol10_solid_red | research_only | D+8 | 39.79 | -0.22 | D+20 | 64.9 | 802 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
