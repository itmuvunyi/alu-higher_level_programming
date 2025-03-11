-- This script lists the top 3 cities with the highest temperatures in July and August
-- It orders the cities by temperature in descending order.

SELECT city, temperature, month
FROM city_temperature
WHERE month IN (7, 8)  -- 7 for July and 8 for August
ORDER BY temperature DESC
LIMIT 3;
