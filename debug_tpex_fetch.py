import requests
import pandas as pd
from pathlib import Path


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

TEST_DATE = "20260515"
ROC_DATE = "115/05/15"


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
        print("Text head:", r.text[:300].replace("\n", " "))

        try:
            data = r.json()
            print("JSON type:", type(data))

            if isinstance(data, dict):
                print("JSON keys:", list(data.keys()))
                fields = data.get("fields") or data.get("tables") or []
                aa_data = data.get("aaData") or data.get("data") or []

                print("fields:", fields[:20] if isinstance(fields, list) else fields)
                print("aaData/data rows:", len(aa_data) if isinstance(aa_data, list) else "not list")

                if isinstance(aa_data, list) and aa_data:
                    print("first row:", aa_data[0])

                return {
                    "name": name,
                    "status": r.status_code,
                    "final_url": r.url,
                    "json_type": "dict",
                    "keys": str(list(data.keys())),
                    "rows": len(aa_data) if isinstance(aa_data, list) else 0,
                    "sample": str(aa_data[0])[:300] if isinstance(aa_data, list) and aa_data else "",
                }

            if isinstance(data, list):
                print("list rows:", len(data))
                print("first row:", data[0] if data else None)

                return {
                    "name": name,
                    "status": r.status_code,
                    "final_url": r.url,
                    "json_type": "list",
                    "keys": "",
                    "rows": len(data),
                    "sample": str(data[0])[:300] if data else "",
                }

        except Exception as e:
            print("JSON parse failed:", e)

        return {
            "name": name,
            "status": r.status_code,
            "final_url": r.url,
            "json_type": "not_json",
            "keys": "",
            "rows": 0,
            "sample": r.text[:300].replace("\n", " "),
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
            "sample": str(e),
        }


def main():
    tests = [
        {
            "name": "legacy_daily_close_quotes",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE,
                "s": "0,asc,0",
            },
        },
        {
            "name": "legacy_daily_close_quotes_no_sort",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE,
            },
        },
        {
            "name": "otc_quotes_no1430_se_EW",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE,
                "se": "EW",
            },
        },
        {
            "name": "otc_quotes_no1430_se_AL",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE,
                "se": "AL",
            },
        },
        {
            "name": "otc_quotes_no1430_se_all",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php",
            "params": {
                "l": "zh-tw",
                "d": ROC_DATE,
                "se": "",
            },
        },
        {
            "name": "otc_quotes_no1430_sect_EW_no_date",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php",
            "params": {
                "l": "zh-tw",
                "sect": "EW",
            },
        },
        {
            "name": "openapi_latest",
            "url": "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes",
            "params": None,
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
    report_lines.append(f"測試日期：{TEST_DATE} / 民國 {ROC_DATE}")
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
