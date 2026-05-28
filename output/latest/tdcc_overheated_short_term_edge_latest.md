# TDCC Overheated Short-Term Edge

- generated_at: `2026-05-28 20:06:44 Asia/Taipei`
- tuning_status: `not_ready`
- allowed_changes: `reporting_priority_only`
- forbidden_changes: `core_weight_change`

## Calculation Method

- close-to-close win rate: `dN_return_pct > 0`, from signal close to D+N close, only mature_dN=True rows.
- close-to-close relative return: stock D+N return minus TWSE/TPEx benchmark D+N return.
- next-open return: next trading day's open to D+N close.
- next-open relative return: stock next-open return minus benchmark next-open return when benchmark OHLC is available.
- pending rows are not counted as success or failure.
- These rules are a short-term reporting specialty, not a core TDCC/ABM weight change.

## Current Matching Stocks

| signal_date | stock_id | stock_name | theme | rule_name_zh | price_ret_1w | price_ret_2w | d5_mature_count | d5_win_rate_pct | d5_avg_relative_return_pct | d10_mature_count | d10_win_rate_pct | d10_avg_relative_return_pct | sample_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260522 | 3624 | 光頡 | passive components | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.0787401574803 | 55.084745762711876 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3481 | 群創 | consumer electronics | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.684210526315773 | 51.87074829931972 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3357 | 臺慶科 | passive components | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.818181818181806 | 48.8 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8043 | 蜜望實 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.486725663716804 | 45.32293986636971 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2302 | 麗正 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.306451612903224 | 43.73401534526855 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6207 | 雷科 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.45077720207255 | 41.35220125786163 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 1727 | 中華化 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.704805491990847 | 41.07883817427387 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8091 | 翔名 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 12.658227848101266 | 39.79057591623037 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2316 | 楠梓電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.53281853281854 | 36.444444444444436 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 5328 | 華容 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.125874125874127 | 31.970260223048342 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6209 | 今國光 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 28.059701492537314 | 30.000000000000004 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6116 | 彩晶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.609756097560968 | 28.80434782608696 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8121 | 越峰 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.323529411764692 | 28.409090909090896 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6239 | 力成 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 14.11290322580645 | 27.477477477477485 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2428 | 興勤 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.71844660194175 | 27.296587926509197 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8261 | 富鼎 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 18.959107806691456 | 26.984126984126977 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6284 | 佳邦 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 21.301775147928993 | 25.76687116564418 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6237 | 驊訊 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.912472647702394 | 25.54410080183276 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6271 | 同欣電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.966101694915245 | 24.79338842975207 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3704 | 合勤控 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 15.183246073298417 | 24.64589235127479 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6570 | 維田 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.932084309133497 | 23.74429223744294 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8096 | 擎亞 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 23.566214807090713 | 23.566214807090713 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2489 | 瑞軒 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 27.38537794299876 | 23.557692307692292 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6182 | 合晶 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 26.630434782608692 | 22.847100175746938 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2401 | 凌陽 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 24.74645030425964 | 21.54150197628457 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 5425 | 台半 | power discrete/diodes | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 20.972222222222214 | 19.315068493150676 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 4919 | 新唐 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 29.126213592233018 | 19.104477611940297 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2233 | 宇隆 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 17.627118644067806 | 18.835616438356162 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2464 | 盟立 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 13.833992094861669 | 18.032786885245898 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2472 | 立隆電 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 19.815668202764968 | 17.381489841986465 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6706 | 惠特 | other | 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 16.719242902208208 | 7.246376811594213 | 54 | 61.11 | 4.90 | 30 | 86.67 | 12.14 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 4542 | 科嶠 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 35.365853658536594 | 41.58163265306123 | 37 | 45.95 | 2.25 | 31 | 83.87 | 13.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 1727 | 中華化 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 16.704805491990847 | 41.07883817427387 | 37 | 45.95 | 2.25 | 31 | 83.87 | 13.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3673 | TPK-KY | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 19.010819165378656 | 30.508474576271194 | 37 | 45.95 | 2.25 | 31 | 83.87 | 13.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6239 | 力成 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 14.11290322580645 | 27.477477477477485 | 37 | 45.95 | 2.25 | 31 | 83.87 | 13.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2489 | 瑞軒 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 27.38537794299876 | 23.557692307692292 | 37 | 45.95 | 2.25 | 31 | 83.87 | 13.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3663 | 鑫科 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 25.94202898550726 | 20.52704576976423 | 37 | 45.95 | 2.25 | 31 | 83.87 | 13.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2495 | 普安 | other | TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 25.74679943100997 | 20.108695652173925 | 37 | 45.95 | 2.25 | 31 | 83.87 | 13.47 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3357 | 臺慶科 | passive components | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.818181818181806 | 48.8 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6166 | 凌華 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.392857142857139 | 45.475372279495986 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8043 | 蜜望實 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.486725663716804 | 45.32293986636971 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2302 | 麗正 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.306451612903224 | 43.73401534526855 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6207 | 雷科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.45077720207255 | 41.35220125786163 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 1727 | 中華化 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.704805491990847 | 41.07883817427387 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3141 | 晶宏 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.167938931297712 | 40.72727272727275 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8091 | 翔名 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 12.658227848101266 | 39.79057591623037 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3615 | 安可 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.651006711409387 | 39.44281524926685 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8289 | 泰藝 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.703703703703695 | 36.88524590163935 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2316 | 楠梓電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.53281853281854 | 36.444444444444436 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 5464 | 霖宏 | PCB/CCL | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.3432574430823 | 35.49618320610688 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2481 | 強茂 | power discrete/diodes | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 13.617021276595743 | 34.170854271356774 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3189 | 景碩 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.308641975308642 | 32.969432314410476 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6415 | 矽力*-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 20.08547008547008 | 32.07990599294948 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 5328 | 華容 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.125874125874127 | 31.970260223048342 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 1582 | 信錦 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.69416498993963 | 30.97949886104785 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3673 | TPK-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.010819165378656 | 30.508474576271194 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6209 | 今國光 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.059701492537314 | 30.000000000000004 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6116 | 彩晶 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.609756097560968 | 28.80434782608696 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 4958 | 臻鼎-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 28.6783042394015 | 28.6783042394015 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8121 | 越峰 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 16.323529411764692 | 28.409090909090896 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6239 | 力成 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 14.11290322580645 | 27.477477477477485 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2428 | 興勤 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 17.71844660194175 | 27.296587926509197 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8261 | 富鼎 | power discrete/diodes | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 18.959107806691456 | 26.984126984126977 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 4991 | 環宇-KY | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.791277258566982 | 26.39751552795031 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6284 | 佳邦 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 21.301775147928993 | 25.76687116564418 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6237 | 驊訊 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 19.912472647702394 | 25.54410080183276 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6271 | 同欣電 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.966101694915245 | 24.79338842975207 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3704 | 合勤控 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 15.183246073298417 | 24.64589235127479 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6570 | 維田 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.932084309133497 | 23.74429223744294 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 8096 | 擎亞 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 23.566214807090713 | 23.566214807090713 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2489 | 瑞軒 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 27.38537794299876 | 23.557692307692292 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 6182 | 合晶 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 26.630434782608692 | 22.847100175746938 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2401 | 凌陽 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 24.74645030425964 | 21.54150197628457 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 3663 | 鑫科 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.94202898550726 | 20.52704576976423 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |
| 20260522 | 2495 | 普安 | other | TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 25.74679943100997 | 20.108695652173925 | 53 | 56.60 | 3.53 | 30 | 83.33 | 11.69 | short-term TDCC overheated edge; reporting-only until more market regimes mature |

