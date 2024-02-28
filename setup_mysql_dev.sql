-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS q_dev_db;
CREATE USER IF NOT EXISTS 'q_dev'@'localhost' IDENTIFIED BY 'q_dev_pwd';
GRANT ALL PRIVILEGES ON `q_dev_db`.* TO 'q_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'q_dev'@'localhost';
FLUSH PRIVILEGES;
