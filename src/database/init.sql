CREATE DATABASE IF NOT EXISTS `pcc_db`;
USE pcc_db;

CREATE USER IF NOT EXISTS 'pcc_user'@'localhost' IDENTIFIED BY 'RaJcnH5Hw7Vxq';
GRANT ALL PRIVILEGES ON pcc_db.* TO 'pcc_user'@'localhost';

DROP TABLE IF EXISTS company, bot, trade, ticker;

-- create table `company` (
--     id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     exchage VARCHAR(255) NOT NULL,
--     is_blacklisted BOOLEAN DEFAULT FALSE
-- );

-- create table `bot` (
--     id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     bot_status VARCHAR(50) NOT NULL,
--     created_at TIMESTAMP
-- );

-- create table `trade` (
--     id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     company_name VARCHAR(255) NOT NULL,
--     order_price INTEGER NOT NULL,
--     trade_status VARCHAR(255) NOT NULL,
--     created_at TIMESTAMP,
--     updated_at TIMESTAMP
-- );

-- create table `ticker` (
--     id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     company_name VARCHAR(255) NOT NULL,
--     ticker_price INTEGER NOT NULL,
--     created_at TIMESTAMP
-- );
