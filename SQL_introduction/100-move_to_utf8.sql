-- This script converts the hbtn_0c_0 database to utf8mb4
-- It also converts the first_table table and the name field in first_table to utf8mb4
-- The database name is passed as an argument

-- Convert the database to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table first_table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the name field in first_table to utf8mb4
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
