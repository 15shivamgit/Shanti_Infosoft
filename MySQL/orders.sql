show databases;
use shivamdb;
show tables;

CREATE TABLE orders ( 
order_id INT, customer_name VARCHAR(50), 
city VARCHAR(50), 
product VARCHAR(50), 
quantity INT, 
price DECIMAL(10,2), 
order_date DATE );

INSERT INTO orders VALUES
(1, 'Amit Sharma', 'Delhi', 'Laptop', 1, 55000.00, '2025-01-05'),
(2, 'Neha Verma', 'Mumbai', 'Mobile', 2, 20000.00, '2025-01-06'),
(3, 'Rohit Singh', 'Bhopal', 'Headphones', 3, 1500.00, '2025-01-07'),
(4, 'Priya Gupta', 'Indore', 'Tablet', 1, 18000.00, '2025-01-08'),
(5, 'Ankit Jain', 'Pune', 'Monitor', 2, 8000.00, '2025-01-09'),
(6, 'Sneha Kapoor', 'Chennai', 'Keyboard', 4, 1200.00, '2025-01-10'),
(7, 'Vikas Yadav', 'Lucknow', 'Mouse', 5, 700.00, '2025-01-11'),
(8, 'Kiran Patel', 'Ahmedabad', 'Printer', 1, 9500.00, '2025-01-12'),
(9, 'Rahul Mehta', 'Surat', 'Camera', 1, 25000.00, '2025-01-13'),
(10, 'Pooja Singh', 'Jaipur', 'Speaker', 2, 3000.00, '2025-01-14'),

(11, 'Deepak Kumar', 'Patna', 'Hard Disk', 2, 5000.00, '2025-01-15'),
(12, 'Riya Sen', 'Kolkata', 'Smart Watch', 1, 7000.00, '2025-01-16'),
(13, 'Manish Tiwari', 'Kanpur', 'Router', 3, 2500.00, '2025-01-17'),
(14, 'Alok Mishra', 'Varanasi', 'Projector', 1, 30000.00, '2025-01-18'),
(15, 'Sanya Malhotra', 'Gurgaon', 'Mobile', 1, 22000.00, '2025-01-19'),
(16, 'Nitin Arora', 'Noida', 'Laptop', 1, 60000.00, '2025-01-20'),
(17, 'Simran Kaur', 'Amritsar', 'Tablet', 2, 17000.00, '2025-01-21'),
(18, 'Ajay Chauhan', 'Agra', 'Camera', 1, 28000.00, '2025-01-22'),
(19, 'Rakesh Das', 'Ranchi', 'Monitor', 2, 9000.00, '2025-01-23'),
(20, 'Komal Shah', 'Vadodara', 'Keyboard', 3, 1100.00, '2025-01-24'),

(21, 'Arjun Nair', 'Kochi', 'Mouse', 4, 800.00, '2025-01-25'),
(22, 'Meera Iyer', 'Bangalore', 'Laptop', 1, 65000.00, '2025-01-26'),
(23, 'Suresh Reddy', 'Hyderabad', 'Printer', 1, 10000.00, '2025-01-27'),
(24, 'Anjali Desai', 'Nagpur', 'Speaker', 2, 3500.00, '2025-01-28'),
(25, 'Tarun Bhatt', 'Dehradun', 'Router', 2, 2700.00, '2025-01-29'),
(26, 'Nisha Yadav', 'Meerut', 'Smart Watch', 1, 7500.00, '2025-01-30'),
(27, 'Gaurav Saxena', 'Bareilly', 'Hard Disk', 2, 5200.00, '2025-02-01'),
(28, 'Isha Arora', 'Chandigarh', 'Tablet', 1, 20000.00, '2025-02-02'),
(29, 'Kunal Sharma', 'Jabalpur', 'Mobile', 2, 21000.00, '2025-02-03'),
(30, 'Divya Joshi', 'Udaipur', 'Camera', 1, 26000.00, '2025-02-04');


