-- 案例 10：各品类退款率
-- 口径：分母 = 该品类 paid + refunded 订单数（去重）；分子 = refunded 订单数（去重）
WITH cat AS (
    SELECT p.category,
           COUNT(DISTINCT CASE WHEN o.status IN ('paid', 'refunded')
                               THEN o.order_id END) AS paid_orders,
           COUNT(DISTINCT CASE WHEN o.status = 'refunded'
                               THEN o.order_id END) AS refund_orders
    FROM orders o
    JOIN order_items oi ON oi.order_id  = o.order_id
    JOIN products   p   ON p.product_id = oi.product_id
    GROUP BY p.category
)
SELECT category,
       paid_orders,
       refund_orders,
       ROUND(1.0 * refund_orders / paid_orders, 4) AS refund_rate
FROM cat
ORDER BY refund_rate DESC;
