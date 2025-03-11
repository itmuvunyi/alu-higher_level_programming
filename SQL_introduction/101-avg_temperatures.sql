-- This script calculates the average temperature (Fahrenheit) by city
-- It orders the result by average temperature in descending order

SELECT city, AVG(temperature) AS average_temperature
FROM city_temperature
GROUP BY city
ORDER BY average_temperature DESC;
