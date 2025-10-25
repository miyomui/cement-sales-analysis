SELECT
    CAST(strftime('%Y', month) AS INTEGER) AS year,
    ROUND(SUM(production), 2) AS total_production,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(AVG(efficiency) * 100, 2) AS avg_efficiency,
    ROUND(AVG(fulfillment) * 100, 2) AS avg_fulfillment
FROM cement_sales
GROUP BY CAST(strftime('%Y', month) AS INTEGER)
ORDER BY year;
