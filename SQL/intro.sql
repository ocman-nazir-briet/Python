show DATABASE;

CREATE DATABASE flow

use DATABASE flow;

DROP TABLE IF EXISTS Customer;

CREATE TABLE Customer(
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50)
);

ALTER TABLE Customer ADD phone VARCHAR(50);

INSERT INTO Customer (id, first_name, last_name, email, phone) VALUES
    (1, 'usman', 'nazir', '1usmannazirbareet@gmail.com', '03058495769'),
    (2, 'usman', 'nazir', '2usmannazirbareet@gmail.com', '13058495769'),
    (3, 'usman', 'nazir', '3usmannazirbareet@gmail.com', '23058495769');


SELECT * FROM Customer;


DROP TABLE if exists Orders;
CREATE TABLE Orders (
    id INT PRIMARY KEY,
    price INT,
    unit VARCHAR(10),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(id)
);


INSERT INTO Orders(id, price, unit, customer_id) VALUES
(1,420, 'US $', 1),
(2,540, 'US $', 2),
(3,250, 'US $', 2)



-- Joins --
SELECT Orders.id, Orders.price, Orders.unit, Customer.first_name, Customer.last_name
FROM Orders
INNER JOIN Customer ON Orders.customer_id = Customer.id;


SELECT Orders.id, Orders.price, Orders.unit, Customer.first_name, Customer.last_name
FROM Orders
LEFT JOIN Customer ON Orders.customer_id = Customer.id;


SELECT Orders.id, Orders.price, Orders.unit, Customer.first_name, Customer.last_name
FROM Orders
RIGHT JOIN Customer ON Orders.customer_id = Customer.id;


SELECT Orders.id, Orders.price, Orders.unit, Customer.first_name, Customer.last_name
FROM Orders
FULL JOIN Customer ON Orders.customer_id = Customer.id;


SELECT Orders.id, Orders.price, Orders.unit, Customer.first_name, Customer.last_name
FROM Orders
CROSS JOIN Customer;



