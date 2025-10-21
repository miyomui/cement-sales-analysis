USE cement_factory;

SELECT 
    DATE_FORMAT(month, '%Y-%m') AS period,
    ROUND(AVG(efficiency) * 100, 2) AS avg_efficiency,
    ROUND(AVG(fulfillment) * 100, 2) AS avg_fulfillment
FROM cement_sales
GROUP BY DATE_FORMAT(month, '%Y-%m')
ORDER BY period;

