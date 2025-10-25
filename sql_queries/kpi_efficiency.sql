SELECT
    strftime('%Y-%m', month) AS period,
    ROUND(AVG(efficiency) * 100, 2) AS avg_efficiency,
    ROUND(AVG(fulfillment) * 100, 2) AS avg_fulfillment
FROM cement_sales
GROUP BY strftime('%Y-%m', month)
ORDER BY period;

