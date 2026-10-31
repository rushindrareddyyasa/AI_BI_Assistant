import pandas as pd

from database.database import read_only_engine
from analytics.schema_analyzer import analyze_schema
from analytics.query_executor import execute_query
from llm.sql_generator import generate_sql


# Read the currently uploaded dataset
data = pd.read_sql_query(
    "SELECT * FROM uploaded_data",
    read_only_engine
)

# Analyze its schema
schema = analyze_schema(data)


questions = [
    "What is the monthly revenue trend?",
    "How did revenue change between January 2025 and February 2025?"
]


for question in questions:

    print("\nQuestion:", question)

    # Generate SQL
    query = generate_sql(
        question,
        schema,
        "uploaded_data"
    )

    print("\nGenerated SQL:")
    print(query)

    if query.strip().upper() == "UNSUPPORTED":
        print("Question is unsupported.")
        continue

    # Execute SQL
    result = execute_query(query)

    print("\nTabular Result:")
    print(result.to_string(index=False))

    print("-" * 60)