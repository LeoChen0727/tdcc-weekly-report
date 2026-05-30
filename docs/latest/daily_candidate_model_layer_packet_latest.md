# DAILY CANDIDATE MODEL LAYER PACKET

- generated_at: `2026-05-30 15:06:57 Asia/Taipei`
- signal_date: `20260529`
- contract: model main condition met means the stock enters that model candidate list.
- scoring: risk, TDCC, warrant, revenue, position, and structure adjust rank inside the model; mainstream/non-mainstream only splits reports.
- PDF rule: do not hard-code model count; render models from `daily_candidate_model_signals_latest.csv` and parameters from `daily_candidate_model_parameters_latest.md`.

## Model Parameters

| model_id                            | model_name_zh              | pdf_visibility             | entry_basis              | main_conditions                                                                                |
|:------------------------------------|:---------------------------|:---------------------------|:-------------------------|:-----------------------------------------------------------------------------------------------|
| volume_range_breakout               | 帶量突破模型               | pdf_core_model             | signal_date_next_open    | 量比 >= 1.5 且突破盤整區間/平台/頸線/波段高點。                                                |
| price_pullback_23ema                | 股價回檔模型               | pdf_core_model             | signal_date_next_open    | 股價回到23EMA或平台附近，且23EMA斜率代理為正。                                                 |
| revenue_unreacted_range             | 營收爆發但股價尚未反應模型 | pdf_core_model             | signal_date_next_open    | 營收YoY或累計YoY強，且股價仍在近20/23日區間上下5%內。                                          |
| w_bottom_right_side                 | W底右側模型                | pdf_core_model             | signal_date_next_open    | W底成立且右側低點墊高。                                                                        |
| near_high_neckline_challenge        | 接近前高/頸線挑戰模型      | pdf_core_model             | signal_date_next_open    | 距前高/頸線0%到5%，量能開始放大，均線轉正。                                                    |
| platform_strengthening              | 平台整理轉強模型           | pdf_core_model             | signal_date_next_open    | 盤整區間形成、波動收斂、接近上緣、量能回升且出現帶量實體紅K。                                  |
| pullback_short_reclaim              | 回檔後短線轉強模型         | pdf_core_model             | signal_date_next_open    | 前面有漲勢，回檔未破結構，重新站回23EMA或短均結構轉強。                                        |
| tdcc_stealth_accumulation           | TDCC潛伏吸籌模型           | pdf_core_model             | signal_date_next_open    | TDCC連續或溫和增加，股價尚未大漲，且股價仍在近20/23日區間上下10%內；優先tdcc_leading_price。   |
| tdcc_short_term_continuation_d5_d10 | TDCC短線延續模型 D+5/D+10  | pdf_specialty_section      | signal_date_next_open    | all_thresholds_overheated或phase_overheated_after_tdcc，搭配MACD/KD/Bollinger與1W/2W漲幅條件。 |
| short_term_surge_d5_d10             | 短線急漲D+5/D+10模型       | pdf_specialty_section      | signal_date_next_open    | 5日或10日漲幅達標、量能擴張、技術動能強。                                                      |
| group_fund_rotation                 | 族群資金輪動模型           | pdf_end_section_theme_only | not_stock_entry_signal   | 有族群標籤，且同族群超過1/3股票量比>=3。                                                       |
| explosive_volume_red_candle         | 爆天量紅K模型              | research_only_not_pdf_core | signal_date_next_open    | 月均量3倍/5倍/10倍、實體紅K、上影線小、收盤接近日高，另分低位爆量。                            |
| five_day_20pct_precursor            | 一週內上漲20%前兆模型      | research_only_not_pdf_core | signal_date_next_open    | 歷史5日內高低點漲幅>=20%的樣本反推前一天與第一天條件。                                         |
| disposition_attention_event_tag     | 處置/注意股事件標籤        | pdf_risk_tag_only          | tag_only                 | 處置、注意、分盤等交易事件。                                                                   |
| msci_event_tag                      | MSCI事件標籤               | pdf_event_tag_only         | effective_date_next_open | MSCI新增或剔除。                                                                               |

## Signal Counts

| model_id                            | model_name_zh              | report_bucket   |   count |
|:------------------------------------|:---------------------------|:----------------|--------:|
| near_high_neckline_challenge        | 接近前高/頸線挑戰模型      | mainstream      |      26 |
| near_high_neckline_challenge        | 接近前高/頸線挑戰模型      | non_mainstream  |      38 |
| platform_strengthening              | 平台整理轉強模型           | mainstream      |      10 |
| platform_strengthening              | 平台整理轉強模型           | non_mainstream  |      26 |
| price_pullback_23ema                | 股價回檔模型               | mainstream      |     226 |
| price_pullback_23ema                | 股價回檔模型               | non_mainstream  |     178 |
| pullback_short_reclaim              | 回檔後短線轉強模型         | mainstream      |      46 |
| pullback_short_reclaim              | 回檔後短線轉強模型         | non_mainstream  |      28 |
| revenue_unreacted_range             | 營收爆發但股價尚未反應模型 | mainstream      |     145 |
| revenue_unreacted_range             | 營收爆發但股價尚未反應模型 | non_mainstream  |     133 |
| short_term_surge_d5_d10             | 短線急漲D+5/D+10模型       | unclassified    |      96 |
| tdcc_short_term_continuation_d5_d10 | TDCC短線延續模型 D+5/D+10  | unclassified    |      75 |
| tdcc_stealth_accumulation           | TDCC潛伏吸籌模型           | mainstream      |     116 |
| tdcc_stealth_accumulation           | TDCC潛伏吸籌模型           | non_mainstream  |     111 |
| volume_range_breakout               | 帶量突破模型               | mainstream      |      64 |
| volume_range_breakout               | 帶量突破模型               | non_mainstream  |      62 |
| w_bottom_right_side                 | W底右側模型                | mainstream      |      72 |
| w_bottom_right_side                 | W底右側模型                | non_mainstream  |      36 |

## Group Rotation

|   signal_date | theme    |   stock_count |   volume_expansion_3x_count |   volume_expansion_ratio | leader_1   | leader_2   | leader_3   | interpretation                       |
|--------------:|:---------|--------------:|----------------------------:|-------------------------:|:-----------|:-----------|:-----------|:-------------------------------------|
|      20260529 | 汽車工業 |            28 |                          12 |                   0.4286 | 1568 倉佑  | 1524 耿鼎  | 1563 巧新  | 族群資金輪動觀察；不是個股買進模型。 |
