-- reates the database hbtn_0d_2 and the user user_0d_2
-- create database
CREATE DATABASE hbtn_0d_2;

-- create user
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant select privilege
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