## D+5 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 37 | 45.95 | 2.39 | -0.91 | 2.25 | 37 | 45.95 | 1.55 | 1.55 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 53 | 56.60 | 4.45 | 2.81 | 3.53 | 53 | 60.38 | 4.14 | 3.13 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 54 | 61.11 | 5.75 | 2.95 | 4.90 | 54 | 59.26 | 4.22 | 3.36 | ok_initial_sample |

## D+10 Table

| rule_name_zh | mature_count | win_rate_close_to_close_pct | avg_return_close_to_close_pct | median_return_close_to_close_pct | avg_relative_return_vs_benchmark_pct | next_open_mature_count | win_rate_next_open_to_close_pct | avg_next_open_to_close_return_pct | avg_next_open_relative_return_vs_benchmark_pct | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週 | 31 | 83.87 | 16.07 | 12.07 | 13.47 | 31 | 80.65 | 15.10 | 12.73 | ok_initial_sample |
| TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50% | 30 | 83.33 | 13.53 | 8.73 | 11.69 | 30 | 73.33 | 12.49 | 10.71 | ok_initial_sample |
| 四級距同步過熱 + 1週漲10~30% + MACD histogram > 0 | 30 | 86.67 | 13.98 | 10.57 | 12.14 | 30 | 73.33 | 11.29 | 9.64 | ok_initial_sample |
