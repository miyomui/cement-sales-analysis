USE cement_factory;

SELECT 
    month,
    production,
    sales,
    ROUND(efficiency * 100, 2) AS efficiency_percent
FROM cement_sales
WHERE efficiency < 0.9
ORDER BY efficiency ASC
LIMIT 10;
