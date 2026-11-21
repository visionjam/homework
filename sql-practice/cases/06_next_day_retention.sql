-- 案例 06：2026 年 9 月注册用户的次日留存（次日有 paid 订单即留存）
-- 关键：LEFT JOIN 后必须 COUNT(rt.user_id)，COUNT(*) 会把未留存的人也算进去
WITH reg AS (
    SELECT user_id, register_date
    FROM users
    WHERE register_date >= '2026-09-01'
      AND register_date <  '2026-10-01'
),
retained AS (
    SELECT DISTINCT r.user_id
    FROM reg r
    JOIN orders o
      ON o.user_id     = r.user_id
     AND o.status      = 'paid'
     AND o.order_date  = date(r.register_date, '+1 day')
)
SELECT r.register_date                              AS reg_date,
       COUNT(*)                                     AS new_users,
       COUNT(rt.user_id)                            AS retained_users,
       ROUND(1.0 * COUNT(rt.user_id) / COUNT(*), 4) AS retention
FROM reg r
LEFT JOIN retained rt ON rt.user_id = r.user_id
GROUP BY r.register_date
ORDER BY reg_date;
