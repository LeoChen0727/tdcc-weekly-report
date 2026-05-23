# Stock Price History Usage Rules

可直接複製以下文字給其他 ChatGPT 對話使用。

```text
請使用 tdcc-weekly-report repo 內的固定資料來源分析個股，不要臨時重抓或自行猜資料。

Repo:
https://github.com/LeoChen0727/tdcc-weekly-report

個股歷史價格 CSV 格式：
https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/{stock_id}.csv

例如宏碁 2353：
https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2353.csv

個股報告 PDF / Markdown 若已由 GitHub Action 產出，優先讀：
https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/{stock_id}_latest.pdf
https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/{stock_id}_latest.md

個股歷史價格 manifest：
https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/stock_price_history_manifest.csv

分析規則：
1. 不要因為股票沒有進今日候選分類就拒絕分析。
2. 今日候選分類只是一個附加訊號，不是分析前提。
3. 優先使用 data/stock_price_history/{stock_id}.csv 判斷價格、量能、均線、前高、回檔與突破。
4. 如果個股報告 PDF / Markdown 已存在，優先讀個股報告。
5. 如果個股報告不存在，讀個股歷史價格 CSV，再搭配每日全市場報告 packet 或 all_candidates 補充分類、TDCC、權證、營收訊號。
6. 請確認資料日期，不要用舊日期資料重做新日期分析。
7. 不要把不同分類分數混成總排名。
8. 不要把區間轉強說成嚴格突破。
9. 不要把營收爆發低反應股混入營收成長股價回檔。
10. 權證只作輔助，不可單獨當成買進理由。
11. TDCC 是背景確認，不是單獨買賣依據。

請輸出：
一、資料狀態
二、個股總結
三、價格與型態
四、營收判斷
五、TDCC 判斷
六、權證判斷
七、若有今日候選分類，列出分類與分數；若沒有，也照樣分析
八、風險提醒
九、明日觀察條件
```
