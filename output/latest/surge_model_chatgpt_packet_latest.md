# SURGE MODEL CHATGPT PACKET

## Metadata
- generated_at: 2026-05-27 21:25:10 Asia/Taipei
- main_price_date: 20260527
- surge_definition: surge_5d=future 5d high >= 20%; surge_10d=future 10d high >= 25%; surge_20d=future 20d high >= 35%
- feature_panel_rows: 260869
- mature_5d_count: 251029
- mature_10d_count: 241189
- mature_20d_count: 221509
- baseline_surge_rate_5d: 0.0439
- baseline_surge_rate_10d: 0.0649
- baseline_surge_rate_20d: 0.0800

## Data Availability
- feature_panel: True
- labels: True
- pre_surge_event_study: True
- non_surge_control_sample: True
- tdcc_snapshot: True
- warrant_flow_by_stock: True
- market_index_history: True

## Top Surge Precondition Candidates
| trade_date | stock_id | stock_name | theme | surge_precondition_score | surge_watch_label | tdcc_price_phase | setup_type | abm_score | tdcc_consecutive_up_weeks | price_ret_20d | distance_ma20_pct | volume_ratio_20d | theme_mainstream_status | revenue_yoy | warrant_flow_score | market_regime | risk_flags | reason_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260527 | 1808 | 潤隆 | other | 103.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 81.0 | 2 | -3.066439522998299 | -1.377935696334176 | 1.0366856927270016 |  | 6493.74 |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 1455 | 集盛 | other | 100.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 79.0 | 3 | -4.358068315665498 | 0.061614294516321166 | 1.2043976864151757 |  |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 2412 | 中華電 | other | 100.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 92.0 | 2 | 0.0 | 0.05477451159392466 | 1.1242130566831599 | mainstream_leader |  | 0 | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 3038 | 全台 | other | 100.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 97.0 | 7 | 1.3071895424836555 | 1.717160669364537 | 1.1529927089678365 | mainstream_leader |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 3045 | 台灣大 | other | 100.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 93.0 | 2 | -0.9009009009009028 | -1.7418490397498876 | 1.1803145361896947 | mainstream_leader |  | 0 | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 3050 | 鈺德 | other | 100.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 87.0 | 3 | -0.40160642570280514 | 1.3693030860412847 | 1.7525484199796126 | mainstream_leader | 3.919474447847816 |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 3705 | 永信 | other | 100.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 97.0 | 5 | 0.5434782608695565 | -0.21574973031283085 | 1.5803433501413624 | mainstream_leader |  | 0 | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 5876 | 上海商銀 | other | 100.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 97.0 | 2 | 1.413881748071999 | -0.30955840545832114 | 1.3895091418372878 | mainstream_leader |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 6605 | 帝寶 | other | 100.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 80.0 | 3 | 2.400000000000002 | -0.7559604574529866 | 1.095679060064449 | mainstream_leader |  | 0 | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 2347 | 聯強 | other | 93.0 | A_surge_watch | tdcc_leading_price | watch_only | 85.0 | 3 | 4.1212121212121255 | 2.78808184755297 | 1.1862537217758402 | mainstream_leader | 83.28 | 0.0 | strong_bull |  | TDCC領先股價；靠近MA20；量能溫和 |
| 20260527 | 1319 | 東陽 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 82.0 | 2 | 3.9630118890356725 | -0.1965633124088484 | 0.8810363570529846 |  |  | 0 | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 1737 | 臺鹽 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 81.0 | 4 | -0.4731861198738141 | -0.015845349389953522 | 0.9374817665999119 |  |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 2414 | 精技 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 88.0 | 2 | 12.157721796276032 | 5.768734183752522 | 0.846337734673854 | mainstream_leader |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 2505 | 國揚 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 82.0 | 3 | -2.499999999999991 | -1.6531241244045813 | 0.7435513987466792 |  |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 2603 | 長榮 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 98.0 | 3 | 5.750000000000011 | 1.2082785022131892 | 1.8740032511291331 |  | 4.514054892315798 | 1.0 | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 4535 | 至興 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 76.0 | 3 | -1.4598540145985384 | -1.7199017199017175 | 2.25 |  |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 5306 | 桂盟 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 80.0 | 2 | 1.7305315203955285 | 0.19478938397856638 | 0.7373195305862005 | mainstream_leader |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 5523 | 豐謙 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.0 | 3 | 0.164473684210531 | 0.3956478733926794 | 0.27347310847766637 |  |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 6180 | 橘子 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 82.0 | 3 | 1.5247776365946653 | 1.8807778131973318 | 0.11029918654349924 | mainstream_leader |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 8409 | 商之器 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 82.0 | 13 | -2.7989821882951516 | -2.051282051282044 | 0.9973753280839895 |  |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 8941 | 關中 | other | 92.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 78.0 | 3 | -0.11273957158963732 | -0.08457851705666597 | 2.8852459016393444 |  |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20 |
| 20260527 | 2461 | 光群雷 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 81.0 | 3 | -8.479532163742698 | -4.529510446850682 | 1.3163540179139208 |  |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；量能溫和 |
| 20260527 | 4527 | 方土霖 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 100.0 | 5 | 5.200945626477549 | 2.4991362432339015 | 1.375 | single_name_signal |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 7718 | 友鋮 | other | 90.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 95.0 | 15 | 3.8461538461538547 | -0.1386962552010984 | 1.7223198594024605 | single_name_signal |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 1604 | 聲寶 | other | 85.0 | A_surge_watch | tdcc_leading_price | watch_only | 75.0 | 2 | 1.3015184381778733 | 1.5769439912996175 | 1.2784393140252852 |  |  |  | strong_bull |  | TDCC領先股價；靠近MA20；量能溫和 |
| 20260527 | 2035 | 唐榮 | other | 85.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 92.0 | 2 | 2.722323049001818 | 0.5328596802842034 | 1.122244488977956 | weak_theme |  |  | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 2480 | 敦陽科 | other | 85.0 | A_surge_watch | tdcc_leading_price | watch_only | 75.0 | 2 | 6.159420289855078 | -0.6779661016949157 | 1.2050449133861745 |  |  | 0 | strong_bull |  | TDCC領先股價；靠近MA20；量能溫和 |
| 20260527 | 2610 | 華航 | other | 85.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 87.0 | 3 | 2.216066481994461 | -0.0406338886631441 | 1.7098113702329412 | weak_theme |  | 1 | strong_bull |  | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和 |
| 20260527 | 2731 | 雄獅 | other | 85.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 80.0 | 3 | 4.0752351097178785 | 3.265940902021769 | 1.2707322185708982 |  |  | 0 | strong_bull | failed_breakout | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和；風險:failed_breakout |
| 20260527 | 2816 | 旺旺保 | other | 85.0 | A_surge_watch | tdcc_leading_price | quiet_accumulation | 92.0 | 16 | 6.146179401993357 | 3.5992217898832557 | 1.370116968022479 | mainstream_leader |  |  | strong_bull | failed_breakout | TDCC領先股價；quiet_accumulation；靠近MA20；量能溫和；風險:failed_breakout |

