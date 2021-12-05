# Question-1
```SQL
SELECT title, description FROM film;
```
# Question-2
```SQL
SELECT * FROM film
WHERE length > 60 AND length < 75;
```
# Question-3
```SQL
SELECT * FROM film
WHERE rental_rate = 0.99 AND (replacement_cost = 12.99 OR replacement_cost = 28.99);
```
# Question-4
```SQL
SELECT last_name FROM customer
WHERE first_name = 'Mary';
```
# Question-5
```SQL
SELECT * FROM film
WHERE NOT length >= 50 AND NOT (rental_rate = 2.99 OR rental_rate = 4.99);
```