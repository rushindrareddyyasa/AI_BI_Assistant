from ingestion.csv_reader import read_csv_file
from analytics.schema_analyzer import analyze_schema
from llm.sql_generator import generate_sql


# Read dataset and analyze its schema
data = read_csv_file("data/raw/sales.csv")
schema = analyze_schema(data)


# Test different business questions
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

    print("-" * 60)