## Feature Importance Summary
| condition_name | sample_count | surge_count | surge_rate | baseline_surge_rate | lift_vs_baseline | avg_future_max_ret_5d | avg_future_max_ret_10d | avg_mae_before_surge | false_positive_rate | precision | recall | control_sample_count | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| relative_ret_20d_vs_twse > 0 | 54341 | 8226 | 0.1513774130030732 | 0.07477952974638147 | 2.024316193435253 | 7.343386466881774 | 11.520037979108118 | -6.102594925654358 | 0.8486225869969268 | 0.1513774130030732 | 0.4560878243512974 | 3297 | ok |
| volume_ratio_20d between 1.0 and 1.8 | 54994 | 4264 | 0.07753573117067317 | 0.07477952974638147 | 1.0368576993415108 | 5.09260955162029 | 7.8557353770585685 | -4.706714599458447 | 0.9224642688293269 | 0.07753573117067317 | 0.23641605677533822 | 3297 | ok |
| distance_ma20_pct between -3 and +6 | 148862 | 7430 | 0.04991199903266112 | 0.07477952974638147 | 0.6674553745114495 | 4.023077735825178 | 6.275613207166932 | -4.213936916774226 | 0.9500880009673389 | 0.04991199903266112 | 0.4119538700377024 | 3297 | ok |
| low volatility compression + volume expansion | 32784 | 906 | 0.027635431918008786 | 0.07477952974638147 | 0.3695587818181759 | 3.293180305348269 | 5.12123124826399 | -3.4680005502387625 | 0.9723645680819912 | 0.027635431918008786 | 0.05023286759813706 | 3297 | ok |
| consolidation_days >= 10 + narrow_range_20d | 96326 | 2318 | 0.024064115607416482 | 0.07477952974638147 | 0.32180084160773864 | 3.0460695855260553 | 4.716638003421715 | -3.375414258374906 | 0.9759358843925835 | 0.024064115607416482 | 0.12852073630516744 | 3297 | ok |
| tdcc_consecutive_up_weeks >= 2 + price_ret_20d <= 8 | 3969 | 72 | 0.018140589569160998 | 0.07477952974638147 | 0.24258763903284386 | 3.1113544766124095 | 4.641487575402634 | -3.419462723448965 | 0.981859410430839 | 0.018140589569160998 | 0.003992015968063872 | 3297 | ok |
| tdcc_leading_price + quiet_accumulation | 0 | 0 |  | 0.07477952974638147 |  |  |  |  |  |  | 0.0 | 3297 | insufficient_sample |
| theme_mainstream_status = emerging_theme | 0 | 0 |  | 0.07477952974638147 |  |  |  |  |  |  | 0.0 | 3297 | insufficient_sample |
| revenue_yoy > 20 + revenue_low_price_response | 0 | 0 |  | 0.07477952974638147 |  |  |  |  |  |  | 0.0 | 3297 | insufficient_sample |
| warrant_call_inflow + TDCC high_thresholds_up | 0 | 0 |  | 0.07477952974638147 |  |  |  |  |  |  | 0.0 | 3297 | insufficient_sample |

