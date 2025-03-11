-- Select the correct database
USE hbtn_0c_0;

-- Convert the database to UTF8 (utf8mb4)
ALTER DATABASE hbtn_0c_0
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

-- Convert the table first_table to UTF8 (utf8mb4)
ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Convert the 'name' column of the first_table to UTF8 (utf8mb4)
ALTER TABLE first_table
  MODIFY COLUMN name VARCHAR(256)
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
