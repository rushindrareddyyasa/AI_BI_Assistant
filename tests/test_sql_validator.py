from analytics.sql_validator import validate_query


queries = [
    "SELECT * FROM sales",
    "SELECT SUM(Quantity) FROM sales",
    "SELECT Product, SUM(Quantity) FROM sales GROUP BY Product",
    "DELETE FROM sales",
    "UPDATE sales SET Quantity = 0",
    "DROP TABLE sales",
    "INSERT INTO sales VALUES (1, 2)",
    "",
    "SELECT * FROM sales; DELETE FROM sales"
]


for query in queries:

    is_valid, message = validate_query(query)

    print("\nQuery:", query)
    print("Valid:", is_valid)
    print("Message:", message)