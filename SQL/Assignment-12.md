# Question-1
```SQL
SELECT COUNT(*) FROM film
WHERE length > (SELECT AVG(length) FROM film);
```
# Question-2
```SQL
SELECT COUNT(*) FROM film
WHERE rental_rate = (SELECT MAX(rental_rate) FROM film);
```
# Question-3
```SQL
SELECT * FROM film
WHERE rental_rate = ANY (SELECT MIN(rental_rate) FROM film)
AND replacement_cost = ANY (SELECT MIN(replacement_cost) FROM film);
```
# Question-4
```SQL
SELECT customer_id, COUNT(payment_id) FROM payment
GROUP BY customer_id ORDER BY COUNT(payment_id) DESC;
```