-- Last updated: 8/12/2026, 11:47:41 AM
SELECT
    stock_name,
    SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END) - SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END) AS capital_gain_loss
FROM
    Stocks
GROUP BY
    stock_name;