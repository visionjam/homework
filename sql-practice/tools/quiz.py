#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SQL 实战练习台：出题 -> 你写 SQL -> 自动和参考答案比对。

用法：
    python tools/quiz.py            列出全部案例
    python tools/quiz.py 3          开始第 3 题（交互式）
    python tools/quiz.py 3 --answer 直接看参考答案和结果

交互命令：空行提交；:a 看答案；:r 重看题目；:q 退出
"""
import argparse
import json
import os
import sqlite3
import sys
import time
import unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE, "db", "shop.db")
CASE_DIR = os.path.join(BASE, "cases")
PROGRESS = os.path.join(CASE_DIR, ".progress")

MAX_ROWS = 20
MAX_CELL = 28


def load_cases():
    with open(os.path.join(CASE_DIR, "cases.json"), encoding="utf-8") as f:
        return json.load(f)["cases"]


def read_answer(case):
    with open(os.path.join(CASE_DIR, case["file"]), encoding="utf-8") as f:
        return f.read()


def connect():
    if not os.path.exists(DB_PATH):
        sys.exit("找不到练习库：%s" % DB_PATH)
    return sqlite3.connect(DB_PATH)


def load_done():
    try:
        with open(PROGRESS, encoding="utf-8") as f:
            return set(int(x) for x in f.read().split())
    except (OSError, ValueError):
        return set()


def mark_done(cid):
    done = load_done()
    done.add(cid)
    try:
        with open(PROGRESS, "w", encoding="utf-8") as f:
            f.write(" ".join(str(x) for x in sorted(done)))
    except OSError:
        pass


def dwidth(s):
    return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1 for ch in s)


def pad(s, width):
    return s + " " * max(0, width - dwidth(s))


def cell(v):
    if v is None:
        s = "NULL"
    elif isinstance(v, float):
        s = ("%.4f" % v).rstrip("0").rstrip(".")
    else:
        s = str(v)
    return s[:MAX_CELL]


def print_table(cols, rows):
    if not cols:
        print("（没有结果集）")
        return
    body = [[cell(v) for v in r] for r in rows[:MAX_ROWS]]
    widths = [dwidth(c) for c in cols]
    for r in body:
        for i, v in enumerate(r):
            widths[i] = max(widths[i], dwidth(v))
    print("  ".join(pad(c, widths[i]) for i, c in enumerate(cols)))
    print("-" * (sum(widths) + 2 * (len(widths) - 1)))
    for r in body:
        print("  ".join(pad(v, widths[i]) for i, v in enumerate(r)))
    if len(rows) > MAX_ROWS:
        print("... 共 %d 行，只显示前 %d 行" % (len(rows), MAX_ROWS))


def run_sql(conn, sql):
    sql = sql.strip()
    while sql.endswith(";"):
        sql = sql[:-1].rstrip()
    cur = conn.execute(sql)
    cols = [d[0] for d in cur.description] if cur.description else []
    return cols, cur.fetchall()


def norm(rows):
    out = []
    for r in rows:
        row = []
        for v in r:
            row.append(round(v, 4) if isinstance(v, float) else v)
        out.append(tuple(row))
    return out


def compare(user_rows, ref_rows):
    u, r = norm(user_rows), norm(ref_rows)
    if len(u) != len(r):
        return False, ["行数不一致：你 %d 行，参考 %d 行" % (len(u), len(r))]
    if u and len(u[0]) != len(r[0]):
        return False, ["列数不一致：你 %d 列，参考 %d 列" % (len(u[0]), len(r[0]))]
    su = sorted(u, key=repr)
    sr = sorted(r, key=repr)
    if su != sr:
        lines = ["数值/内容不一致，前 3 处差异："]
        shown = 0
        for a, b in zip(su, sr):
            if a != b and shown < 3:
                lines.append("  你的: %s" % (a,))
                lines.append("  参考: %s" % (b,))
                shown += 1
        return False, lines
    if u != r:
        return True, ["结果一致，但行顺序和参考答案不同 —— 检查 ORDER BY"]
    return True, ["完全一致，漂亮。"]


def show_case(case):
    print("=" * 68)
    print("案例 %02d  %s    难度 %s" % (case["id"], case["title"], case["difficulty"]))
    print("考察：%s" % case["topic"])
    print("-" * 68)
    print("背景：%s" % case["background"])
    print("口径：%s" % case["metric"])
    print("提示：")
    for h in case["hints"]:
        print("  - %s" % h)
    print("=" * 68)


def read_sql():
    lines = []
    while True:
        try:
            line = input("sql> " if not lines else "  -> ")
        except (EOFError, KeyboardInterrupt):
            print()
            return None
        if line.strip() == "" and not lines:
            continue
        if line.strip() == "" and lines:
            break
        lines.append(line)
    return "\n".join(lines)


def practice(case, conn):
    show_case(case)
    ref_sql = read_answer(case)
    try:
        ref_cols, ref_rows = run_sql(conn, ref_sql)
    except sqlite3.Error as e:
        sys.exit("参考答案跑不通（数据或 SQL 有问题）：%s" % e)
    print("输入 SQL，空行提交；:a 看答案，:r 重看题目，:q 退出")
    print()

    while True:
        sql = read_sql()
        if sql is None:
            return
        cmd = sql.strip().lower()
        if cmd in (":q", ":quit", "quit", "exit"):
            return
        if cmd in (":a", ":answer"):
            print()
            print("--- 参考答案 ---")
            print(ref_sql.strip())
            print()
            print("--- 参考结果（前 %d 行）---" % MAX_ROWS)
            print_table(ref_cols, ref_rows)
            print()
            continue
        if cmd in (":r", ":reset"):
            print()
            show_case(case)
            print()
            continue

        started = time.time()
        try:
            cols, rows = run_sql(conn, sql)
        except sqlite3.Error as e:
            print("SQL 报错：%s" % e)
            print()
            continue
        elapsed = (time.time() - started) * 1000

        print_table(cols, rows)
        print()
        ok, lines = compare(rows, ref_rows)
        print(("PASS  " if ok else "FAIL  ") + lines[0])
        for extra in lines[1:]:
            print(extra)
        print("（%.0f ms，返回 %d 行）" % (elapsed, len(rows)))
        print()
        if ok:
            mark_done(case["id"])


def main():
    ap = argparse.ArgumentParser(description="SQL 实战练习台")
    ap.add_argument("case_id", nargs="?", type=int, help="案例编号；不带则列出全部")
    ap.add_argument("--answer", action="store_true", help="直接显示参考答案和结果")
    args = ap.parse_args()

    cases = load_cases()
    if args.case_id is None:
        done = load_done()
        print("可用案例：")
        for c in cases:
            flag = "[done]" if c["id"] in done else "      "
            print("  %2d. %s %s %-30s %s" % (c["id"], flag, c["difficulty"], c["title"], c["topic"]))
        print()
        print("用法：python tools/quiz.py <编号>")
        return

    case = next((c for c in cases if c["id"] == args.case_id), None)
    if case is None:
        sys.exit("没有编号 %d 的案例" % args.case_id)

    conn = connect()
    if args.answer:
        show_case(case)
        sql = read_answer(case)
        print()
        print("--- 参考答案 ---")
        print(sql.strip())
        print()
        print("--- 参考结果 ---")
        cols, rows = run_sql(conn, sql)
        print_table(cols, rows)
        print()
        print("共 %d 行" % len(rows))
        return

    practice(case, conn)


if __name__ == "__main__":
    main()
