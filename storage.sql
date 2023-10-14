-- Create Table Script
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Insert Data Script
INSERT INTO users (username, email) VALUES
    ('john_doe', 'john@example.com'),
    ('jane_doe', 'jane@example.com');

INSERT INTO products (name, price) VALUES
    ('Product A', 19.99),
    ('Product B', 29.99);

-- Update Data Script
UPDATE products
SET price = 24.99
WHERE name = 'Product A';

-- Delete Data Script
DELETE FROM users
WHERE username = 'john_doe';

-- Select Data Script
SELECT * FROM products;

-- SQL Script for Database Operation (Stored Procedure)
DELIMITER //
CREATE PROCEDURE GetProductCount()
BEGIN
    SELECT COUNT(*) AS product_count FROM products;
END //
DELIMITER ;
