# Question-1
```SQL
(SELECT first_name FROM actor)
UNION
(SELECT first_name FROM customer);
```
# Question-2
```SQL
(SELECT first_name FROM actor)
INTERSECT
(SELECT first_name FROM customer);
```
# Question-3
```SQL
(SELECT first_name FROM actor)
EXCEPT
(SELECT first_name FROM customer);
```
# Question-4
```SQL
(SELECT first_name FROM actor)
UNION ALL
(SELECT first_name FROM customer);
```
```SQL
(SELECT first_name FROM actor)
INTERSECT ALL
(SELECT first_name FROM customer);
```
```SQL
(SELECT first_name FROM actor)
EXCEPT ALL
(SELECT first_name FROM customer);
```