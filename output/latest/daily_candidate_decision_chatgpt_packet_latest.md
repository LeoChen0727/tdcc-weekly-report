# DAILY CANDIDATE DECISION CHATGPT PACKET

## Metadata
- generated_at: 2026-05-31 09:56:55 Asia/Taipei
- signal_date: 20260530
- source_file: output/latest/all_candidates_latest.csv
- decision_csv: output/latest/daily_candidate_decision_latest.csv

## Interpretation Rules
- This packet is the program-side decision layer. Prefer it over conversation memory.
- Category scores remain category-local; do not compare them as one universal model score.
- `decision_priority` is a reporting and tracking priority, not a buy/sell instruction.
- Risk handling is split into hard_exclusion, high_momentum_risk_follow, risk_watch, and normal. Mainstream/non-mainstream is a display section, not a score cap.
- TDCC distribution, continued overheat, and short-term overheat are rank and risk modifiers. If momentum remains strong, keep it in high_momentum_risk_follow and verify with D+5/D+10 evidence.
- Mainstream and non-mainstream candidates must be shown in separate sections and compared within their own section_rank; do not use theme group alone to downgrade score or veto selection.
- For 2484 regression: 20260520-20260521 platform_right_side, 20260522 neckline_breakout, 20260525 breakout_confirmed.
- For 8069 regression: 20260507 early right-side watch, 20260508 neckline_challenge, 20260512 strict volume-confirmed breakout.

## Priority Summary

| decision_priority   | decision_priority_label   |   count |
|:--------------------|:--------------------------|--------:|
| A_priority_watch    | 最優先追蹤                |      22 |
| B_confirm_needed    | 可等確認                  |     197 |
| C_watch_only        | 僅觀察                    |     462 |

## A Priority Watch

|   stock_id | stock_name   | original_category_cn      | pattern_stage       | decision_priority_label   |   decision_score | tdcc_status         | repeat_appear_label      | risk_handling_bucket   | downgrade_flags   | next_confirmation                           |
|-----------:|:-------------|:--------------------------|:--------------------|:--------------------------|-----------------:|:--------------------|:-------------------------|:-----------------------|:------------------|:--------------------------------------------|
|       1101 | 台泥         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             88.8 | strong_accumulation | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       1612 | 宏泰         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             88.8 | strong_accumulation | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2362 | 藍天         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             88.8 | strong_accumulation | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2618 | 長榮航       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             88.8 | strong_accumulation | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       1434 | 福懋         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       1471 | 首利         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       1608 | 華榮         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       1718 | 中纖         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2331 | 精英         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2332 | 友訊         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2376 | 技嘉         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | strong_accumulation | repeated_but_no_breakout | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2597 | 潤弘         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2601 | 益航         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2610 | 華航         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2881 | 富邦金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | strong_accumulation | repeated_but_no_breakout | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       2883 | 凱基金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | strong_accumulation | repeated_but_no_breakout | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       3046 | 建碁         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       3058 | 立德         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       5522 | 遠雄         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       6235 | 華孚         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | mild_accumulation   | continued_2_3d           | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       8070 | 長華*        | 區間內轉強 / 挑戰前高觀察 | neckline_challenge  | 最優先追蹤                |             84.8 | strong_accumulation | repeated_but_no_breakout | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |
|       3321 | 同泰         | 區間內轉強 / 挑戰前高觀察 | platform_right_side | 最優先追蹤                |             82.8 | strong_accumulation | repeated_but_no_breakout | normal                 |                   | 確認放量站上頸線/平台壓力，且收盤靠近高點。 |

## B Confirm Needed

