-- This script displays the top 3 cities' temperatures during July and August ordered by temperature (descending).

SELECT city, temperature
FROM city_temperature  -- Replace with the correct table name
WHERE month IN (7, 8)  -- July (7) and August (8)
ORDER BY temperature DESC
LIMIT 3;
