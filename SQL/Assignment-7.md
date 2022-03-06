# Question-1
```SQL
SELECT rating FROM film
GROUP BY rating;
```
# Question-2
```SQL
SELECT replacement_cost, COUNT(*) FROM film
GROUP BY replacement_cost
HAVING COUNT(*) > 50
ORDER BY COUNT(*);
```
# Question-3
```SQL
SELECT store_id, COUNT(*) FROM customer
GROUP BY store_id;
```
# Question-4
```SQL
SELECT country_id, COUNT(*) FROM city
GROUP BY country_id
ORDER BY COUNT(*) DESC
LIMIT 1;
```