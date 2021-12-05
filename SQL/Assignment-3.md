# Question-1
```SQL
SELECT * FROM country
WHERE country LIKE ('A%a');
```
# Question-2
```SQL
SELECT * FROM country
WHERE country ~~ ('_____%n');
```
# Question-3
```SQL
SELECT * FROM film
WHERE title ILIKE ('%t%t%t%t%');
```
# Question-4
```SQL
SELECT * FROM film
WHERE title LIKE ('C%') AND length > 90 AND rental_rate = 2.99;
```