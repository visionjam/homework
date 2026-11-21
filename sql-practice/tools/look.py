#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数据库导览：先看清数据长什么样，再写查询。

用法：
    python tools/look.py                 # 总览：每张表多少行
    python tools/look.py orders          # 看表结构、前 5 行、每列取值
    python tools/look.py orders 3        # 只看前 3 行
    python tools/look.py --map           # 表之间的关系
    python tools/look.py --sql "SELECT * FROM users LIMIT 3"
    python tools/look.py -i              # 自由查询（空行执行，:q 退出）
"""
import argparse
import os
import sqlite3
import sys
import unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE, "db", "shop.db")

TABLES = ["users", "products", "orders", "order_items", "events"]

TABLE_DOC = {
    "users": ("一个注册用户", {
        "user_id": "用户编号，主键",
        "user_name": "昵称",
        "city": "城市",
        "channel": "注册渠道（这个人从哪来的）",
        "register_date": "注册日期 YYYY-MM-DD",
    }),
    "products": ("一个在售商品", {
        "product_id": "商品编号，主键",
        "product_name": "商品名",
        "category": "品类（6 个之一）",
        "list_price": "标价（原价）",
    }),
    "orders": ("一笔订单", {
        "order_id": "订单号，主键",
        "user_id": "下单用户，对应 users.user_id",
        "order_date": "下单日期 YYYY-MM-DD",
        "status": "paid 已支付 / refunded 已退款 / cancelled 已取消",
        "channel": "下单渠道（和注册渠道不是一回事）",
        "pay_amount": "实付金额，含运费；cancelled 为 0",
        "created_at": "下单时间戳",
    }),
    "order_items": ("订单里的一行商品", {
        "item_id": "明细编号，主键",
        "order_id": "属于哪笔订单，对应 orders.order_id",
        "product_id": "哪个商品，对应 products.product_id",
        "quantity": "买了几件",
        "unit_price": "成交单价（优惠已算进去，不含运费）",
    }),
    "events": ("一条用户行为", {
        "event_id": "行为编号，主键",
        "user_id": "谁做的，对应 users.user_id",
        "event_date": "发生日期",
        "event_type": "view 浏览 / add_cart 加购 / pay 支付",
    }),
}

MAP_TEXT = """
  users ──< orders ──< order_items >── products
    │         (1 个用户 N 笔订单)   (1 笔订单 N 行商品)
    │
    └──< events  (1 个用户 N 条行为)

  读法：箭头指向「多」的一边。
  orders.user_id   -> users.user_id      （这单是谁下的）
  order_items.order_id -> orders.order_id（这行属于哪单）
  order_items.product_id -> products.product_id（这行是哪个商品）
