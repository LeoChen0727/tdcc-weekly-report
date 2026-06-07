# Individual Stock Available Raw Data Index

- generated_at: 2026-06-07 22:25:41 Asia/Taipei
- total_stocks: 2370
- standard_rawdata_report: 2210
- partial_rawdata_report: 160
- insufficient_data: 0
- insufficient_tdcc_history: 1891
- csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_available_raw_data_index.csv

## Columns

- `report_status=standard_rawdata_report` means price raw data has at least 60 rows.
- `insufficient_tdcc_history` means TDCC history has fewer than 8 weekly rows.
- Missing individual Markdown does not mean missing raw data; use price/TDCC raw first.
- If a `raw.githubusercontent.com/.../main/...` URL returns stale content, use the matching `*_github_api_url` and base64-decode the `content` field.

## Preview

| stock_id | stock_name | price_history_rows | tdcc_history_rows | latest_price_date | latest_tdcc_date | has_individual_md | has_sell_strategy_summary | report_status | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0050 | 元大台灣50 | 142 | 0 | 20260605 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0051 | 元大中型100 | 142 | 0 | 20260605 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0052 | 富邦科技 | 137 | 0 | 20260605 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0053 | 元大電子 | 142 | 0 | 20260605 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0055 | 元大MSCI金融 | 142 | 0 | 20260605 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0056 | 元大高股息 | 142 | 0 | 20260605 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0057 | 富邦摩台 | 142 | 0 | 20260605 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 0061 | 元大寶滬深 | 142 | 0 | 20260605 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 006201 | 元大富櫃50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006203 | 元大MSCI台灣 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006204 | 永豐臺灣加權 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006205 | 富邦上証 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006206 | 元大上證50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006207 | 復華滬深 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 006208 | 富邦台50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00636 | 國泰中國A50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00639 | 富邦深100 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00643 | 群益深証中小 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00645 | 富邦日本 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00646 | 元大S&P500 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00652 | 富邦印度 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00657 | 國泰日經225 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00660 | 元大歐洲50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00661 | 元大日經225 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00662 | 富邦NASDAQ | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00668 | 國泰美國道瓊 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00678 | 群益那斯達克生技 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00690 | 兆豐藍籌30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00692 | 富邦公司治理 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00700 | 富邦恒生國企 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00701 | 國泰股利精選30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00702 | 國泰標普低波高息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00703 | 台新MSCI中國 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00709 | 富邦歐洲 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00712 | 復華富時不動產 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00713 | 元大台灣高息低波 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00714 | 群益道瓊美國地產 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00717 | 富邦美國特別股 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00728 | 第一金工業30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00730 | 富邦臺灣優質高息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00731 | 復華富時高息低波 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00733 | 富邦臺灣中小 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00735 | 國泰臺韓科技 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00736 | 國泰新興市場 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00737 | 國泰AI機器人 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00739 | 元大MSCI A股 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00752 | 中信中國50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00757 | 統一FANG+ | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00762 | 元大全球AI | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00770 | 國泰北美科技 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00771 | 元大US高息特別股 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00783 | 富邦中証500 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00830 | 國泰費城半導體 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00850 | 元大臺灣ESG永續 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00851 | 台新全球AI | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00858 | 永豐美國500大 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00861 | 元大全球未來通訊 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00875 | 國泰網路資安 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00876 | 元大全球5G | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00877 | 復華中國5G | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00878 | 國泰永續高股息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00881 | 國泰台灣科技龍頭 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00882 | 中信中國高股息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00885 | 富邦越南 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00886 | 永豐美國科技 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00887 | 永豐中國科技50大 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00888 | 永豐台灣ESG | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00891 | 中信關鍵半導體 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00892 | 富邦台灣半導體 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00893 | 國泰智能電動車 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00894 | 中信小資高價30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00895 | 富邦未來車 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00896 | 中信綠能及電動車 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00897 | 富邦基因免疫生技 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00898 | 國泰基因免疫革命 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00899 | FT潔淨能源 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00900 | 富邦特選高股息30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00901 | 永豐智能車供應鏈 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00902 | 中信電池及儲能 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00903 | 富邦元宇宙 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00904 | 新光臺灣半導體30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00905 | FT臺灣Smart | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00907 | 永豐優息存股 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00908 | 富邦入息REITs+ | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00909 | 國泰數位支付服務 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00910 | 第一金太空衛星 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00911 | 兆豐洲際半導體 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00912 | 中信臺灣智慧50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00913 | 兆豐台灣晶圓製造 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00915 | 凱基優選高股息30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00916 | 國泰全球品牌50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00917 | 中信特選金融 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00918 | 大華優利高填息30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00919 | 群益台灣精選高息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00920 | 富邦ESG綠色電力 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00921 | 兆豐龍頭等權重 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00922 | 國泰台灣領袖50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00923 | 群益台ESG低碳50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00924 | 復華S&P500成長 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00926 | 凱基全球菁英55 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00927 | 群益半導體收益 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00928 | 中信上櫃ESG 30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00929 | 復華台灣科技優息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00930 | 永豐ESG低碳高息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00932 | 兆豐永續高息等權 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00934 | 中信成長高股息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00935 | 野村臺灣新科技50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00936 | 台新永續高息中小 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00938 | 凱基優選30 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00939 | 統一台灣高息動能 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00940 | 元大台灣價值高息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00941 | 中信上游半導體 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00943 | 兆豐電子高息等權 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00944 | 野村趨勢動能高息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00946 | 群益科技高息成長 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00947 | 台新臺灣IC設計 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00949 | 復華日本龍頭 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00951 | 台新日本半導體 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00952 | 凱基台灣AI50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00954 | 中信日本半導體 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00955 | 中信日本商社 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00956 | 中信日經高股息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00960 | 野村全球航運龍頭 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00961 | FT臺灣永續高息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00962 | 台新AI優息動能 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00963 | 中信全球高股息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00964 | 中信亞太高股息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00965 | 元大航太防衛科技 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00971 | 野村美國研發龍頭 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 00972 | 野村日本動能高息 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009800 | 中信NASDAQ | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009801 | 中信美國創新科技 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009802 | 富邦旗艦50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009803 | 玉山市值動能50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009804 | 聯邦台精彩50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009805 | 新光美國電力基建 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009806 | 台新標普500 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009807 | 台新標普科技精選 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009808 | 華南永昌優選50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009809 | 富邦淨零ESG50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009810 | 玉山全球藍籌100 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009811 | 統一美國50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009812 | 野村日本東證 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009813 | 貝萊德標普卓越50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009814 | 富邦標普500 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009815 | 大華美國MAG7+ | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009816 | 凱基台灣TOP50 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009817 | 國泰日本不動產 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009818 | 華南永昌NASDAQxT | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009819 | 中信數據及電力 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009820 | 元大納斯達克精選 | 11 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 009822 | 華南永昌未來金融 | 3 | 0 | 20260605 |  | False | False | partial_rawdata_report | insufficient_price_history; tdcc_history_missing |
| 0200 | 兆豐半導體氣候N | 136 | 0 | 20251031 |  | False | False | standard_rawdata_report | tdcc_history_missing |
| 1101 | 台泥 | 277 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1102 | 亞泥 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1103 | 嘉泥 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1104 | 環泥 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1108 | 幸福 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1109 | 信大 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1110 | 東泥 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1201 | 味全 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1203 | 味王 | 277 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1210 | 大成 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1213 | 大飲 | 263 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1215 | 卜蜂 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1216 | 統一 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1217 | 愛之味 | 278 | 28 | 20260605 | 20260605 | False | False | standard_rawdata_report |  |
| 1218 | 泰山 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1219 | 福壽 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1220 | 台榮 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1225 | 福懋油 | 227 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1227 | 佳格 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1229 | 聯華 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1231 | 聯華食 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1232 | 大統益 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1233 | 天仁 | 278 | 28 | 20260605 | 20260605 | False | False | standard_rawdata_report |  |
| 1234 | 黑松 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1235 | 興泰 | 273 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1236 | 宏亞 | 275 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1240 | 茂生農經 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1256 | 鮮活果汁-KY | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1259 | 安心 | 258 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1264 | 德麥 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1268 | 漢來美食 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1294 | 漢田生技 | 277 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1295 | 生合 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1301 | 台塑 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1303 | 南亞 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1304 | 台聚 | 278 | 28 | 20260605 | 20260605 | False | False | standard_rawdata_report |  |
| 1305 | 華夏 | 278 | 28 | 20260605 | 20260605 | False | False | standard_rawdata_report |  |
| 1307 | 三芳 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1308 | 亞聚 | 278 | 28 | 20260605 | 20260605 | False | False | standard_rawdata_report |  |
| 1309 | 台達化 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1310 | 台苯 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1312 | 國喬 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1313 | 聯成 | 278 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1314 | 中石化 | 277 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1315 | 達新 | 270 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1316 | 上曜 | 277 | 6 | 20260605 | 20260605 | False | False | standard_rawdata_report | insufficient_tdcc_history |
| 1319 | 東陽 | 278 | 28 | 20260605 | 20260605 | False | False | standard_rawdata_report |  |

_Only first 200 rows shown. Use the CSV for the full index._
