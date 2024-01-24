--Creating a view to return the difference between return date and rental date for each movie rental--
SELECT * FROM rental;

CREATE VIEW  rental_return_times AS
SELECT rental_id, customer_id,rental_date,
CASE
    WHEN (return_date IS NULL) THEN DATEDIFF(CURRENT_DATE,rental_date)
    ELSE DATEDIFF(return_date,rental_date) 
END AS duration
FROM rental;

--Creating a view to obtain the average movie return time of each customer--
CREATE VIEW customer_avg_return_times AS
SELECT customer_id,AVG(duration) AS avg_duration
FROM rental_return_times 
WHERE rental_date >= '2005-01-01' 
GROUP BY customer_id;

--Creating the query that feeds customer dashboard--
SELECT customer.*,
CASE
    WHEN customer_avg_return_times.avg_duration <= 7 THEN "GOOD"
    WHEN customer_avg_return_times.avg_duration > 7 AND customer_avg_return_times.avg_duration <= 30  THEN "FAIR"
    ELSE "BAD"
END AS customer_category
FROM customer
INNER JOIN customer_avg_return_times
ON customer.customer_id = customer_avg_return_times.customer_id;


--Creating a view from the query that feeds the customer dashboard--
CREATE VIEW customer_dashboard AS
SELECT customer.*,
CASE
    WHEN customer_avg_return_times.avg_duration <= 7 THEN "GOOD"
    WHEN customer_avg_return_times.avg_duration > 7 AND customer_avg_return_times.avg_duration <= 30  THEN "FAIR"
    ELSE "BAD"
END AS customer_category
FROM customer
INNER JOIN customer_avg_return_times
ON customer.customer_id = customer_avg_return_times.customer_id;

