from analytics.query_executor import execute_query
from sqlalchemy import text
from database.database import read_only_engine

# Test: SQLite read-only protection
# Test: Filtered analysis

result = execute_query(
    """
    SELECT *
    FROM sales
    WHERE Region = 'North'
    """
)

print("\nNorth Region Transactions:")
print(result)