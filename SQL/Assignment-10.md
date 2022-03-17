# Question-1
```SQL
SELECT city, country FROM city
LEFT JOIN country ON city.country_id = country.country_id;
```
# Question-2
```SQL
SELECT payment_id, first_name, last_name FROM payment
RIGHT JOIN customer ON payment.customer_id = customer.customer_id;
```
# Question-3
```SQL
SELECT rental.rental_id, customer.first_name, customer.last_name
FROM customer
FULL JOIN rental ON customer.customer_id = rental.customer_id;
```