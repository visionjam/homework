# SQL 实战练习（数据分析向）

11 个电商业务案例，自带数据、参考答案和自动判分。目标是练到「拿到需求能独立出数」，
不是背语法。

## 快速开始

```powershell
cd "D:\dsh_dev\code learning\sql-practice"
python db/build_db.py        # 生成 db/shop.db（约 12 MB，已 gitignore，可随时重建）
python tools/quiz.py         # 看案例清单
python tools/quiz.py 3       # 做第 3 题（交互式，写完自动判分）
python tools/quiz.py 3 --answer   # 卡住了，直接看答案
python tools/verify.py       # 自检：11 个参考答案全部跑一遍
```

只依赖 Python 3.8+ 标准库（本机 `D:\Python314\python.exe` 直接可用），不用装数据库。

## 数据长什么样

练习库是一套简化电商模型，时间范围 **2026-08-01 ~ 2026-10-31**：

| 表 | 行数 | 一行代表什么 |
| --- | --- | --- |
| `users` | 3,000 | 一个注册用户（含城市、注册渠道、注册日期） |
| `products` | 120 | 一个商品（6 个品类，各有标价） |
| `orders` | 19,841 | 一笔订单（paid 17,084 / refunded 1,581 / cancelled 1,176） |
| `order_items` | 33,159 | 订单里的一行商品（数量 + 成交单价） |
| `events` | 132,136 | 一条用户行为（view / add_cart / pay） |

字段：

- `users`：`user_id, user_name, city, channel, register_date`
- `products`：`product_id, product_name, category, list_price`
- `orders`：`order_id, user_id, order_date, status, channel, pay_amount, created_at`
- `order_items`：`item_id, order_id, product_id, quantity, unit_price`
- `events`：`event_id, user_id, event_date, event_type`

### 口径约定（做之前先读一遍）

- **GMV** = `status = 'paid'` 的 `pay_amount` 合计，**含运费**。
- `refunded` 是「已付款后退款」，`pay_amount` 仍保留，但**不计入 GMV**。
- `cancelled` 是「下单未付款」，`pay_amount = 0`，但明细行还在（这是案例 09 的考点）。
- `order_items.unit_price` 是**成交单价**（优惠已体现在单价里），**不含运费**。
- `orders.channel` 是**下单渠道**，`users.channel` 是**注册渠道**，两个不是一回事。
- 日期字段都是 `'YYYY-MM-DD'` 文本，可以直接比较和排序。

## 11 个案例

| # | 主题 | 考察点 | 难度 | 建议用时 |
| --- | --- | --- | --- | --- |
| 01 | 经营日报：每日订单数与 GMV | 聚合 / 日期过滤 | ★ | 10 分钟 |
| 02 | 渠道效果对比 | GROUP BY / COUNT DISTINCT | ★ | 10 分钟 |
| 03 | 每个品类的销售额 Top3 商品 | 窗口函数 ROW_NUMBER | ★★ | 20 分钟 |
| 04 | 每个用户的首单 | 窗口去重（取每组第一条） | ★★ | 20 分钟 |
| 05 | 复购率 | 条件聚合 | ★★ | 15 分钟 |
| 06 | 9 月注册用户的次日留存 | 日期函数 / LEFT JOIN | ★★★ | 25 分钟 |
| 07 | 10 月转化漏斗 | 条件聚合 / 用户去重 | ★★★ | 25 分钟 |
| 08 | 每日 GMV 与日环比 | 窗口函数 LAG | ★★★ | 20 分钟 |
| 09 | 对账：订单金额 vs 明细金额 | 预聚合再 JOIN | ★★★ | 30 分钟 |
| 10 | 各品类退款率 | 多对多口径 / COUNT DISTINCT | ★★★ | 30 分钟 |
| 11 | RFM 用户分层 | NTILE / 综合 | ★★★★ | 40 分钟 |

**推荐顺序**：01 → 02 → 05 → 04 → 03 → 08 → 06 → 07 → 09 → 10 → 11。
先建立「过滤 + 聚合」的手感，再上窗口函数，最后碰口径最绕的对账和多对多。

## 怎么练（比刷题数量重要）

1. **先读题和口径，自己写**，别一上来按 `:a`。
2. 卡 10 分钟看提示；再卡 10 分钟看答案。
3. 看完答案**关掉重写一遍**——看懂和写出来是两回事。
4. 每题记一句「我卡在哪」（是语法？是口径？还是没想到窗口函数？），这比连刷 10 题有用。
5. 11 题全 PASS 后，把答案改写成 MySQL / Hive 版本，对照下面的方言表。

判分规则：行数、列数、数值（保留 4 位小数）都要对上；行顺序不同只提示、不算错。

