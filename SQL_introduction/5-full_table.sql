-- This script prints the full description of the table first_table
-- It queries the information_schema to get the structure of the table
-- The database name is passed as an argument

-- Query the information_schema to get the table structure
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';
