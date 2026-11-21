-- 案例 01：2026-10-01 ~ 2026-10-07 的每日经营日报
-- 口径：只统计 status='paid'；GMV = 实付金额合计（含运费）；客单价 = GMV / 订单数
SELECT order_date                              AS dt,
       COUNT(*)                                AS paid_orders,
       ROUND(SUM(pay_amount), 2)               AS gmv,
       ROUND(SUM(pay_amount) / COUNT(*), 2)    AS aov
FROM orders
WHERE status = 'paid'
  AND order_date BETWEEN '2026-10-01' AND '2026-10-07'
GROUP BY order_date
ORDER BY dt;
