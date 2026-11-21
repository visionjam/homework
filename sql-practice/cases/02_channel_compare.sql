-- 案例 02：2026-09-01 ~ 2026-10-31 各下单渠道的经营表现
-- 口径：只算 paid；买家数按 user_id 去重；客单价 = GMV / 订单数
SELECT channel,
       COUNT(*)                             AS paid_orders,
       COUNT(DISTINCT user_id)              AS buyers,
       ROUND(SUM(pay_amount), 2)            AS gmv,
       ROUND(SUM(pay_amount) / COUNT(*), 2) AS aov
FROM orders
WHERE status = 'paid'
  AND order_date >= '2026-09-01'
  AND order_date <  '2026-11-01'
GROUP BY channel
ORDER BY gmv DESC;