INSERT INTO orders VALUES
(31, 'Harsh Vardhan', 'Delhi', 'Laptop', 1, 58000.00, '2025-02-05'),
(32, 'Ayesha Khan', 'Mumbai', 'Mobile', 2, 24000.00, '2025-02-06'),
(33, 'Siddharth Roy', 'Kolkata', 'Tablet', 1, 19000.00, '2025-02-07'),
(34, 'Pankaj Tripathi', 'Patna', 'Monitor', 2, 8500.00, '2025-02-08'),
(35, 'Ritu Sharma', 'Jaipur', 'Smart Watch', 1, 7200.00, '2025-02-09'),
(36, 'Abhishek Dubey', 'Bhopal', 'Keyboard', 3, 1300.00, '2025-02-10'),
(37, 'Naveen Kumar', 'Hyderabad', 'Mouse', 4, 750.00, '2025-02-11'),
(38, 'Shreya Ghosh', 'Kolkata', 'Camera', 1, 27000.00, '2025-02-12'),
(39, 'Varun Malhotra', 'Chandigarh', 'Printer', 1, 9800.00, '2025-02-13'),
(40, 'Tanvi Joshi', 'Pune', 'Speaker', 2, 3200.00, '2025-02-14'),

(41, 'Mohit Agarwal', 'Lucknow', 'Hard Disk', 2, 5400.00, '2025-02-15'),
(42, 'Irfan Ali', 'Delhi', 'Router', 3, 2600.00, '2025-02-16'),
(43, 'Kavita Nair', 'Bangalore', 'Laptop', 1, 67000.00, '2025-02-17'),
(44, 'Ramesh Pillai', 'Chennai', 'Tablet', 2, 17500.00, '2025-02-18'),
(45, 'Anurag Sinha', 'Patna', 'Mobile', 1, 21000.00, '2025-02-19'),
(46, 'Preeti Verma', 'Indore', 'Monitor', 1, 8800.00, '2025-02-20'),
(47, 'Sahil Arora', 'Amritsar', 'Camera', 1, 29000.00, '2025-02-21'),
(48, 'Megha Kapoor', 'Delhi', 'Smart Watch', 2, 8000.00, '2025-02-22'),
(49, 'Rohit Kulkarni', 'Nagpur', 'Keyboard', 3, 1150.00, '2025-02-23'),
(50, 'Ananya Iyer', 'Bangalore', 'Mouse', 5, 900.00, '2025-02-24'),

(51, 'Deepika Singh', 'Varanasi', 'Printer', 1, 10200.00, '2025-02-25'),
(52, 'Karan Mehta', 'Ahmedabad', 'Speaker', 2, 3600.00, '2025-02-26'),
(53, 'Yash Thakur', 'Bhopal', 'Router', 2, 2800.00, '2025-02-27'),
(54, 'Neeraj Yadav', 'Meerut', 'Hard Disk', 2, 5300.00, '2025-02-28'),
(55, 'Swati Gupta', 'Noida', 'Laptop', 1, 62000.00, '2025-03-01'),
(56, 'Aditya Sharma', 'Delhi', 'Mobile', 2, 23000.00, '2025-03-02'),
(57, 'Ritika Jain', 'Udaipur', 'Tablet', 1, 19500.00, '2025-03-03'),
(58, 'Gaurav Verma', 'Kanpur', 'Monitor', 2, 8700.00, '2025-03-04'),
(59, 'Simran Kaur', 'Ludhiana', 'Smart Watch', 1, 7800.00, '2025-03-05'),
(60, 'Vivek Pandey', 'Gorakhpur', 'Camera', 1, 27500.00, '2025-03-06');








