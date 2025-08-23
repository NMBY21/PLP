-- Question 1 
-- Get firstName, lastName, email, and officeCode of all employees
-- Use INNER JOIN with offices on officeCode
SELECT 
    e.firstName, 
    e.lastName, 
    e.email, 
    e.officeCode
FROM employees e
INNER JOIN offices o
    ON e.officeCode = o.officeCode;


-- Question 2 
-- Get productName, productVendor, and productLine from products
-- Use LEFT JOIN with productlines on productLine
SELECT 
    p.productName, 
    p.productVendor, 
    pl.productLine
FROM products p
LEFT JOIN productlines pl
    ON p.productLine = pl.productLine;


-- Question 3 
-- Retrieve orderDate, shippedDate, status, and customerNumber for first 10 orders
-- Use RIGHT JOIN with customers and orders on customerNumber
SELECT 
    o.orderDate, 
    o.shippedDate, 
    o.status, 
    o.customerNumber
FROM customers c
RIGHT JOIN orders o
    ON c.customerNumber = o.customerNumber
LIMIT 10;
