WITH neighboring_cities as (SELECT 
"FSP_city".name as city, 
(
    SELECT "FSP_city".name 
    FROM "FSP_city"
    WHERE "FSP_road".next_city = "FSP_city".id
) as target_city,
"FSP_road".distance as distance
FROM "FSP_city" 
JOIN "FSP_road" on "FSP_road".previous_city = "FSP_city".id
WHERE "FSP_city".name = 'Renton')
SELECT *,
ABS(LEAD(distance) OVER(PARTITION BY city ORDER BY target_city) - distance) 
FROM neighboring_cities;