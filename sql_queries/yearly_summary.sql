USE cement_factory;

SELECT 
    YEAR(month) AS year,
    ROUND(SUM(production), 2) AS total_production,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(AVG(efficiency) * 100, 2) AS avg_efficiency,
    ROUND(AVG(fulfillment) * 100, 2) AS avg_fulfillment
FROM cement_sales
GROUP BY YEAR(month)
ORDER BY year;
