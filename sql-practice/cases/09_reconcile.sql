-- 案例 09：按状态核对「订单实付」与「明细商品金额」
-- 关键：先把明细按订单聚合成一行，再 JOIN，否则 pay_amount 会被明细行数放大
WITH item_sum AS (
    SELECT order_id,
           SUM(quantity * unit_price) AS items_amount
    FROM order_items
    GROUP BY order_id
)
SELECT o.status,
       COUNT(*)                                     AS orders,
       ROUND(SUM(o.pay_amount), 2)                  AS pay_total,
       ROUND(SUM(i.items_amount), 2)                AS items_total,
       ROUND(SUM(o.pay_amount - i.items_amount), 2) AS diff
FROM orders o
LEFT JOIN item_sum i ON i.order_id = o.order_id
GROUP BY o.status
ORDER BY o.status;
