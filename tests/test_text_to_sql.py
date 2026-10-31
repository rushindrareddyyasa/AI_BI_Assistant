from ingestion.csv_reader import read_csv_file
from analytics.schema_analyzer import analyze_schema
from llm.sql_generator import generate_sql
from analytics.query_executor import execute_query


data = read_csv_file("data/raw/sales.csv")
schema = analyze_schema(data)

questions = [
    "Which product has the highest total revenue?",
    "What is the average quantity sold in each region?",
    "Show total revenue for each sales channel."
]

for question in questions:

    print("\nQuestion:", question)

    query = generate_sql(question, schema)

    print("\nGenerated SQL:")
    print(query)

    result = execute_query(query)

    print("\nResult:")
    print(result.to_string(index=False))

    print("-" * 60)