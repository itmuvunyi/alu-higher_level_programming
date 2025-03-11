-- This script calculates the average temperature by city, ordered by temperature (descending).

SELECT city, AVG(temperature) AS avg_temp
FROM city_temperature  -- Replace with the correct table name
GROUP BY city
ORDER BY avg_temp DESC;