INSERT INTO orders VALUES
(101, 'Shivam', 'Patna', 'Laptop', 1, 55000.00, '2024-01-10'),
(102, 'Aman', 'Delhi', 'Mobile', 2, 20000.00, '2024-01-12'),
(103, 'Rohit', 'Mumbai', 'Tablet', 1, 15000.00, '2024-01-15'),
(104, 'Neha', 'Patna', 'Mobile', 3, 18000.00, '2024-01-18'),
(105, 'Ankit', 'Delhi', 'Laptop', 1, 60000.00, '2024-01-20'),
(106, 'Priya', 'Kolkata', 'Headphones', 2, 3000.00, '2024-01-22'),
(107, 'Rahul', 'Mumbai', 'Laptop', 1, 58000.00, '2024-01-25'),
(108, 'Pooja', 'Patna', 'Tablet', 2, 14000.00, '2024-01-28'),
(109, 'Suman', 'Delhi', 'Mobile', 1, 22000.00, '2024-02-01'),
(110, 'Karan', 'Kolkata', 'Laptop', 1, 52000.00, '2024-02-03'),

(111, 'Riya', 'Mumbai', 'Headphones', 3, 3500.00, '2024-02-05'),
(112, 'Amit', 'Patna', 'Mobile', 2, 21000.00, '2024-02-07'),
(113, 'Sneha', 'Delhi', 'Tablet', 1, 16000.00, '2024-02-10'),
(14, 'Vikas', 'Kolkata', 'Mobile', 2, 19000.00, '2024-02-12'),
(15, 'Deepak', 'Mumbai', 'Laptop', 1, 62000.00, '2024-02-15'),
(16, 'Anjali', 'Patna', 'Headphones', 2, 2800.00, '2024-02-18'),
(17, 'Manish', 'Delhi', 'Laptop', 1, 59000.00, '2024-02-20'),
(18, 'Kavita', 'Mumbai', 'Mobile', 2, 23000.00, '2024-02-22'),
(19, 'Rakesh', 'Kolkata', 'Tablet', 1, 17000.00, '2024-02-25'),
(20, 'Nisha', 'Patna', 'Laptop', 1, 54000.00, '2024-02-28'),

(21, 'Sanjay', 'Delhi', 'Headphones', 3, 3200.00, '2024-03-02'),
(22, 'Meena', 'Mumbai', 'Tablet', 2, 15000.00, '2024-03-05'),
(23, 'Alok', 'Kolkata', 'Laptop', 1, 61000.00, '2024-03-07'),
(24, 'Pankaj', 'Patna', 'Mobile', 2, 20000.00, '2024-03-10'),
(25, 'Rekha', 'Delhi', 'Laptop', 1, 63000.00, '2024-03-12'),
(26, 'Sunil', 'Mumbai', 'Headphones', 2, 3400.00, '2024-03-15'),
(27, 'Geeta', 'Kolkata', 'Mobile', 1, 21000.00, '2024-03-18'),
(28, 'Vivek', 'Patna', 'Tablet', 2, 15500.00, '2024-03-20'),
(29, 'Arjun', 'Delhi', 'Mobile', 3, 25000.00, '2024-03-22'),
(30, 'Komal', 'Mumbai', 'Laptop', 1, 64000.00, '2024-03-25');





select * from orders;



-- 🔥 Subquery Practice Set (Based on Your Data)
-- 🟢 Single Row Subquery
-- Find orders where price is greater than the average price of all orders.
select * from orders where price > ( select avg(price) from orders);

-- Find orders where quantity is less than the average quantity.
-- Find the order(s) having the maximum price.
-- Find customers who placed orders on the latest date.
-- Find the product with the minimum price.


-- 🟡 Multi-Row Subquery (IN, ANY, ALL)
-- Find customers who ordered products that 'Shivam' has ordered.
select * from orders where product in ( select product from orders where customer_name='amit sharma');

-- Find orders where price is greater than ANY price of 'Mobile'.
select * from orders where price > any ( select price from orders where product='mobile');
select * from orders where price >( select min(price) from orders where product='mobile');

-- Find orders where price is greater than ALL prices of 'Headphones'.
select * from orders where price > all ( select price from orders where product = 'headphones');

-- Find customers who ordered products available in 'Delhi'.
select customer_name from orders where product in ( select product from orders where city='delhi');

-- Find orders whose quantity matches any quantity ordered in 'Mumbai'.
select * from orders where quantity in ( select quantity from orders where city = 'mumbai');



