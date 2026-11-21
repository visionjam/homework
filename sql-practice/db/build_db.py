#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 SQL 实战练习库 db/shop.db（确定性数据，可重复运行）。

用法：
    python db/build_db.py

数据是脚本造出来的，不是真实业务数据；但表结构、状态流转、渠道/品类分布
都按电商常见形态设计，够用来练日常取数。
"""
import bisect
import datetime as dt
import os
import random
import sqlite3

SEED = 20261121
HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "shop.db")

START = dt.date(2026, 8, 1)
DAYS = 92

CITIES = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉", "西安", "南京", "长沙"]
CHANNELS = ["自然流量", "抖音", "小红书", "微信", "搜索"]
CHANNEL_W = [0.30, 0.18, 0.18, 0.22, 0.12]

CATS = {
    "数码": (299, 5999),
    "家居": (39, 899),
    "美妆": (59, 599),
    "服饰": (49, 499),
    "食品": (9, 129),
    "图书": (19, 99),
}
CAT_W = {"食品": 3.0, "美妆": 2.5, "服饰": 2.0, "家居": 1.5, "图书": 1.5, "数码": 1.0}

SCHEMA = """
CREATE TABLE users (
    user_id       INTEGER PRIMARY KEY,
    user_name     TEXT    NOT NULL,
    city          TEXT    NOT NULL,
    channel       TEXT    NOT NULL,   -- 注册渠道
    register_date TEXT    NOT NULL    -- YYYY-MM-DD
);

CREATE TABLE products (
    product_id   INTEGER PRIMARY KEY,
    product_name TEXT    NOT NULL,
    category     TEXT    NOT NULL,
    list_price   REAL    NOT NULL     -- 标价
);

CREATE TABLE orders (
    order_id   INTEGER PRIMARY KEY,
    user_id    INTEGER NOT NULL,
    order_date TEXT    NOT NULL,      -- YYYY-MM-DD
    status     TEXT    NOT NULL,      -- paid / refunded / cancelled
    channel    TEXT    NOT NULL,      -- 下单渠道
    pay_amount REAL    NOT NULL,      -- 实付（含运费；cancelled 为 0）
    created_at TEXT    NOT NULL
);

CREATE TABLE order_items (
    item_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id   INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity   INTEGER NOT NULL,
    unit_price REAL    NOT NULL       -- 成交单价（优惠已体现在这里）
);

