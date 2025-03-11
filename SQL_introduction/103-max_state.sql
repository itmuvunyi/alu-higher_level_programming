-- This script displays the max temperature for each state, ordered by state name.

SELECT state, MAX(temperature) AS max_temp
FROM city_temperature  -- Replace with the actual table name if necessary
GROUP BY state
ORDER BY state;
