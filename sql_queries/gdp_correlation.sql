SELECT
    ROUND(
        (COUNT(*) * SUM(gdp * sales) - SUM(gdp) * SUM(sales)) /
        SQRT((COUNT(*) * SUM(gdp * gdp) - SUM(gdp) * SUM(gdp)) *
             (COUNT(*) * SUM(sales * sales) - SUM(sales) * SUM(sales))),
        3
    ) AS corr_gdp_sales,
    ROUND(
        (COUNT(*) * SUM(interestrate * sales) - SUM(interestrate) * SUM(sales)) /
        SQRT((COUNT(*) * SUM(interestrate * interestrate) - SUM(interestrate) * SUM(interestrate)) *
             (COUNT(*) * SUM(sales * sales) - SUM(sales) * SUM(sales))),
        3
    ) AS corr_interest_sales
FROM cement_sales;