-- 🔵 Correlated Subqueries
-- Find orders where price is greater than the average price of their city.
select * from orders o where price > (select avg(price) from orders where city = o.city);

-- Find orders where quantity is greater than the average quantity of that product.
select * from orders o where quantity > ( select avg(quantity) from orders where product = o.product);

SELECT *
FROM orders
WHERE price > (
    SELECT AVG(price)
    FROM orders
    WHERE city IN (
        SELECT city
        FROM orders
        WHERE quantity > 2
    )
);

-- Find orders where price is equal to the maximum price in that city.
select * from orders o where price = (select max(price) from orders where city = o.city);



-- Find customers whose order price is above their city’s average.
select * from orders o where price > (select avg(price) from orders where city = o.city);

-- Find orders where quantity is less than the average quantity of that city.
select * from orders o where quantity < (select avg(quantity) from orders where city = o.city);

-- 🟣 EXISTS / NOT EXISTS
-- Find customers who have placed at least one order with price greater than 60000.
-- Find customers who never ordered 'Headphones'.
-- Find products that have been ordered at least once in 'Patna'.
-- Find customers who have placed multiple orders (using EXISTS).
-- Find cities where no order has price less than 3000.
-- 🔴 Nested Subqueries (Advanced)
-- Find customers who placed orders with price greater than the average price of their city AND overall average price.
-- Find the second highest price using subquery.
-- Find customers who placed orders equal to the maximum price of their city.
-- Find products whose average price is greater than the overall average price.
-- Find cities whose average price is higher than the average price of 'Delhi'.
-- 🚀 Challenge Level (Interview 🔥)
-- Find customers who always order products with price above average.
-- Find products that were never ordered by 'Aman'.
-- Find the top 3 highest prices using only subqueries (no LIMIT).
-- Find customers who ordered all products available in the table.
-- Find customers whose every order has quantity greater than the average quantity.












-- Basic Level
-- Find all orders where the price is greater than the average price of all orders.
-- Find the customer(s) who placed the order with the maximum price.
select * from orders where price = (select max(price) from orders);

-- Find orders where the quantity is less than the average quantity.
select * from orders where quantity < (select avg(quantity) from orders);

-- Find the product with the minimum price.
select product from orders where price = (select min(price) from orders);

-- 🔹 Intermediate Level
-- Find all orders from the same city as a specific customer (e.g., 'John').
select * from orders where city = (select city from orders where customer_name = 'priya gupta');

-- Find customers who ordered the same product as a specific customer (e.g., 'Alice').
select * from orders where product = ( select product from orders where customer_name = 'priya gupta');

-- Find orders where the price is higher than the average price of their respective city.
select * from orders o where price > (select avg(price) from orders where city = o.city);

-- Find customers who have placed orders on the latest order date.
-- -- select * from orders order by order_date desc;
select * from orders where order_date = ( select max(order_date) from orders);

-- Find orders where quantity is greater than the average quantity of a specific product.
select * from orders where quantity > ( select avg(quantity) from orders where product = "camera");



-- 🔹 Advanced Level
-- Find customers who have never placed an order with price below the average price.
select * from orders where customer_name not in (
select customer_name from orders where price < 
(select avg(price) from orders));


-- Find products whose price is greater than the average price of all other products.
select * from orders o where price > (select avg(price) from orders where product != o.product);

-- Find the second highest price in the orders table.
-- Find customers who have placed more orders than the average number of orders per customer.
-- Find cities where the total order price is greater than the overall average total price of all cities.
-- Find customers who ordered only products that have a price greater than the average price.
-- 🔹 Challenge Questions (Hard 🔥)
-- Find customers whose every order has a price greater than the overall average price.
-- Find the product(s) that have never been ordered by a specific customer.
-- Find orders where the price is equal to the maximum price in that city.
-- Find customers who share the same city and have placed orders on the same date.
-- Find the top 3 highest priced orders using subqueries only (no LIMIT if possible).