## Backtest Summary
| segment | sample_count | surge_5d_rate | surge_10d_rate | surge_20d_rate | baseline_surge_5d_rate | baseline_surge_10d_rate | baseline_surge_20d_rate | lift_5d | lift_10d | lift_20d | avg_future_max_ret_5d | avg_future_max_ret_10d | avg_future_max_ret_20d | avg_max_drawdown_10d | avg_max_drawdown_20d | sample_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| top_10 | 1250 | 0.0064 | 0.0152 | 0.012 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.1520048842934515 | 0.23425385303514376 | 0.1634256352343309 | 2.6619691520398643 | 4.112374015192219 | 6.290146301551732 | -3.5005053767208474 | -4.906530341191594 | ok |
| top_20 | 2500 | 0.006 | 0.0096 | 0.0084 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.14250457902511077 | 0.14794980191693288 | 0.11439794466403161 | 2.6694664051887576 | 4.0732539690179985 | 6.230789203986102 | -3.363857841555222 | -4.687739269684339 | ok |
| top_50 | 6250 | 0.0088 | 0.01248 | 0.01808 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.20900671590349582 | 0.19233474249201277 | 0.24622795708639186 | 2.9652812399191792 | 4.483948609601701 | 6.953068219639194 | -3.4556086878312153 | -4.73381212650269 | ok |
| top_100 | 12500 | 0.012 | 0.01808 | 0.02416 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.28500915805022153 | 0.27863879361022365 | 0.3290302789384529 | 3.0913996462271625 | 4.7063879334081795 | 7.377408283511394 | -3.4181571666945354 | -4.753006261517005 | ok |
| score_ge_80 | 914 | 0.010940919037199124 | 0.016411378555798686 | 0.009846827133479213 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.25985517692398025 | 0.25292293817856415 | 0.1341019982776238 | 2.8701239610325158 | 4.456471319899988 | 6.827643224290943 | -2.8216218560499016 | -4.046657161999553 | ok |
| score_70_80 | 585 | 0.0017094017094017094 | 0.0017094017094017094 | 0.0017094017094017094 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.04059959516384922 | 0.026344337948171814 | 0.023280005019135453 | 2.358820992310576 | 3.825031549098939 | 6.190288312228263 | -3.3857787106883754 | -4.949410153950187 | ok |
| score_60_70 | 363 | 0.008264462809917356 | 0.005509641873278237 | 0.008264462809917356 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.19628729893265948 | 0.08491150247757857 | 0.11255209038177058 | 2.954030784255913 | 4.272680148920883 | 5.730132445902836 | -3.471743365642519 | -5.004677651567718 | ok |
| score_50_60 | 1511 | 0.0066181336863004635 | 0.009265387160820648 | 0.003970880211780278 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.15718572581635867 | 0.1427929369924071 | 0.05407863508746885 | 2.7187386974538565 | 4.174585876147126 | 6.0793590224716425 | -3.6271021546954763 | -4.61206857393751 | ok |
| score_lt_50 | 237816 | 0.042600161469371275 | 0.06567262084973256 | 0.07438944393985265 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 1.011786346099083 | 1.0121095048003927 | 1.0130951775499222 | 5.035815369670503 | 7.818251005232249 | 12.217162859091433 | -4.943587651215034 | -6.541384005307847 | ok |
| label_A_surge_watch | 1070 | 0.009345794392523364 | 0.014953271028037384 | 0.008411214953271028 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.22196974926029714 | 0.23045140485503568 | 0.11455067890256838 | 2.776530748685531 | 4.324243958824947 | 6.7620584068206595 | -2.87551428305158 | -4.105773075219884 | ok |
| label_B_confirm_needed | 738 | 0.0040650406504065045 | 0.0027100271002710027 | 0.005420054200542005 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.09654781776769024 | 0.041765413820272386 | 0.07381465006067339 | 2.6270856191770102 | 4.104724519318609 | 5.950938657861356 | -3.4857364946369636 | -5.081082233231151 | ok |
| label_C_too_hot | 24771 | 0.1267207621815833 | 0.17572968390456584 | 0.17782891284162933 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 3.0097148114046175 | 2.7082470754797656 | 2.421816920347811 | 9.05134858320362 | 13.848828131333658 | 21.26242564408221 | -7.57094705194732 | -9.432545369149802 | ok |
| label_D_weak_or_insufficient | 214610 | 0.032631284655887424 | 0.052555798891011606 | 0.06193560411909976 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.7750179138226323 | 0.8099604203657634 | 0.8434887872321599 | 4.555521019702717 | 7.095518718062414 | 11.216748731429869 | -4.630611223807444 | -6.22187560531132 | ok |
| market_unknown | 241189 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 1.0 | 1.0 | 1.0 | 5.003466156752519 | 7.767662793310808 | 12.148594837939921 | -4.9213051921149376 | -6.518265343384744 | ok |
| theme_unknown | 241189 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 0.04210391021149389 | 0.06488687295025893 | 0.07342789264850387 | 1.0 | 1.0 | 1.0 | 5.003466156752519 | 7.767662793310808 | 12.148594837939921 | -4.9213051921149376 | -6.518265343384744 | ok |

## Risk Summary
- C_too_hot / failed_breakout / high_volume_upper_shadow 不可解讀為暴漲前低位候選。
- 未來資料只用於 label，不可用來產生當日 feature。
- pending 不可視為成功或失敗。
- 樣本不足時標示 insufficient_sample，不做正式調參。

## Model Tuning Status
tuning_status = not_ready
reason = insufficient mature samples for stable feature/weight tuning
allowed_changes = reporting_priority_only
forbidden_changes = core_weight_change

## Raw URLs
- surge_precondition_candidates_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_precondition_candidates_latest.md
- surge_precondition_candidates_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_precondition_candidates_latest.csv
- surge_model_backtest_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_model_backtest_latest.md
- surge_model_backtest_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_model_backtest_latest.csv
- surge_model_feature_importance_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_model_feature_importance_latest.md
- surge_model_feature_importance_csv_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/surge_model_feature_importance_latest.csv
