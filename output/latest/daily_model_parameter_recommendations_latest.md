# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-06-12 10:49:43 Asia/Taipei
- purpose: convert parameter backtests into program-side reporting recommendations
- entry_basis: signal date next trading day open
- close_return: D+n close divided by next open minus 1
- high_return: max intraday high through D+n divided by next open minus 1
- rule: recommendations affect reporting and model research priority only; do not silently change core weights

## Usage Summary

| recommended_usage | count |
| --- | --- |
| intraday_target_watch | 50 |
| research_only | 12 |
| promote_to_pdf_core | 4 |
| pdf_secondary_watch | 4 |
| score_component_only | 1 |

## Top Recommendations

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | promote_to_pdf_core | D+10 | 72.18 | 10.92 | D+20 | 93.94 | 255 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | promote_to_pdf_core | D+10 | 60.37 | 8.44 | D+20 | 74.89 | 1361 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | promote_to_pdf_core | D+7 | 75.0 | 5.28 | D+8 | 79.63 | 550 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | promote_to_pdf_core | D+6 | 80.93 | 5.21 | D+8 | 78.79 | 677 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| hot_theme_pullback | strict_mainstream_any_ema-2.5_5_support8 | pdf_secondary_watch | D+6 | 62.16 | 2.61 | D+8 | 73.43 | 1354 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | pdf_secondary_watch | D+10 | 55.08 | 2.31 | D+10 | 44.08 | 15906 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | pdf_secondary_watch | D+10 | 52.25 | 2.23 | D+20 | 49.08 | 26468 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| hot_theme_pullback | strict_mainstream_any_ema-4_7_support10 | pdf_secondary_watch | D+6 | 59.07 | 2.18 | D+8 | 73.64 | 1763 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | tdcc_up3_range10 | score_component_only | D+7 | 51.4 | 1.06 | D+20 | 47.82 | 9596 | 單獨模型勝率不足，但平均報酬略正；可當 TDCC、營收、族群或權證共振的加分項。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 49.04 | 2.71 | D+20 | 70.13 | 1514 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 49.78 | 2.64 | D+20 | 69.54 | 2375 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | intraday_target_watch | D+10 | 44.8 | 2.45 | D+20 | 72.39 | 3076 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 49.42 | 2.33 | D+20 | 69.09 | 3355 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | intraday_target_watch | D+10 | 43.3 | 2.26 | D+20 | 70.57 | 2313 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | intraday_target_watch | D+10 | 44.81 | 2.24 | D+20 | 71.15 | 3805 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | intraday_target_watch | D+10 | 44.12 | 2.19 | D+20 | 72.08 | 2496 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | intraday_target_watch | D+10 | 44.56 | 2.18 | D+20 | 71.42 | 3047 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | intraday_target_watch | D+10 | 44.64 | 2.15 | D+20 | 69.51 | 4792 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | intraday_target_watch | D+10 | 44.5 | 2.09 | D+20 | 69.7 | 3813 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | intraday_target_watch | D+10 | 43.17 | 2.06 | D+20 | 69.73 | 2761 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | intraday_target_watch | D+10 | 43.1 | 2.01 | D+20 | 68.52 | 3329 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | intraday_target_watch | D+10 | 42.34 | 1.96 | D+20 | 70.25 | 1836 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol500 | intraday_target_watch | D+10 | 43.81 | 1.95 | D+20 | 71.81 | 3701 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | intraday_target_watch | D+10 | 42.66 | 1.93 | D+20 | 70.03 | 2169 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol2000 | intraday_target_watch | D+10 | 42.76 | 1.91 | D+20 | 68.64 | 2599 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 44.81 | 1.93 | D+20 | 71.75 | 12515 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.92 | 0.73 | D+20 | 62.96 | 7635 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| platform_strengthening | w20_near5_vol1.2 | research_only | D+10 | 41.67 | 0.33 | D+20 | 44.91 | 11530 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 41.6 | 0.3 | D+20 | 43.93 | 8722 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| revenue_unreacted_range | range23_tol5 | research_only | D+10 | 43.28 | 0.24 | D+20 | 36.33 | 330819 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| revenue_unreacted_range | range23_tol10 | research_only | D+10 | 43.26 | 0.24 | D+20 | 36.43 | 332438 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 41.45 | 0.24 | D+20 | 41.74 | 8410 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 41.43 | 0.24 | D+20 | 41.33 | 6026 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.5 | research_only | D+10 | 41.31 | 0.23 | D+20 | 43.14 | 5927 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.5 | research_only | D+8 | 41.16 | 0.21 | D+20 | 42.96 | 4341 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.69 | 0.17 | D+20 | 63.55 | 3187 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol10_solid_red | research_only | D+8 | 38.39 | -0.52 | D+20 | 63.6 | 799 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
