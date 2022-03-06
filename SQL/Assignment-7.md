# Question-1
```SQL
SELECT ROUND(AVG(rental_rate), 3) FROM film;
```
# Question-2
```SQL
SELECT COUNT(title) FROM film
WHERE title ~~* 'C%';
```
# Question-3
```SQL
SELECT MAX(length) FROM film
WHERE rental_rate = 0.99;
```
# Question-4
```SQL
SELECT COUNT(DISTINCT(replacement_cost)) FROM film
WHERE length > 150;
```