|   stock_id | stock_name   | original_category_cn      | pattern_stage      | decision_priority_label   |   decision_score | tdcc_status         | repeat_appear_label      | risk_handling_bucket   | downgrade_flags             | next_confirmation                                              |
|-----------:|:-------------|:--------------------------|:-------------------|:--------------------------|-----------------:|:--------------------|:-------------------------|:-----------------------|:----------------------------|:---------------------------------------------------------------|
|       2031 | 新光鋼       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             81.8 | mild_accumulation   | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2201 | 裕隆         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             81.8 | mild_accumulation   | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2204 | 中華         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             81.8 | mild_accumulation   | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2352 | 佳世達       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             81.8 | strong_accumulation | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2731 | 雄獅         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             81.8 | mild_accumulation   | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       7711 | 永擎         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             81.8 | mild_accumulation   | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2603 | 長榮         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             81   | strong_accumulation | continued_2_3d           | normal                 | missing_attack_confirmation | 等待嚴格突破、放量站上重要均線、權證資金偏多，或財報品質確認。 |
|       1536 | 和大         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | stale_signal             | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       1605 | 華新         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       1618 | 合機         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | neutral             | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2374 | 佳能         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2382 | 廣達         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | stale_signal             | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2405 | 輔信         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2412 | 中華電       | 區間內轉強 / 挑戰前高觀察 |                    | 可等確認                  |             80.8 | mild_accumulation   | continued_2_3d           | normal                 |                             | 等待量價、TDCC、相對強弱至少一項轉強。                         |
|       2419 | 仲琦         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2882 | 國泰金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2885 | 元大金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2886 | 兆豐金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2891 | 中信金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       5876 | 上海商銀     | 區間內轉強 / 挑戰前高觀察 |                    | 可等確認                  |             80.8 | mild_accumulation   | continued_2_3d           | normal                 |                             | 等待量價、TDCC、相對強弱至少一項轉強。                         |
|       6224 | 聚鼎         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       8039 | 台虹         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       1449 | 佳和         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             80.4 | mild_accumulation   | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       3229 | 晟鈦         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             79.6 | mild_accumulation   | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2491 | 吉祥全       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             79   | mild_accumulation   | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       6672 | 騰輝電子-KY  | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             79   | mild_accumulation   | continued_2_3d           | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       1808 | 潤隆         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             77.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2328 | 廣宇         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             77.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2365 | 昆盈         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             77.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2645 | 長榮航太     | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             77.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       2646 | 星宇航空     | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             77.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       3022 | 威強電       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             77.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       3406 | 玉晶光       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             77.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       4306 | 炎洲         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             77.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |
|       6214 | 精誠         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 可等確認                  |             77.8 | mild_accumulation   | repeated_but_no_breakout | normal                 |                             | 確認放量站上頸線/平台壓力，且收盤靠近高點。                    |

## C Watch Only

|   stock_id | stock_name   | original_category_cn      | pattern_stage      | decision_priority_label   |   decision_score | tdcc_status          | repeat_appear_label      | risk_handling_bucket      | downgrade_flags           | next_confirmation                                              |
|-----------:|:-------------|:--------------------------|:-------------------|:--------------------------|-----------------:|:---------------------|:-------------------------|:--------------------------|:--------------------------|:---------------------------------------------------------------|
|       1447 | 力鵬         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             64.8 | mild_accumulation    | repeated_but_no_breakout | high_momentum_risk_follow | price_reaction_priced_in  | ??????????????????????????????????? D+5/D+10 ???               |
|       1301 | 台塑         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       1326 | 台化         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       1616 | 億泰         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       2207 | 和泰車       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       6591 | 動力-KY      | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       8033 | 雷虎         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       6197 | 佳必琪       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             59.6 | mild_accumulation    | repeated_but_no_breakout | high_momentum_risk_follow | price_reaction_priced_in  | ??????????????????????????????????? D+5/D+10 ???               |
|       1789 | 神隆         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             57.8 | distribution_warning | continued_2_3d           | risk_watch                | tdcc_distribution_warning | 先看 TDCC 是否停止轉弱，再看價格能否守住 MA20/EMA23 與突破區。 |
|       2634 | 漢翔         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             57   | distribution_warning | continued_2_3d           | risk_watch                | tdcc_distribution_warning | 先看 TDCC 是否停止轉弱，再看價格能否守住 MA20/EMA23 與突破區。 |
|       1303 | 南亞         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       1312 | 國喬         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       1440 | 南紡         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       1444 | 力麗         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       1504 | 東元         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       1609 | 大亞         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       2006 | 東和鋼鐵     | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       2243 | 宏旭-KY      | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       2330 | 台積電       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       2501 | 國建         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       2834 | 臺企銀       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       2838 | 聯邦銀       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       2890 | 永豐金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       3380 | 明泰         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       3706 | 神達         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       4566 | 時碩工業     | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       4915 | 致伸         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       4938 | 和碩         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       5880 | 合庫金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       6176 | 瑞儀         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       6531 | 愛普*        | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       6698 | 旭暉應材     | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       6805 | 富世達       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       8103 | 瀚荃         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |
|       8131 | 福懋科       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ???               |

## D Risk Downgrade

_No rows._

## High Momentum Risk Follow

Not a front-line buy list. Keep these rows visible for short-term D+5/D+10 validation instead of deleting them as generic overheat risk.

