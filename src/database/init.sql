CREATE USER 'admin_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_database.* TO 'admin_user'@'localhost';

CREATE DATABASE IF NOT EXISTS `pcc_db`;
USE pcc_db;

DROP TABLE IF EXISTS company, bot, trade, ticker;

create table `company` (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    is_blacklisted BOOLEAN DEFAULT FALSE,
);

create table `bot` (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    bot_status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP,
);

create table `trade` (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    exchange VARCHAR(15) NOT NULL,
    order_price INTEGER NOT NULL,
    trade_status VARCHAR(255) NOT NULL,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
);

create table `ticker` (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    ticker_price INTEGER NOT NULL,
    created_at TIMESTAMP,
);

-- create table `companies` (
--     id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     company_name VARCHAR(255) NOT NULL,
--     search_id VARCHAR(255) NOT NULL,
--     market_price DECIMAL(12, 2),
--     p_e_ratio DECIMAL(5, 2),
--     market_cap DECIMAL(12, 2),
--     divident_yield_percentage DECIMAL(5, 2),
--     quaterly_sales_in_crores DECIMAL(12, 2),
--     quaterly_sales_growth_percentage DECIMAL(5, 2),
--     return_on_capital_employed_percentage DECIMAL(6, 2),
--     tag VARCHAR(255) NOT NULL
-- );
-- insert into `companies` (company_name,search_id,market_price,p_e_ratio,market_cap,divident_yield_percentage,quaterly_sales_in_crores,quaterly_sales_growth_percentage,return_on_capital_employed_percentage,tag) values ('HDFC Bank','hdfc-bank-ltd',1636.9,18.72,1239557.41,1.16,51168.14,37.28,6.24,'Banking');
-- insert into `companies` (company_name,search_id,market_price,p_e_ratio,market_cap,divident_yield_percentage,quaterly_sales_in_crores,quaterly_sales_growth_percentage,return_on_capital_employed_percentage,tag) values ('ICICI Bank','icici-bank-ltd',990.5,18.6,693376.03,0.81,37105.89,41.85,6.35,'Banking');
-- insert into `companies` (company_name,search_id,market_price,p_e_ratio,market_cap,divident_yield_percentage,quaterly_sales_in_crores,quaterly_sales_growth_percentage,return_on_capital_employed_percentage,tag) values ('State Bank of India','state-bank-of-india',588.35,7.86,525212.69,1.92,101460.01,32.14,5.21,'Banking');
-- insert into `companies` (company_name,search_id,market_price,p_e_ratio,market_cap,divident_yield_percentage,quaterly_sales_in_crores,quaterly_sales_growth_percentage,return_on_capital_employed_percentage,tag) values ('Kotak Mahindra Bank','kotak-mahindra-bank-ltd',1811.2,22.06,359987.05,0.08,12868.93,40.42,6.86,'Banking');
-- insert into `companies` (company_name,search_id,market_price,p_e_ratio,market_cap,divident_yield_percentage,quaterly_sales_in_crores,quaterly_sales_growth_percentage,return_on_capital_employed_percentage,tag) values ('Axis Bank','axis-bank-ltd',1000.9,13.51,308447.72,0.1,26245.74,36.74,6.16,'Banking');
-- insert into `companies` (company_name,search_id,market_price,p_e_ratio,market_cap,divident_yield_percentage,quaterly_sales_in_crores,quaterly_sales_growth_percentage,return_on_capital_employed_percentage,tag) values ('IndusInd Bank','indusind-bank-ltd',1429.15,14.03,110979.5,0.98,10729.65,31.14,7.37,'Banking');
-- insert into `companies` (company_name,search_id,market_price,p_e_ratio,market_cap,divident_yield_percentage,quaterly_sales_in_crores,quaterly_sales_growth_percentage,return_on_capital_employed_percentage,tag) values ('Bank of Baroda','bank-of-baroda',199.95,5.94,103375.89,2.75,28002.54,39.68,5.17,'Banking');
