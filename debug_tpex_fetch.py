import requests
import pandas as pd
from pathlib import Path


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

TEST_DATE = "20260515"
ROC_DATE_SLASH = "115/05/15"
ROC_DATE_NOSLASH = "1150515"


def try_request(name, url, params=None):
    print(f"\n=== Testing {name} ===")
    print("URL:", url)
    print("PARAMS:", params)

    try:
        r = requests.get(
            url,
            params=params,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30,
        )
        r.encoding = "utf-8"

        print("Status:", r.status_code)
        print("Final URL:", r.url)
        print("Text head:", r.text[:500].replace("\n", " "))

        rows = 0
        sample = ""
        json_type = "not_json"
        keys = ""

        try:
            data = r.json()

            if isinstance(data, dict):
                json_type = "dict"
                keys = str(list(data.keys()))

                aa_data = (
                    data.get("aaData")
                    or data.get("data")
                    or data.get("tables")
                    or []
                )

                if isinstance(aa_data, list):
                    rows = len(aa_data)
                    sample = str(aa_data[0])[:500] if aa_data else ""

            elif isinstance(data, list):
                json_type = "list"
                rows = len(data)
                sample = str(data[0])[:500] if data else ""

        except Exception:
            # 不是 JSON，就嘗試當 CSV/HTML 看有沒有 1815
            text = r.text
            if "1815" in text or "富喬" in text:
                sample = "TEXT_CONTAINS_1815_OR_FUQIAO"
            else:
                sample = text[:500].replace("\n", " ")

        return {
            "name": name,
            "status": r.status_code,
            "final_url": r.url,
            "json_type": json_type,
            "keys": keys,
            "rows": rows,
            "contains_1815": ("1815" in r.text),
            "contains_fu_qiao": ("富喬" in r.text),
            "sample": sample,
        }

    except Exception as e:
        print("Request failed:", e)

        return {
            "name": name,
            "status": "failed",
            "final_url": url,
            "json_type": "",
            "keys": "",
            "rows": 0,
            "contains_1815": False,
            "contains_fu_qiao": False,
            "sample": str(e),
        }


def main():
    tests = [
        {
            "name": "UPPER_DAILY_CLOSE_o_data_with_slash_date",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/DAILY_CLOSE_quotes/stk_quote_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE_SLASH,
                "o": "data",
            },
        },
        {
            "name": "UPPER_DAILY_CLOSE_o_json_with_slash_date",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/DAILY_CLOSE_quotes/stk_quote_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE_SLASH,
                "o": "json",
            },
        },
        {
            "name": "UPPER_DAILY_CLOSE_o_htm_with_slash_date",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/DAILY_CLOSE_quotes/stk_quote_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE_SLASH,
                "o": "htm",
            },
        },
        {
            "name": "UPPER_DAILY_CLOSE_no_o_with_slash_date",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/DAILY_CLOSE_quotes/stk_quote_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE_SLASH,
            },
        },
        {
            "name": "UPPER_DAILY_CLOSE_o_data_no_date",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/DAILY_CLOSE_quotes/stk_quote_result.php",
            "params": {
                "l": "zh-tw",
                "o": "data",
            },
        },
        {
            "name": "UPPER_DAILY_CLOSE_o_data_noslash_date",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/DAILY_CLOSE_quotes/stk_quote_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE_NOSLASH,
                "o": "data",
            },
        },
        {
            "name": "new_zh_tw_pricing_page",
            "url": "https://www.tpex.org.tw/zh-tw/mainboard/trading/info/pricing.html",
            "params": {
                "date": ROC_DATE_SLASH,
            },
        },
    ]

    results = []

    for test in tests:
        results.append(
            try_request(
                name=test["name"],
                url=test["url"],
                params=test["params"],
            )
        )

    df = pd.DataFrame(results)
    df.to_csv("output/debug_tpex_fetch_latest.csv", index=False, encoding="utf-8-sig")

    report_lines = ["# TPEx 抓取測試報告", ""]
    report_lines.append(f"測試日期：{TEST_DATE} / 民國 {ROC_DATE_SLASH}")
    report_lines.append("")
    report_lines.append(df.to_markdown(index=False))
    report_lines.append("")

    Path("output/debug_tpex_fetch_latest.md").write_text(
        "\n".join(report_lines),
        encoding="utf-8"
    )

    print("Debug report generated.")


if __name__ == "__main__":
    main()
