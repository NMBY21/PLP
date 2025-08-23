-- Question 1
-- Show the total payment amount for each payment date from payments table.
-- Sort by payment date in descending order and show only the top 5 latest dates.
SELECT 
    paymentDate, 
    SUM(amount) AS total_amount
FROM payments
GROUP BY paymentDate
ORDER BY paymentDate DESC
LIMIT 5;


-- Question 2
-- Find the average credit limit of each customer from customers table.
-- Display customer name, country, and the average credit limit.
SELECT 
    customerName, 
    country, 
    AVG(creditLimit) AS avg_credit_limit
FROM customers
GROUP BY customerName, country;


-- Question 3
-- Find the total price of products ordered from orderdetails table.
-- (total price = quantityOrdered * priceEach)
-- Display product code, quantity ordered, and total price for each product.
SELECT 
    productCode, 
    quantityOrdered, 
    SUM(quantityOrdered * priceEach) AS total_price
FROM orderdetails
GROUP BY productCode, quantityOrdered;


-- Question 4
-- Find the highest payment amount for each check number from payments table.
-- Display check number and highest amount paid.
SELECT 
    checkNumber, 
    MAX(amount) AS highest_payment
FROM payments
GROUP BY checkNumber;