## 参考答案里刻意教的 6 个套路

| 套路 | 用在哪 | 什么时候用 |
| --- | --- | --- |
| `ROW_NUMBER()` 取每组第一条 | 04 首单、03 TopN | 「每个用户/品类取最新/最大的一条」 |
| 先聚合再 JOIN | 09 对账 | 一对多关联后要 SUM，先想行数会不会翻倍 |
| 条件聚合 `SUM(CASE WHEN ...)` | 05 复购、07 漏斗 | 一行里同时算多个指标，避免多次扫表 |
| `LEFT JOIN` 后 `COUNT(右表列)` | 06 留存 | 分母是左表全量，分子才看右表命中 |
| `LAG()` | 08 环比 | 同环比、相邻行比较 |
| `NTILE(4)` | 11 RFM | 分位数分层，比手写阈值稳 |

## 方言对照（换成公司的库时看这个）

| 需求 | SQLite（本练习） | MySQL 8 | Hive / Spark SQL | PostgreSQL |
| --- | --- | --- | --- | --- |
| 日期加一天 | `date(d, '+1 day')` | `DATE_ADD(d, INTERVAL 1 DAY)` | `date_add(d, 1)` | `d + INTERVAL '1 day'` |
| 当前日期 | `date('now')` | `CURDATE()` | `current_date` | `CURRENT_DATE` |
| 按月截断 | `strftime('%Y-%m', d)` | `DATE_FORMAT(d, '%Y-%m')` | `substr(d, 1, 7)` | `date_trunc('month', d)` |
| 分页 | `LIMIT 10 OFFSET 20` | `LIMIT 20, 10` | `LIMIT 10` | `LIMIT 10 OFFSET 20` |
| 空值兜底 | `IFNULL / COALESCE` | `IFNULL` | `COALESCE / NVL` | `COALESCE` |
| 日期差（天） | `julianday(a) - julianday(b)` | `DATEDIFF(a, b)` | `datediff(a, b)` | `a::date - b::date` |
| 行号 / 排名 | `ROW_NUMBER()` | 8.0+ 支持 | 支持 | 支持 |
| 整数相除 | 取整（要乘 1.0） | 取整（要乘 1.0） | 返回小数 | 返回小数 |

## 常见坑清单

- **整数除法**：`SUM(a) / COUNT(*)` 在 SQLite/MySQL 里会取整，乘 `1.0` 或 `CAST`。
- **`COUNT(*)` vs `COUNT(col)`**：后者跳过 NULL。LEFT JOIN 后数错人基本都是这个。
- **NULL**：`= NULL` 永远不成立，用 `IS NULL`；`NOT IN` 的子查询里有 NULL 会让结果整体为空。
- **JOIN 放大**：一对多关联后 `SUM` 翻倍，先聚合再 JOIN，或 `COUNT(DISTINCT)`。
- **日期边界**：`BETWEEN '2026-10-01' AND '2026-10-31'` 对纯日期没问题，但带时分秒的字段会漏掉最后一天，改用 `>= ... AND < ...`。
- **窗口函数不能进 WHERE**：要在 CTE/子查询里算好再过滤。
- **口径先行**：去不去重、含不含退款、含不含测试账号、时区是哪个——写之前问清楚，比返工便宜。

## 学完自查

- [ ] 不看答案能写出「按周统计 GMV 并算环比」
- [ ] 能解释为什么 JOIN 明细后订单金额会翻倍
- [ ] 能说清 `COUNT(*)` 和 `COUNT(user_id)` 在 LEFT JOIN 后的区别
- [ ] 知道窗口函数为什么不能直接写在 WHERE 里
- [ ] 拿到一张新表，先看：行数、主键、时间范围、状态枚举、NULL 比例
- [ ] 能把任意一题的 SQL 改写成 MySQL 版本并说出改了哪里

## 目录结构

```text
sql-practice/
├── README.md            本文件
├── db/
│   ├── build_db.py      造数脚本（固定 seed，可重复生成）
│   └── shop.db          练习库（gitignore，跑 build_db.py 生成）
├── cases/
│   ├── cases.json       题目、口径、提示
│   ├── 01_daily_gmv.sql ~ 11_rfm.sql   参考答案
│   └── .progress        本地完成记录（gitignore）
└── tools/
    ├── quiz.py          出题 + 判分
    └── verify.py        自检全部答案
```

## 说明

数据是脚本生成的（`SEED = 20261121`），不是真实业务数据。金额分布、周末高峰、
抖音渠道占比随时间上升等特征都是**刻意造的**，方便练趋势和渠道分析；结论不要当真实业务判断。

`db/shop.db` 不进版本库，删了随时 `python db/build_db.py` 重建，结果完全一致。
