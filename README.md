# bot

create database database name character set utf8 collate utf8_unicode_ci;
CREATE USER 'admin1234'@'localhost' IDENTIFIED BY 'admin1234';
GRANT ALL PRIVILEGES ON *.* TO 'admin1234'@'localhost';
FLUSH PRIVILEGES;

// To import database from local *.sql file:
mysql -u user_name -p database_name < dump.sql

//To export database to local *.sql file:
mysqldump -u user_name -p database_name > dump.sql
