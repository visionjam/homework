-- 案例 11：RFM 分层（观察截止 2026-10-31，只算 paid）
-- R：距今天数（越小越近期）；F：订单数；M：金额。三项各 NTILE(4) 分四档
WITH base AS (
    SELECT user_id,
           MAX(order_date) AS last_order_date,
           COUNT(*)        AS freq,
           SUM(pay_amount) AS amount
    FROM orders
    WHERE status = 'paid'
    GROUP BY user_id
),
scored AS (
    SELECT user_id,
           last_order_date,
           CAST(julianday('2026-10-31') - julianday(last_order_date) AS INTEGER) AS recency_days,
           freq,
           ROUND(amount, 2)                                  AS amount,
           NTILE(4) OVER (ORDER BY last_order_date DESC)      AS r_score,
           NTILE(4) OVER (ORDER BY freq ASC, user_id)         AS f_score,
           NTILE(4) OVER (ORDER BY amount ASC, user_id)       AS m_score
    FROM base
)
SELECT user_id, last_order_date, recency_days, freq, amount,
       r_score, f_score, m_score,
       CASE
           WHEN r_score <= 2 AND f_score >= 4 THEN '高价值'
           WHEN r_score <= 2 AND f_score <= 2 THEN '新客/低频'
           WHEN r_score >= 3 AND f_score >= 4 THEN '流失预警'
           WHEN r_score >= 3 AND f_score <= 2 THEN '沉睡'
           ELSE '一般'
       END AS segment
FROM scored
ORDER BY amount DESC
LIMIT 20;
