-- 案例 03：每个品类销售额 Top3 的商品（2026-08-01 ~ 2026-10-31，只算 paid）
-- 关键：先在商品粒度聚合，再用窗口函数排名
WITH item_sales AS (
    SELECT p.category,
           p.product_id,
           p.product_name,
           SUM(oi.quantity)                           AS qty,
           ROUND(SUM(oi.quantity * oi.unit_price), 2) AS amount
    FROM order_items oi
    JOIN orders   o ON o.order_id   = oi.order_id AND o.status = 'paid'
    JOIN products p ON p.product_id = oi.product_id
    GROUP BY p.category, p.product_id, p.product_name
),
ranked AS (
    SELECT item_sales.*,
           ROW_NUMBER() OVER (
               PARTITION BY category
               ORDER BY amount DESC, product_id
           ) AS rn
    FROM item_sales
)
SELECT category, rn, product_name, qty, amount
FROM ranked
WHERE rn <= 3
ORDER BY category, rn;
