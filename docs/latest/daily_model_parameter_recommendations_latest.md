# DAILY MODEL PARAMETER RECOMMENDATIONS

- generated_at: 2026-06-15 13:49:44 Asia/Taipei
- purpose: convert parameter backtests into program-side reporting recommendations
- entry_basis: signal date next trading day open
- close_return: D+n close divided by next open minus 1
- high_return: max intraday high through D+n divided by next open minus 1
- rule: recommendations affect reporting and model research priority only; do not silently change core weights

## Usage Summary

| recommended_usage | count |
| --- | --- |
| intraday_target_watch | 61 |
| research_only | 12 |
| pdf_secondary_watch | 5 |
| promote_to_pdf_core | 3 |
| score_component_only | 1 |

## Top Recommendations

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tdcc_short_term_continuation_d5_d10 | high_thresholds_ret5_10_30_ret10_20_50_kd | promote_to_pdf_core | D+10 | 69.18 | 9.26 | D+20 | 90.7 | 265 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| hot_theme_pullback | strict_mainstream_supported_ema-2.5_5_support8 | promote_to_pdf_core | D+7 | 75.0 | 5.28 | D+9 | 79.63 | 618 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| hot_theme_pullback | strict_mainstream_supported_ema-4_7_support10 | promote_to_pdf_core | D+7 | 72.88 | 5.01 | D+9 | 79.55 | 757 | D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。 |
| tdcc_short_term_continuation_d5_d10 | all_thresholds_up_ret5_10_30_macd | pdf_secondary_watch | D+10 | 57.65 | 6.98 | D+20 | 78.97 | 1397 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_short_term_continuation_d5_d10 | production_current_proxy | pdf_secondary_watch | D+10 | 52.59 | 5.03 | D+20 | 76.99 | 2313 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | tdcc_up2_range10 | pdf_secondary_watch | D+10 | 55.3 | 2.29 | D+10 | 44.86 | 16636 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | production_current_proxy | pdf_secondary_watch | D+10 | 53.17 | 2.23 | D+20 | 50.28 | 24273 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | tdcc_up1_range10 | pdf_secondary_watch | D+10 | 52.54 | 2.2 | D+20 | 51.43 | 27457 | 收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。 |
| tdcc_stealth_accumulation | tdcc_up3_range10 | score_component_only | D+8 | 51.56 | 1.14 | D+20 | 48.11 | 10144 | 單獨模型勝率不足，但平均報酬略正；可當 TDCC、營收、族群或權證共振的加分項。 |
| volume_range_breakout | locked_limit_up_breakout_no_volume_gate | intraday_target_watch | D+10 | 44.76 | 3.85 | D+20 | 70.85 | 657 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.5 | intraday_target_watch | D+10 | 48.97 | 2.69 | D+20 | 70.25 | 1519 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1.2 | intraday_target_watch | D+10 | 49.72 | 2.62 | D+20 | 69.64 | 2383 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol1000 | intraday_target_watch | D+10 | 44.72 | 2.41 | D+20 | 72.57 | 3090 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| pullback_short_reclaim | prior20up_reclaim_vol1 | intraday_target_watch | D+10 | 49.44 | 2.32 | D+20 | 69.18 | 3363 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | production_current | intraday_target_watch | D+10 | 44.82 | 2.24 | D+20 | 71.38 | 4349 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol1000 | intraday_target_watch | D+10 | 43.19 | 2.23 | D+20 | 70.69 | 2324 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol1000 | intraday_target_watch | D+10 | 44.67 | 2.19 | D+20 | 71.36 | 3819 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol2_minvol2000 | intraday_target_watch | D+10 | 44.04 | 2.16 | D+20 | 72.23 | 2504 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol2_minvol2000 | intraday_target_watch | D+10 | 44.43 | 2.13 | D+20 | 71.6 | 3055 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol1000 | intraday_target_watch | D+10 | 44.5 | 2.11 | D+20 | 69.72 | 4808 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol2_minvol2000 | intraday_target_watch | D+10 | 44.36 | 2.05 | D+20 | 69.9 | 3823 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol1000 | intraday_target_watch | D+10 | 43.03 | 2.03 | D+20 | 69.86 | 2772 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.01_vol3_minvol1000 | intraday_target_watch | D+10 | 42.98 | 1.98 | D+20 | 68.66 | 3342 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.03_vol3_minvol2000 | intraday_target_watch | D+10 | 42.21 | 1.93 | D+20 | 70.36 | 1842 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |
| volume_range_breakout | prior20x1.02_vol3_minvol2000 | intraday_target_watch | D+10 | 42.51 | 1.9 | D+20 | 70.13 | 2175 | 盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。 |

## Research Only / Not Yet Promoted

| model_id | parameter_set_id | recommended_usage | recommended_close_exit_horizon | best_close_win_rate_pct | best_avg_close_return_pct | recommended_high_exit_horizon | best_high_5pct_hit_rate_pct | selected_stock_days | model_revision_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| short_term_surge_d5_d10 | ret5_10_30_vol5_ge1_5_macd | research_only | D+10 | 44.75 | 1.91 | D+20 | 71.9 | 12550 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol3_solid_red | research_only | D+10 | 40.87 | 0.72 | D+20 | 63.07 | 7646 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| revenue_unreacted_range | production_current_proxy | research_only | D+10 | 43.82 | 0.53 | D+20 | 40.76 | 453519 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w20_near3_vol1.2 | research_only | D+10 | 41.64 | 0.3 | D+20 | 44.02 | 8754 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| revenue_unreacted_range | range23_tol5 | research_only | D+10 | 43.36 | 0.25 | D+20 | 36.41 | 331637 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| revenue_unreacted_range | range23_tol10 | research_only | D+10 | 43.33 | 0.25 | D+20 | 36.52 | 333285 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.2 | research_only | D+10 | 41.43 | 0.24 | D+20 | 41.83 | 8441 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.2 | research_only | D+10 | 41.4 | 0.24 | D+20 | 41.42 | 6053 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near5_vol1.5 | research_only | D+9 | 41.61 | 0.23 | D+20 | 43.26 | 5947 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| platform_strengthening | w30_near3_vol1.5 | research_only | D+9 | 41.47 | 0.22 | D+20 | 43.07 | 4359 | 目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。 |
| explosive_volume_red_candle | vol5_solid_red | research_only | D+10 | 39.59 | 0.14 | D+20 | 63.64 | 3190 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
| explosive_volume_red_candle | vol10_solid_red | research_only | D+8 | 38.32 | -0.57 | D+20 | 63.61 | 799 | 此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。 |
