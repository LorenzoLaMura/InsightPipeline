-- Create the ecommerce database if it doesn't exist
CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

-- Create the category table
CREATE TABLE IF NOT EXISTS category (
    category_id INT PRIMARY KEY,
    category_name TEXT,
    category_description TEXT
);

-- Create the seller table
CREATE TABLE IF NOT EXISTS seller (
    seller_id INT PRIMARY KEY,
    seller_name TEXT,
    seller_description TEXT
);

-- Create the product table, referencing category and seller tables
CREATE TABLE IF NOT EXISTS product (
    product_id INT PRIMARY KEY,
    category_id INT,
    seller_id INT,
    product_name TEXT,
    product_price DOUBLE,
    description TEXT,
    FOREIGN KEY (category_id) REFERENCES category(category_id),
    FOREIGN KEY (seller_id) REFERENCES seller(seller_id)
);

-- Insert sample data into category table
INSERT INTO category (category_id, category_name, category_description) VALUES
(1, 'Electronics', 'Devices and gadgets'),
(2, 'Books', 'Various types of books'),
(3, 'Clothing', 'Apparel and accessories'),
(4, 'Furniture', 'Home and office furniture'),
(5, 'Toys', 'Toys and games for children'),
(6, 'Sports', 'Sports equipment and apparel'),
(7, 'Beauty', 'Beauty and personal care products'),
(8, 'Automotive', 'Car accessories and parts'),
(9, 'Home Appliances', 'Various home appliances'),
(10, 'Groceries', 'Daily groceries and food items'),
(11, 'Jewelry', 'Jewelry and accessories'),
(12, 'Garden', 'Gardening tools and accessories'),
(13, 'Music', 'Musical instruments and accessories');

-- Insert sample data into seller table
INSERT INTO seller (seller_id, seller_name, seller_description) VALUES
(1, 'TechWorld', 'Electronics and gadgets seller'),
(2, 'BookBarn', 'Book seller'),
(3, 'FashionHub', 'Clothing and accessories seller'),
(4, 'HomeEssentials', 'Furniture and home accessories seller'),
(5, 'ToyLand', 'Toys and games seller'),
(6, 'SportsGear', 'Sports equipment seller'),
(7, 'BeautyStore', 'Beauty and personal care products seller'),
(8, 'AutoParts', 'Automotive parts seller');

-- Insert sample data into product table
INSERT INTO product (product_id, category_id, seller_id, product_name, product_price, description) VALUES
(1, 1, 1, 'Smartphone', 699.99, 'Latest model smartphone with 5G support'),
(2, 1, 1, 'Laptop', 1299.99, 'High performance laptop for professionals'),
(3, 2, 2, 'Fiction Book', 19.99, 'A popular fiction book'),
(4, 2, 2, 'Non-fiction Book', 29.99, 'A well-known non-fiction book'),
(5, 3, 3, 'T-shirt', 14.99, 'Comfortable cotton t-shirt'),
(6, 3, 3, 'Jeans', 39.99, 'Stylish denim jeans'),
(7, 4, 4, 'Sofa', 499.99, 'Comfortable living room sofa'),
(8, 4, 4, 'Office Chair', 149.99, 'Ergonomic office chair'),
(9, 5, 5, 'Action Figure', 24.99, 'Popular action figure for kids'),
(10, 5, 5, 'Board Game', 39.99, 'Fun board game for family'),
(11, 6, 6, 'Basketball', 29.99, 'Professional basketball'),
(12, 6, 6, 'Tennis Racket', 89.99, 'High-quality tennis racket'),
(13, 7, 7, 'Lipstick', 19.99, 'Long-lasting lipstick'),
(14, 7, 7, 'Shampoo', 12.99, 'Herbal shampoo for all hair types'),
(15, 8, 8, 'Car Battery', 99.99, 'High performance car battery'),
(16, 8, 8, 'Oil Filter', 14.99, 'Oil filter for various car models'),
(17, 9, 1, 'Microwave', 89.99, 'Compact microwave oven'),
(18, 9, 1, 'Refrigerator', 499.99, 'Energy-efficient refrigerator'),
(19, 10, 2, 'Pasta', 2.99, 'Organic pasta'),
(20, 10, 2, 'Olive Oil', 9.99, 'Extra virgin olive oil'),
(21, 11, 3, 'Necklace', 49.99, 'Elegant gold necklace'),
(22, 11, 3, 'Earrings', 29.99, 'Stylish earrings'),
(23, 12, 4, 'Lawn Mower', 199.99, 'Electric lawn mower'),
(24, 12, 4, 'Garden Hose', 24.99, 'Durable garden hose'),
(25, 13, 5, 'Guitar', 199.99, 'Acoustic guitar'),
(26, 13, 5, 'Drum Set', 499.99, 'Complete drum set');