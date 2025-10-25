SELECT
    strftime('%Y-%m', month) AS period,
    ROUND(AVG(production - sales), 2) AS avg_production_gap
FROM cement_sales
GROUP BY strftime('%Y-%m', month)
ORDER BY period;
