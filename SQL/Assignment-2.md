# Question-1
```SQL
SELECT * FROM film
WHERE replacement_cost BETWEEN 12.99 AND 16.99;
```
# Question-2
```SQL
SELECT * FROM actor
WHERE first_name IN ('Penelope', 'Nick', 'Ed');
```
# Question-3
```SQL
SELECT * FROM film
WHERE rental_rate IN (0.99,2.99,4.99) AND replacement_cost IN (12.99,15.99,28.99);
```