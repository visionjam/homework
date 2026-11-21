-- 案例 07：2026 年 10 月「浏览 -> 加购 -> 支付」漏斗（按用户去重）
WITH per_user AS (
    SELECT user_id,
           MAX(CASE WHEN event_type = 'view'     THEN 1 ELSE 0 END) AS has_view,
           MAX(CASE WHEN event_type = 'add_cart' THEN 1 ELSE 0 END) AS has_cart,
           MAX(CASE WHEN event_type = 'pay'      THEN 1 ELSE 0 END) AS has_pay
    FROM events
    WHERE event_date >= '2026-10-01'
      AND event_date <  '2026-11-01'
    GROUP BY user_id
)
SELECT SUM(has_view)                                 AS view_users,
       SUM(has_cart)                                 AS cart_users,
       SUM(has_pay)                                  AS pay_users,
       ROUND(1.0 * SUM(has_cart) / SUM(has_view), 4) AS view_to_cart,
       ROUND(1.0 * SUM(has_pay)  / SUM(has_cart), 4) AS cart_to_pay,
       ROUND(1.0 * SUM(has_pay)  / SUM(has_view), 4) AS view_to_pay
FROM per_user;
