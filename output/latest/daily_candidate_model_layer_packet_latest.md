# DAILY CANDIDATE MODEL LAYER PACKET

- generated_at: `2026-05-30 20:40:50 Asia/Taipei`
- signal_date: `20260529`
- contract: model main condition met means the stock enters that model candidate list.
- scoring: risk, TDCC, warrant, revenue, position, and structure adjust rank inside the model; mainstream/non-mainstream only splits reports.
- PDF rule: do not hard-code model count; render models from `daily_candidate_model_signals_latest.csv` and parameters from `daily_candidate_model_parameters_latest.md`.

## Model Parameters

| model_id                            | model_name_zh              | pdf_visibility             | entry_basis              | recommended_usage     | recommended_close_exit_horizon   |   best_close_win_rate_pct |   best_avg_close_return_pct | main_conditions                                                                                |
|:------------------------------------|:---------------------------|:---------------------------|:-------------------------|:----------------------|:---------------------------------|--------------------------:|----------------------------:|:-----------------------------------------------------------------------------------------------|
| volume_range_breakout               | 帶量突破模型               | pdf_core_model             | signal_date_next_open    | intraday_target_watch | D+10                             |                     41.42 |                        0.68 | 量比 >= 1.5 且突破盤整區間/平台/頸線/波段高點。                                                |
| price_pullback_23ema                | 股價回檔模型               | pdf_core_model             | signal_date_next_open    | intraday_target_watch | D+10                             |                     43.65 |                        0.81 | 股價回到23EMA或平台附近，且23EMA斜率代理為正。                                                 |
| revenue_unreacted_range             | 營收爆發但股價尚未反應模型 | pdf_core_model             | signal_date_next_open    |                       |                                  |                           |                             | 營收YoY或累計YoY強，且股價仍在近20/23日區間上下5%內。                                          |
| w_bottom_right_side                 | W底右側模型                | pdf_core_model             | signal_date_next_open    | intraday_target_watch | D+10                             |                     43.44 |                        1    | W底成立且右側低點墊高。                                                                        |
| near_high_neckline_challenge        | 接近前高/頸線挑戰模型      | pdf_core_model             | signal_date_next_open    | intraday_target_watch | D+10                             |                     42.03 |                        0.74 | 距前高/頸線0%到5%，量能開始放大，均線轉正。                                                    |
| platform_strengthening              | 平台整理轉強模型           | pdf_core_model             | signal_date_next_open    | intraday_target_watch | D+10                             |                     41.31 |                        0.32 | 盤整區間形成、波動收斂、接近上緣、量能回升且出現帶量實體紅K。                                  |
| pullback_short_reclaim              | 回檔後短線轉強模型         | pdf_core_model             | signal_date_next_open    | intraday_target_watch | D+10                             |                     48.96 |                        2.69 | 前面有漲勢，回檔未破結構，重新站回23EMA或短均結構轉強。                                        |
| tdcc_stealth_accumulation           | TDCC潛伏吸籌模型           | pdf_core_model             | signal_date_next_open    | score_component_only  | D+7                              |                     48.17 |                        1.09 | TDCC連續或溫和增加，股價尚未大漲，且股價仍在近20/23日區間上下10%內；優先tdcc_leading_price。   |
| tdcc_short_term_continuation_d5_d10 | TDCC短線延續模型 D+5/D+10  | pdf_specialty_section      | signal_date_next_open    | promote_to_pdf_core   | D+10                             |                     76.71 |                       15.56 | all_thresholds_overheated或phase_overheated_after_tdcc，搭配MACD/KD/Bollinger與1W/2W漲幅條件。 |
| short_term_surge_d5_d10             | 短線急漲D+5/D+10模型       | pdf_specialty_section      | signal_date_next_open    | intraday_target_watch | D+10                             |                     44.18 |                        1.76 | 5日或10日漲幅達標、量能擴張、技術動能強。                                                      |
| group_fund_rotation                 | 族群資金輪動模型           | pdf_end_section_theme_only | not_stock_entry_signal   |                       |                                  |                           |                             | 有族群標籤，且同族群超過1/3股票量比>=3。                                                       |
| explosive_volume_red_candle         | 爆天量紅K模型              | research_only_not_pdf_core | signal_date_next_open    | research_only         | D+10                             |                     40.35 |                        0.6  | 月均量3倍/5倍/10倍、實體紅K、上影線小、收盤接近日高，另分低位爆量。                            |
| five_day_20pct_precursor            | 一週內上漲20%前兆模型      | research_only_not_pdf_core | signal_date_next_open    |                       |                                  |                           |                             | 歷史5日內高低點漲幅>=20%的樣本反推前一天與第一天條件。                                         |
| disposition_attention_event_tag     | 處置/注意股事件標籤        | pdf_risk_tag_only          | tag_only                 |                       |                                  |                           |                             | 處置、注意、分盤等交易事件。                                                                   |
| msci_event_tag                      | MSCI事件標籤               | pdf_event_tag_only         | effective_date_next_open |                       |                                  |                           |                             | MSCI新增或剔除。                                                                               |

