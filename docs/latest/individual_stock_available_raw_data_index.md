# Individual Stock Available Raw Data Index

- generated_at: 2026-05-26 23:03:39 Asia/Taipei
- total_stocks: 2149
- standard_rawdata_report: 1956
- partial_rawdata_report: 168
- insufficient_data: 25
- insufficient_tdcc_history: 1890
- csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_available_raw_data_index.csv

## Columns

- `report_status=standard_rawdata_report` means price raw data has at least 60 rows.
- `insufficient_tdcc_history` means TDCC history has fewer than 8 weekly rows.
- Missing individual Markdown does not mean missing raw data; use price/TDCC raw first.
- If a `raw.githubusercontent.com/.../main/...` URL returns stale content, use the matching `*_github_api_url` and base64-decode the `content` field.

## Preview

| stock_id | stock_name | price_history_rows | tdcc_history_rows | latest_price_date | latest_tdcc_date | has_individual_md | has_sell_strategy_summary | report_status | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0001 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 0027 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 0039 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 0050 | 元大台灣50 | 134 | 0 | 20260526 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0051 | 元大中型100 | 134 | 0 | 20260526 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0052 | 富邦科技 | 129 | 0 | 20260526 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0053 | 元大電子 | 134 | 0 | 20260526 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0055 | 元大MSCI金融 | 134 | 0 | 20260526 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0056 | 元大高股息 | 134 | 0 | 20260526 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0057 | 富邦摩台 | 134 | 0 | 20260526 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0061 | 元大寶滬深 | 134 | 0 | 20260526 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0062 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 006201 | 元大富櫃50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006203 | 元大MSCI台灣 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006204 | 永豐臺灣加權 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006205 | 富邦上証 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006206 | 元大上證50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006207 | 復華滬深 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006208 | 富邦台50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0063 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00636 | 國泰中國A50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00639 | 富邦深100 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0064 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00643 | 群益深証中小 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00645 | 富邦日本 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00646 | 元大S&P500 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0065 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00652 | 富邦印度 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00657 | 國泰日經225 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0066 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00660 | 元大歐洲50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00661 | 元大日經225 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00662 | 富邦NASDAQ | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00668 | 國泰美國道瓊 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0067 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00678 | 群益那斯達克生技 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0068 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 0069 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00690 | 兆豐藍籌30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00692 | 富邦公司治理 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0070 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00700 | 富邦恒生國企 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00701 | 國泰股利精選30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00702 | 國泰標普低波高息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00703 | 台新MSCI中國 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00709 | 富邦歐洲 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0071 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00712 | 復華富時不動產 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00713 | 元大台灣高息低波 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00714 | 群益道瓊美國地產 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00717 | 富邦美國特別股 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00728 | 第一金工業30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0073 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00730 | 富邦臺灣優質高息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00731 | 復華富時高息低波 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00733 | 富邦臺灣中小 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00735 | 國泰臺韓科技 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00736 | 國泰新興市場 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00737 | 國泰AI機器人 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00739 | 元大MSCI A股 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0075 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00752 | 中信中國50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00757 | 統一FANG+ | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0076 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00762 | 元大全球AI | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00770 | 國泰北美科技 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00771 | 元大US高息特別股 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00783 | 富邦中証500 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0083 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00830 | 國泰費城半導體 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0085 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00850 | 元大臺灣ESG永續 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00851 | 台新全球AI | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00858 | 永豐美國500大 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00861 | 元大全球未來通訊 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0087 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00875 | 國泰網路資安 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00876 | 元大全球5G | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00877 | 復華中國5G | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00878 | 國泰永續高股息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0088 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00881 | 國泰台灣科技龍頭 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00882 | 中信中國高股息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00885 | 富邦越南 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00886 | 永豐美國科技 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00887 | 永豐中國科技50大 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00888 | 永豐台灣ESG | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0089 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00891 | 中信關鍵半導體 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00892 | 富邦台灣半導體 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00893 | 國泰智能電動車 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00894 | 中信小資高價30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00895 | 富邦未來車 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00896 | 中信綠能及電動車 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00897 | 富邦基因免疫生技 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00898 | 國泰基因免疫革命 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00899 | FT潔淨能源 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0090 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00900 | 富邦特選高股息30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00901 | 永豐智能車供應鏈 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00902 | 中信電池及儲能 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00903 | 富邦元宇宙 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00904 | 新光臺灣半導體30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00905 | FT臺灣Smart | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00907 | 永豐優息存股 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00908 | 富邦入息REITs+ | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00909 | 國泰數位支付服務 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0091 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00910 | 第一金太空衛星 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00911 | 兆豐洲際半導體 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00912 | 中信臺灣智慧50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00913 | 兆豐台灣晶圓製造 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00915 | 凱基優選高股息30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00916 | 國泰全球品牌50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00917 | 中信特選金融 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00918 | 大華優利高填息30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00919 | 群益台灣精選高息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0092 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 00920 | 富邦ESG綠色電力 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00921 | 兆豐龍頭等權重 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00922 | 國泰台灣領袖50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00923 | 群益台ESG低碳50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00924 | 復華S&P500成長 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00926 | 凱基全球菁英55 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00927 | 群益半導體收益 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00928 | 中信上櫃ESG 30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00929 | 復華台灣科技優息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00930 | 永豐ESG低碳高息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00932 | 兆豐永續高息等權 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00934 | 中信成長高股息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00935 | 野村臺灣新科技50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00936 | 台新永續高息中小 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00938 | 凱基優選30 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00939 | 統一台灣高息動能 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00940 | 元大台灣價值高息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00941 | 中信上游半導體 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00943 | 兆豐電子高息等權 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00944 | 野村趨勢動能高息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00946 | 群益科技高息成長 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00947 | 台新臺灣IC設計 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00949 | 復華日本龍頭 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00951 | 台新日本半導體 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00952 | 凱基台灣AI50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00954 | 中信日本半導體 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00955 | 中信日本商社 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00956 | 中信日經高股息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00960 | 野村全球航運龍頭 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00961 | FT臺灣永續高息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00962 | 台新AI優息動能 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00963 | 中信全球高股息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00964 | 中信亞太高股息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00965 | 元大航太防衛科技 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00971 | 野村美國研發龍頭 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00972 | 野村日本動能高息 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0098 |  | 0 | 0 |  |  | False | False | insufficient_data | price_history_missing; tdcc_history_missing |
| 009800 | 中信NASDAQ | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009801 | 中信美國創新科技 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009802 | 富邦旗艦50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009803 | 玉山市值動能50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009804 | 聯邦台精彩50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009805 | 新光美國電力基建 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009806 | 台新標普500 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009807 | 台新標普科技精選 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009808 | 華南永昌優選50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009809 | 富邦淨零ESG50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009810 | 玉山全球藍籌100 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009811 | 統一美國50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009812 | 野村日本東證 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009813 | 貝萊德標普卓越50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009814 | 富邦標普500 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009815 | 大華美國MAG7+ | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009816 | 凱基台灣TOP50 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009817 | 國泰日本不動產 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009818 | 華南永昌NASDAQxT | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009819 | 中信數據及電力 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009820 | 元大納斯達克精選 | 3 | 0 | 20260526 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 1101 | 台泥 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1102 | 亞泥 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1103 | 嘉泥 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1104 | 環泥 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1108 | 幸福 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1109 | 信大 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1110 | 東泥 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1201 | 味全 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1203 | 味王 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1210 | 大成 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1213 | 大飲 | 128 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1215 | 卜蜂 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1216 | 統一 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1217 | 愛之味 | 134 | 26 | 20260526 | 20260522 | False | False | standard_rawdata_report |  |
| 1218 | 泰山 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1219 | 福壽 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1220 | 台榮 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1225 | 福懋油 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1227 | 佳格 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1229 | 聯華 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1231 | 聯華食 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1232 | 大統益 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1233 | 天仁 | 134 | 26 | 20260526 | 20260522 | False | False | standard_rawdata_report |  |
| 1234 | 黑松 | 134 | 4 | 20260526 | 20260522 | False | False | standard_rawdata_report | insufficient_tdcc_history |

_Only first 200 rows shown. Use the CSV for the full index._
