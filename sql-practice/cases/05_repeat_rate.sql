-- 案例 05：复购率（paid 订单数 >= 2 的用户占比）
WITH per_user AS (
    SELECT user_id, COUNT(*) AS order_cnt
    FROM orders
    WHERE status = 'paid'
    GROUP BY user_id
)
SELECT COUNT(*)                                              AS buyers,
       SUM(CASE WHEN order_cnt >= 2 THEN 1 ELSE 0 END)        AS repeat_buyers,
       ROUND(1.0 * SUM(CASE WHEN order_cnt >= 2 THEN 1 ELSE 0 END)
             / COUNT(*), 4)                                   AS repeat_rate
FROM per_user;
