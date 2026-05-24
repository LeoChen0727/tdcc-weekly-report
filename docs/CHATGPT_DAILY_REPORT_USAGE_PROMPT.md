請用 tdcc-weekly-report 的多入口資料流程產出每日台股全市場候選股分析。請先讀原始資料與 packet，不要優先用 PDF。

資料來源優先順序：

1. 優先讀 READ_ME_FIRST_DAILY_REPORT.txt。
2. 依 READ_ME_FIRST 裡的 URL 讀 packet、CSV、source tables、signal logs、warrant tables、market tables、catalyst logs、validation files。
3. PDF 只作為輔助與可分享成品，不是第一資料來源。
4. 只有在原始 CSV / packet / source tables 讀不到時，才使用 PDF 內容。
5. 如果本次只能使用 PDF，請在回答第一行明確寫：
   本次僅使用 PDF 報告資料，未讀取原始 CSV / packet / source tables，因此只能做摘要型分析。

入口檔：

優先讀 GitHub Pages：

https://LeoChen0727.github.io/tdcc-weekly-report/latest/READ_ME_FIRST_DAILY_REPORT.txt

如果 Pages 讀不到，再讀 raw：

https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/READ_ME_FIRST_DAILY_REPORT.txt

請解析 READ_ME_FIRST 的 key=value，至少讀取：

- main_price_date
- report_ready
- preferred_chatgpt_url
- packet_pages_url
- packet_commit_raw_url
- packet_latest_raw_url
- packet_github_api_url
- rules_pages_url
- rules_raw_url
- daily_market_curated_pdf_pages_url
- daily_market_full_table_pdf_pages_url
- warrant_market_report_pdf_pages_url
- market_risk_dashboard_pdf_pages_url
- daily_signal_performance_summary_raw_url
- catalyst_needs_review_csv_raw_url
- catalyst_needs_review_md_raw_url
- read_order

讀取順序：

1. 先讀 rules_pages_url；失敗再讀 rules_raw_url。
2. 再讀 preferred_chatgpt_url。
3. 如果 preferred_chatgpt_url 失敗，依 read_order 讀：
   packet_pages_url
   packet_commit_raw_url
   packet_latest_raw_url
   packet_github_api_url
4. 如果讀 packet_github_api_url，要解析 GitHub API JSON 的 content 欄位並 base64 decode。
5. packet 必須包含：
   CHATGPT DAILY REPORT PACKET
   EMBEDDED SUMMARY REPORT
   EMBEDDED FULL REPORT

正式分析資料規則：

- 原始資料優先，PDF 輔助。
- 不准用舊日期資料重做今天報告。
- 不准把讀取工具失敗或 cache miss 說成 GitHub 沒更新。
- 如果所有入口都讀不到，只能說：讀取工具失敗，目前無法取得 GitHub 已產出的報告內容。
- 如果資料日期不一致，先指出日期不一致，不要硬分析。
- 如果只讀到 PDF，必須在回答開頭揭露只使用 PDF。

每日候選股分析請使用六大分類，不要新增第七大分類：

1. 嚴格突破
2. 區間內轉強 / 挑戰前高觀察
3. 營收爆發低反應股
4. 營收成長股價回檔
5. 回檔後短線轉強
6. 型態觀察

事件 / 財報 / 題材催化層只作為跨分類標籤，不是新分類。請讀取 catalyst_needs_review_*：

- model_effect_allowed=False 的資料不能影響分數、排名、升級、降級或 similar_to_shihsinko_flag。
- pdf_effect_allowed=False 的資料不能當成正式 PDF 推薦理由。
- 股東會日期、BLS CPI / 就業、未有明確來源的展覽 / 新技術驗證 / 新聞 / 法說 / 重大訊息，在正式 source row 進入資料表前，只能列為待確認，不得當作利多。

報告輸出架構：

一、資料狀態確認
二、今日總覽
三、族群性分析 / 今日族群輪動
四、分類解讀
五、財報 / 事件催化觀察
六、權證市場與資金熱度輔助
七、大盤 / 期權 / 市場風險背景
八、今日優先追蹤清單
九、風險提醒
十、明日觀察重點

請同時提供四份成品連結或摘要：

1. 每日推薦精華 PDF：daily_market_curated_pdf_pages_url
2. 每日完整表格 PDF：daily_market_full_table_pdf_pages_url
3. 權證市場報告 PDF：warrant_market_report_pdf_pages_url
4. 大盤 / 期權 / 市場風險 PDF：market_risk_dashboard_pdf_pages_url

注意：

- 權證只作輔助訊號，不可單獨作為買進理由。
- 大盤期權資料是背景，不是個股買賣指令。
- TDCC 是背景確認，不是硬篩選。
- 不要把不同分類分數混成總排名。
- 不要把區間轉強混入嚴格突破。
- 不要把營收爆發低反應股混入營收成長股價回檔。
- 營建 / 交屋認列型營收不能因單月 YoY 暴增就列為最優先，必須等 EPS、毛利率、合約負債、建案交屋進度、TDCC 與股價確認。
- 不要分析使用者個人持股、成本、損益、融資風險或個人部位操作。
