-- 案例 04：每个用户的首单（只算 paid；同日多单取 order_id 最小）
WITH paid AS (
    SELECT o.*,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY order_date, order_id
           ) AS rn
    FROM orders o
    WHERE o.status = 'paid'
)
SELECT p.user_id,
       u.user_name,
       p.order_date                     AS first_date,
       p.order_id,
       ROUND(p.pay_amount, 2)           AS first_amount
FROM paid p
JOIN users u ON u.user_id = p.user_id
WHERE p.rn = 1
ORDER BY p.user_id;
