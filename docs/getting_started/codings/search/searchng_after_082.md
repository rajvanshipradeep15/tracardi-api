# Searching (after 0.8.2)

Filtering in version 0.8.2 was simplified and has the following operations.

1. **Comparison Conditions:**
    - Basic comparison between a field and a value:
        - `fieldName > 42`
        - `product_price <= 100.50`

2. **Logical Operators:**
    - Combining conditions with `AND` and `OR`:
        - `sales > 1000 AND region = "North"`
        - `age >= 18 OR (gender = "Female" AND has_children = TRUE)`

3. **Grouping:**
    - Using parentheses to group conditions:
        - `(age < 30 AND income > 50000) OR (region = "West" AND product = "Widget")`

4. **NULL Conditions:**
    - Checking for NULL values:
        - `product_name IS NULL`

5. **Boolean Values:**
    - Using boolean values:
        - `is_active = TRUE`
        - `is_deleted = FALSE`

6. **Field Existence:**
    - Checking for the existence or non-existence of a field:
        - `customer_email EXISTS`
        - `employee_manager NOT EXISTS`

7. **Range Conditions:**
    - Comparing a field with a range:
        - `temperature BETWEEN 68 AND 72`
        - `price BETWEEN 10.99 AND 19.99`

8. **IS NULL Condition:**
    - Checking if a field is NULL:
        - `product_description IS NULL`

9. **Field Equality:**
    - Comparing two fields:
        - `order_total_amount = payment_total_amount`
        - `start_date < end_date`

10. **Array Conditions:**
    - Using arrays in conditions:
    - `categories IN ["Electronics", "Clothing", "Books"]`
    - `product_id NOT IN [101, 102, 103]`

11. **Field Functions:**
    - Applying functions to fields:
    - `DATE(order_date) = "2023-01-15"`
    - `UPPER(product_name) = "WIDGET"`

12. **Compound Value and Field Conditions:**
    - Using compound values and fields:
    - `category("Electronics") = price + tax`
    - `order_status("Shipped") = customer_name`

13. **Numeric and String Values:**
    - Basic numeric and string value conditions:
    - `quantity > 10`
    - `product_name = "Widget"`

14. **Time Conditions:**
    - Expressing time conditions:
    - `time_elapsed >= 2d` (greater than or equal to 2 days)
    - `duration < 1h` (less than 1 hour)

---
This documentation answer the following questions:

* How to search for profile, session, and events in Tracardi GUI
* How to search data in Tracardi?
* How does Tracardi's query parser work?
* What is a query condition?
* What is the syntax for searching, filtering in Tracardi?
