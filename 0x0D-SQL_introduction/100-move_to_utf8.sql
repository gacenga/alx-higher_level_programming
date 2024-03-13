-- choose database
USE hbtn_0c_0

-- converts database to UTF8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
