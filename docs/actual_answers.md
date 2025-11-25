1. Who are the customers in the database?

```sql
SELECT first_name, last_name, country 
FROM customer;
```
2. What is the email of customer 'John Doe'?
```sql
SELECT email 
FROM customer 
WHERE first_name = 'John' AND last_name = 'Doe';
```
3. How many invoices has customer 'Jane Smith' made?
```sql
SELECT COUNT(i.invoice_id) as invoice_count
FROM invoice i
JOIN customer c ON i.customer_id = c.customer_id
WHERE c.first_name = 'Jane' AND c.last_name = 'Smith';
```
4. Which genre has the most tracks?
```sql
SELECT g.name, COUNT(t.track_id) as track_count
FROM genre g
JOIN track t ON g.genre_id = t.genre_id
GROUP BY g.name
ORDER BY track_count DESC
LIMIT 1;
```
5. How much revenue has each artist generated?
```sql
SELECT ar.name, SUM(il.unit_price * il.quantity) as total_revenue
FROM artist ar
JOIN album al ON ar.artist_id = al.artist_id
JOIN track t ON al.album_id = t.album_id
JOIN invoice_line il ON t.track_id = il.track_id
GROUP BY ar.name
ORDER BY total_revenue DESC;
```
6. Who are the top 5 customers who spent the most?
```sql
SELECT c.first_name, c.last_name, SUM(i.total) as total_spent
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 5;
```
7. What is the total revenue per month in 2009?
```sql
SELECT strftime('%m', invoice_date) as month, SUM(total) as monthly_revenue
FROM invoice
WHERE strftime('%Y', invoice_date) = '2009'
GROUP BY month
ORDER BY month;
```