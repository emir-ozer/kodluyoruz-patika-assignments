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
SELECT payment.customer_id, first_name, last_name, COUNT(payment.customer_id) FROM payment
FULL JOIN customer ON customer.customer_id = payment.customer_id
GROUP BY payment.customer_id, customer.first_name, customer.last_name
ORDER BY COUNT(payment.customer_id) DESC;
```
