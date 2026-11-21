-- 案例 08：2026-10-01 起每日 GMV 与日环比（dod = 今日/昨日 - 1）
WITH daily AS (
    SELECT order_date                 AS dt,
           ROUND(SUM(pay_amount), 2)  AS gmv
    FROM orders
    WHERE status = 'paid'
      AND order_date >= '2026-10-01'
    GROUP BY order_date
)
SELECT dt,
       gmv,
       LAG(gmv) OVER (ORDER BY dt)                     AS gmv_prev_day,
       ROUND(gmv - LAG(gmv) OVER (ORDER BY dt), 2)     AS diff,
       ROUND(gmv / LAG(gmv) OVER (ORDER BY dt) - 1, 4) AS dod
FROM daily
ORDER BY dt;