|   stock_id | stock_name   | original_category_cn      | pattern_stage      | decision_priority_label   |   decision_score | tdcc_status          | repeat_appear_label      | risk_handling_bucket      | downgrade_flags           | next_confirmation                                |
|-----------:|:-------------|:--------------------------|:-------------------|:--------------------------|-----------------:|:---------------------|:-------------------------|:--------------------------|:--------------------------|:-------------------------------------------------|
|       1447 | 力鵬         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             64.8 | mild_accumulation    | repeated_but_no_breakout | high_momentum_risk_follow | price_reaction_priced_in  | ??????????????????????????????????? D+5/D+10 ??? |
|       1301 | 台塑         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       1326 | 台化         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       1616 | 億泰         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2207 | 和泰車       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       6591 | 動力-KY      | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       8033 | 雷虎         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             60.8 | distribution_warning | continued_2_3d           | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       6197 | 佳必琪       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             59.6 | mild_accumulation    | repeated_but_no_breakout | high_momentum_risk_follow | price_reaction_priced_in  | ??????????????????????????????????? D+5/D+10 ??? |
|       1303 | 南亞         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       1312 | 國喬         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       1440 | 南紡         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       1444 | 力麗         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       1504 | 東元         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       1609 | 大亞         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2006 | 東和鋼鐵     | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2243 | 宏旭-KY      | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2330 | 台積電       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2501 | 國建         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2834 | 臺企銀       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2838 | 聯邦銀       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2890 | 永豐金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       3380 | 明泰         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       3706 | 神達         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       4566 | 時碩工業     | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       4915 | 致伸         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       4938 | 和碩         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       5880 | 合庫金       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       6176 | 瑞儀         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       6531 | 愛普*        | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       6698 | 旭暉應材     | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       6805 | 富世達       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       8103 | 瀚荃         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       8131 | 福懋科       | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             56.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2354 | 鴻準         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             53.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2392 | 正崴         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             53.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       2402 | 毅嘉         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             53.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       3005 | 神基         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             53.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       3023 | 信邦         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             53.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       3515 | 華擎         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             53.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |
|       8112 | 至上         | 區間內轉強 / 挑戰前高觀察 | neckline_challenge | 僅觀察                    |             53.8 | distribution_warning | stale_signal             | high_momentum_risk_follow | tdcc_distribution_warning | ??????????????????????????????????? D+5/D+10 ??? |

## 2484 Latest Decision

_No rows._

## 2484 Regression Replay

|   case_date | breakout_type   |   score | pattern_stage       | neckline_breakout_flag   | platform_breakout_flag   | volume_confirmed_breakout   |
|------------:|:----------------|--------:|:--------------------|:-------------------------|:-------------------------|:----------------------------|
|    20260511 | pattern_watch   |      43 | pullback_entry_zone | False                    | False                    | False                       |
|    20260512 | pattern_watch   |      35 | pullback_entry_zone | False                    | False                    | False                       |
|    20260513 | pattern_watch   |      35 | pullback_entry_zone | False                    | False                    | False                       |
|    20260514 | pattern_watch   |      40 | pullback_entry_zone | False                    | False                    | False                       |
|    20260515 |                 |         |                     |                          |                          |                             |
|    20260518 | pattern_watch   |      54 | early_entry_watch   | False                    | False                    | False                       |
|    20260519 | pattern_watch   |      54 | early_entry_watch   | False                    | False                    | True                        |
|    20260520 | range_rebound   |      69 | platform_right_side | False                    | False                    | True                        |
|    20260521 | range_rebound   |      69 | platform_right_side | False                    | False                    | True                        |
|    20260522 | range_rebound   |      69 | neckline_breakout   | True                     | True                     | True                        |
|    20260525 | true_breakout   |      94 | breakout_confirmed  | True                     | True                     | True                        |

## 8069 Regression Replay

|   case_date | breakout_type   |   score | pattern_stage      | w_bottom_flag   | early_entry_watch_flag   | neckline_challenge_flag   | neckline_breakout_flag   | platform_breakout_flag   | volume_confirmed_breakout   |
|------------:|:----------------|--------:|:-------------------|:----------------|:-------------------------|:--------------------------|:-------------------------|:-------------------------|:----------------------------|
|    20260505 |                 |         |                    |                 |                          |                           |                          |                          |                             |
|    20260506 |                 |         |                    |                 |                          |                           |                          |                          |                             |
|    20260507 | pattern_watch   |      54 | early_entry_watch  | False           | True                     | False                     | False                    | False                    | True                        |
|    20260508 | range_rebound   |      69 | neckline_challenge | False           | False                    | True                      | False                    | False                    | True                        |
|    20260511 | pattern_watch   |      54 | base_building      | True            | False                    | False                     | False                    | False                    | False                       |
|    20260512 | true_breakout   |      89 | breakout_confirmed | True            | False                    | False                     | True                     | True                     | True                        |
|    20260513 | true_breakout   |      94 | breakout_confirmed | True            | False                    | False                     | True                     | True                     | True                        |
|    20260514 | true_breakout   |      89 | platform_breakout  | True            | False                    | False                     | True                     | True                     | True                        |
|    20260515 |                 |         |                    |                 |                          |                           |                          |                          |                             |
|    20260518 |                 |         |                    |                 |                          |                           |                          |                          |                             |
|    20260519 |                 |         |                    |                 |                          |                           |                          |                          |                             |
|    20260520 |                 |         |                    |                 |                          |                           |                          |                          |                             |
|    20260521 |                 |         |                    |                 |                          |                           |                          |                          |                             |
|    20260522 |                 |         |                    |                 |                          |                           |                          |                          |                             |
|    20260525 |                 |         |                    |                 |                          |                           |                          |                          |                             |
|    20260526 |                 |         |                    |                 |                          |                           |                          |                          |                             |