CREATE TABLE events (
    event_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    INTEGER NOT NULL,
    event_date TEXT    NOT NULL,
    event_type TEXT    NOT NULL       -- view / add_cart / pay
);
"""

INDEXES = """
CREATE INDEX idx_orders_date      ON orders(order_date);
CREATE INDEX idx_orders_user      ON orders(user_id);
CREATE INDEX idx_items_order      ON order_items(order_id);
CREATE INDEX idx_items_product    ON order_items(product_id);
CREATE INDEX idx_events_user_date ON events(user_id, event_date);
CREATE INDEX idx_events_date      ON events(event_date);
"""


def build_users(rng):
    rows = []
    for uid in range(1, 3001):
        reg = dt.date(2026, 5, 1) + dt.timedelta(days=rng.randint(0, 182))
        rows.append((
            uid,
            "用户%04d" % uid,
            rng.choice(CITIES),
            rng.choices(CHANNELS, CHANNEL_W)[0],
            reg.isoformat(),
        ))
    return rows


def build_products(rng):
    rows = []
    names = list(CATS)
    for pid in range(1, 121):
        cat = names[(pid - 1) % len(names)]
        lo, hi = CATS[cat]
        rows.append((pid, "%s商品%03d" % (cat, pid), cat, round(rng.uniform(lo, hi), 2)))
    return rows


def build_orders(rng, users, products):
    reg = sorted((u[4], u[0]) for u in users)
    reg_keys = [r[0] for r in reg]
    reg_ids = [r[1] for r in reg]

    pids = [p[0] for p in products]
    price = {p[0]: p[3] for p in products}
    pcat = {p[0]: p[2] for p in products}
    pweight = [CAT_W[pcat[p]] for p in pids]

    orders, items = [], []
    oid = 0
    for i in range(DAYS):
        day = START + dt.timedelta(days=i)
        key = day.isoformat()
        t = i / (DAYS - 1)

        base = 150 + 90 * t
        wd = day.weekday()
        factor = 1.30 if wd >= 5 else (1.10 if wd == 4 else 1.0)
        n = max(30, int(base * factor * rng.gauss(1.0, 0.10)))

        cw = [0.30 - 0.10 * t, 0.18 + 0.16 * t, 0.18, 0.22 - 0.04 * t, 0.12 - 0.02 * t]
        pool = bisect.bisect_right(reg_keys, key)

        for _ in range(n):
            oid += 1
            uid = reg_ids[rng.randrange(pool)]
            status = rng.choices(("paid", "refunded", "cancelled"), (0.86, 0.08, 0.06))[0]
            channel = rng.choices(CHANNELS, cw)[0]

            k = rng.choices((1, 2, 3, 4), (0.55, 0.28, 0.12, 0.05))[0]
            chosen = set()
            while len(chosen) < k:
                chosen.add(rng.choices(pids, pweight)[0])

            total = 0.0
            for pid in sorted(chosen):
                qty = rng.choices((1, 2, 3), (0.80, 0.15, 0.05))[0]
                disc = rng.choice((0.0, 0.0, 0.0, 0.05, 0.10, 0.15, 0.20))
                unit = round(price[pid] * (1 - disc), 2)
                items.append((oid, pid, qty, unit))
                total += qty * unit

            total = round(total, 2)
            shipping = 0.0 if total >= 99 else 8.0
            pay = 0.0 if status == "cancelled" else round(total + shipping, 2)
            created = "%s %02d:%02d:%02d" % (key, rng.randrange(24), rng.randrange(60), rng.randrange(60))
            orders.append((oid, uid, key, status, channel, pay, created))

    return orders, items


def build_events(rng, users):
    reg = sorted((u[4], u[0]) for u in users)
    reg_keys = [r[0] for r in reg]
    reg_ids = [r[1] for r in reg]

    out = []
    for i in range(DAYS):
        day = START + dt.timedelta(days=i)
        key = day.isoformat()
        pool = bisect.bisect_right(reg_keys, key)
        n = max(80, int(rng.gauss(360, 35)))
        for _ in range(n):
            uid = reg_ids[rng.randrange(pool)]
            views = rng.choices((1, 2, 3, 4, 5, 6), (0.10, 0.18, 0.24, 0.22, 0.16, 0.10))[0]
            for _ in range(views):
                out.append((uid, key, "view"))
            if rng.random() < 0.35:
                out.append((uid, key, "add_cart"))
                if rng.random() < 0.50:
                    out.append((uid, key, "pay"))
    return out


def main():
    rng = random.Random(SEED)
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)

    users = build_users(rng)
    products = build_products(rng)
    orders, items = build_orders(rng, users, products)
    events = build_events(rng, users)

    conn.executemany("INSERT INTO users VALUES (?,?,?,?,?)", users)
    conn.executemany("INSERT INTO products VALUES (?,?,?,?)", products)
    conn.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?,?)", orders)
    conn.executemany(
        "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?,?,?,?)",
        items,
    )
    conn.executemany("INSERT INTO events (user_id, event_date, event_type) VALUES (?,?,?)", events)

    conn.executescript(INDEXES)
    conn.execute("ANALYZE")
    conn.commit()

    print("已生成:", DB_PATH)
    print("文件大小: %.1f MB" % (os.path.getsize(DB_PATH) / 1024 / 1024))
    for table in ("users", "products", "orders", "order_items", "events"):
        cnt = conn.execute("SELECT COUNT(*) FROM " + table).fetchone()[0]
        print("  %-12s %7d 行" % (table, cnt))
    print("订单状态分布:")
    for status, cnt in conn.execute(
        "SELECT status, COUNT(*) FROM orders GROUP BY status ORDER BY status"
    ):
        print("  %-10s %6d" % (status, cnt))
    conn.close()


if __name__ == "__main__":
    main()
