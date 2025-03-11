-- This script lists the maximum temperature for each state, ordered by state name.

SELECT state, MAX(temperature) AS max_temperature
FROM city_temperature
GROUP BY state
ORDER BY state;
