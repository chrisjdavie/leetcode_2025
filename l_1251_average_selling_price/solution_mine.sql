SELECT 
    product_id,
    CASE WHEN average_price IS NOT NULL THEN average_price
         ELSE 0
    END AS average_price
FROM (
    SELECT
        prices.product_id,
        ROUND((SUM(prices.price*unitssold.units)::float/SUM(unitssold.units))::numeric, 2) AS average_price
    FROM prices
    LEFT JOIN
        unitssold ON unitssold.product_id = prices.product_id
            AND unitssold.purchase_date >= prices.start_date
            AND unitssold.purchase_date <= prices.end_date
    GROUP BY prices.product_id
);
