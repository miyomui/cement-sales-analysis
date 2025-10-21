USE cement_factory;

SELECT 
    DATE_FORMAT(month, '%Y-%m') AS period,
    ROUND(AVG(production - sales), 2) AS avg_production_gap
FROM cement_sales
GROUP BY DATE_FORMAT(month, '%Y-%m')
ORDER BY period;