"""


def dwidth(s):
    return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F") else 1 for ch in s)


def pad(s, width):
    return s + " " * max(0, width - dwidth(s))


def rpad(s, width):
    return " " * max(0, width - dwidth(s)) + s


def cell(v):
    if v is None:
        return "NULL"
    if isinstance(v, float):
        return ("%.2f" % v).rstrip("0").rstrip(".")
    return str(v)


def print_table(cols, rows, limit=5):
    if not cols:
        print("（没有结果集）")
        return
    body = [[cell(v) for v in r] for r in rows[:limit]]
    widths = [dwidth(c) for c in cols]
    for r in body:
        for i, v in enumerate(r):
            widths[i] = max(widths[i], dwidth(v))
    print("  ".join(pad(c, widths[i]) for i, c in enumerate(cols)))
    print("-" * (sum(widths) + 2 * (len(widths) - 1)))
    for r in body:
        print("  ".join(pad(v, widths[i]) for i, v in enumerate(r)))
    if len(rows) > limit:
        print("... 共 %d 行，只显示前 %d 行" % (len(rows), limit))


def connect():
    if not os.path.exists(DB_PATH):
        sys.exit("找不到 %s，先运行 python db/build_db.py" % DB_PATH)
    return sqlite3.connect(DB_PATH)


def show_overview(conn):
    print("数据库文件：%s" % DB_PATH)
    print("（就是一个文件，不是服务，不用启动，也没有账号密码）")
    print()
    print(pad("表名", 12) + "  " + rpad("行数", 8) + "  一行代表什么")
    print("-" * 66)
    for t in TABLES:
        n = conn.execute("SELECT COUNT(*) FROM " + t).fetchone()[0]
        print(pad(t, 12) + "  " + rpad(str(n), 8) + "  " + TABLE_DOC[t][0])
    print()
    print("想看某张表：python tools/look.py orders")
    print("想看表关系：python tools/look.py --map")


def show_table(conn, table, limit):
    if table not in TABLE_DOC:
        sys.exit("没有这张表：%s（可选：%s）" % (table, "、".join(TABLES)))
    desc, doc = TABLE_DOC[table]
    n = conn.execute("SELECT COUNT(*) FROM " + table).fetchone()[0]
    print("表 %s —— %s，共 %d 行" % (table, desc, n))
    print()

    cols = conn.execute("PRAGMA table_info(" + table + ")").fetchall()
    print(pad("字段", 14) + "  " + pad("类型", 8) + "  说明")
    print("-" * 70)
    for c in cols:
        print(pad(c[1], 14) + "  " + pad(c[2], 8) + "  " + doc.get(c[1], ""))
    print()

    print("前 %d 行长这样：" % limit)
    cur = conn.execute("SELECT * FROM " + table + " LIMIT %d" % limit)
    print_table([d[0] for d in cur.description], cur.fetchall(), limit)
    print()

    print("每列都有什么值：")
    for c in cols:
        name = c[1]
        distinct = conn.execute(
            "SELECT COUNT(DISTINCT " + name + ") FROM " + table
        ).fetchone()[0]
        nulls = conn.execute(
            "SELECT COUNT(*) FROM " + table + " WHERE " + name + " IS NULL"
        ).fetchone()[0]
        if distinct <= 12:
            vals = conn.execute(
                "SELECT " + name + ", COUNT(*) FROM " + table +
                " GROUP BY " + name + " ORDER BY COUNT(*) DESC"
            ).fetchall()
            text = "、".join("%s(%d)" % (cell(v), k) for v, k in vals)
        else:
            lo, hi = conn.execute(
                "SELECT MIN(" + name + "), MAX(" + name + ") FROM " + table
            ).fetchone()
            text = "%s .. %s（%d 个不同值）" % (cell(lo), cell(hi), distinct)
        if nulls:
            text += "；NULL %d 个" % nulls
        print("  %-14s %s" % (name, text))


def run_sql(conn, sql):
    sql = sql.strip()
    while sql.endswith(";"):
        sql = sql[:-1].rstrip()
    cur = conn.execute(sql)
    cols = [d[0] for d in cur.description] if cur.description else []
    print_table(cols, cur.fetchall(), 20)


def repl(conn):
    print("自由查询：输入 SQL，空行执行；:q 退出")
    print("试试：SELECT * FROM orders LIMIT 5")
    print()
    lines = []
    while True:
        try:
            line = input("sql> " if not lines else "  -> ")
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not line.strip() and not lines:
            continue
        if not line.strip():
            sql = " ".join(lines)
            lines = []
            if sql.strip().lower() in (":q", "quit", "exit"):
                return
            try:
                run_sql(conn, sql)
            except sqlite3.Error as e:
                print("SQL 报错：%s" % e)
            print()
            continue
        lines.append(line)


def main():
    ap = argparse.ArgumentParser(description="数据库导览")
    ap.add_argument("table", nargs="?", help="表名")
    ap.add_argument("limit", nargs="?", type=int, default=5, help="显示几行，默认 5")
    ap.add_argument("--map", action="store_true", help="看表之间的关系")
    ap.add_argument("--sql", help="直接执行一条 SQL")
    ap.add_argument("-i", "--interactive", action="store_true", help="自由查询")
    args = ap.parse_args()

    conn = connect()
    if args.map:
        print(MAP_TEXT)
        return
    if args.sql:
        run_sql(conn, args.sql)
        return
    if args.interactive:
        repl(conn)
        return
    if args.table:
        show_table(conn, args.table, args.limit)
        return
    show_overview(conn)


if __name__ == "__main__":
    main()
