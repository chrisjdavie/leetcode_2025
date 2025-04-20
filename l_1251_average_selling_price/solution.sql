-- most popular submission, better than mine
SELECT
    prices.product_id,
    CASE
        WHEN SUM(unitssold.units) IS NULL THEN 0
        ELSE ROUND(SUM(prices.price*unitssold.units)/SUM(unitssold.units)::numeric, 2)
    END AS average_price
FROM prices
LEFT JOIN unitssold ON prices.product_id = unitssold.product_id
                    AND unitssold.purchase_date BETWEEN prices.start_date AND prices.end_date
GROUP BY prices.product_id;