## Signal Counts

| model_id                            | model_name_zh              | report_bucket   |   count |
|:------------------------------------|:---------------------------|:----------------|--------:|
| near_high_neckline_challenge        | 接近前高/頸線挑戰模型      | mainstream      |       1 |
| near_high_neckline_challenge        | 接近前高/頸線挑戰模型      | non_mainstream  |      24 |
| near_high_neckline_challenge        | 接近前高/頸線挑戰模型      | unclassified    |      39 |
| platform_strengthening              | 平台整理轉強模型           | mainstream      |       1 |
| platform_strengthening              | 平台整理轉強模型           | non_mainstream  |      21 |
| platform_strengthening              | 平台整理轉強模型           | unclassified    |      14 |
| price_pullback_23ema                | 股價回檔模型               | mainstream      |      10 |
| price_pullback_23ema                | 股價回檔模型               | non_mainstream  |     126 |
| price_pullback_23ema                | 股價回檔模型               | unclassified    |     268 |
| pullback_short_reclaim              | 回檔後短線轉強模型         | mainstream      |       1 |
| pullback_short_reclaim              | 回檔後短線轉強模型         | non_mainstream  |      17 |
| pullback_short_reclaim              | 回檔後短線轉強模型         | unclassified    |      56 |
| revenue_unreacted_range             | 營收爆發但股價尚未反應模型 | mainstream      |       9 |
| revenue_unreacted_range             | 營收爆發但股價尚未反應模型 | non_mainstream  |      99 |
| revenue_unreacted_range             | 營收爆發但股價尚未反應模型 | unclassified    |     170 |
| short_term_surge_d5_d10             | 短線急漲D+5/D+10模型       | unclassified    |      90 |
| tdcc_short_term_continuation_d5_d10 | TDCC短線延續模型 D+5/D+10  | unclassified    |     100 |
| tdcc_stealth_accumulation           | TDCC潛伏吸籌模型           | mainstream      |       7 |
| tdcc_stealth_accumulation           | TDCC潛伏吸籌模型           | non_mainstream  |      87 |
| tdcc_stealth_accumulation           | TDCC潛伏吸籌模型           | unclassified    |     133 |
| volume_range_breakout               | 帶量突破模型               | mainstream      |       3 |
| volume_range_breakout               | 帶量突破模型               | non_mainstream  |      37 |
| volume_range_breakout               | 帶量突破模型               | unclassified    |      86 |
| w_bottom_right_side                 | W底右側模型                | mainstream      |       5 |
| w_bottom_right_side                 | W底右側模型                | non_mainstream  |      18 |
| w_bottom_right_side                 | W底右側模型                | unclassified    |      85 |

## Group Rotation

|   signal_date | theme    |   stock_count |   volume_expansion_3x_count |   volume_expansion_ratio | leader_1   | leader_2   | leader_3   | interpretation                       |
|--------------:|:---------|--------------:|----------------------------:|-------------------------:|:-----------|:-----------|:-----------|:-------------------------------------|
|      20260529 | 汽車工業 |            29 |                          12 |                   0.4138 | 1568 倉佑  | 1524 耿鼎  | 1563 巧新  | 族群資金輪動觀察；不是個股買進模型。 |
