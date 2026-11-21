#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""自检：把 11 个参考答案全部跑一遍，确认数据、SQL、判分链路都正常。

用法：python tools/verify.py
"""
import json
import os
import sqlite3
import sys
import time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE, "db", "shop.db")
CASE_DIR = os.path.join(BASE, "cases")


def main():
    if not os.path.exists(DB_PATH):
        sys.exit("缺少 %s，先运行 python db/build_db.py" % DB_PATH)

    with open(os.path.join(CASE_DIR, "cases.json"), encoding="utf-8") as f:
        cases = json.load(f)["cases"]

    conn = sqlite3.connect(DB_PATH)
    failed = 0
    print("%-4s %-32s %6s %5s %8s" % ("id", "title", "rows", "cols", "ms"))
    print("-" * 62)
    for case in cases:
        with open(os.path.join(CASE_DIR, case["file"]), encoding="utf-8") as f:
            sql = f.read().strip().rstrip(";")
        started = time.time()
        try:
            cur = conn.execute(sql)
            rows = cur.fetchall()
            cols = cur.description
        except sqlite3.Error as e:
            failed += 1
            print("%-4d %-32s ERROR: %s" % (case["id"], case["title"], e))
            continue
        ms = (time.time() - started) * 1000
        if not rows:
            failed += 1
            print("%-4d %-32s 空结果" % (case["id"], case["title"]))
            continue
        print("%-4d %-32s %6d %5d %8.0f" % (case["id"], case["title"], len(rows), len(cols), ms))

    print("-" * 62)
    if failed:
        print("FAIL: %d 个案例有问题" % failed)
        sys.exit(1)
    print("OK: %d 个案例全部可执行、结果非空" % len(cases))


if __name__ == "__main__":
    main()
