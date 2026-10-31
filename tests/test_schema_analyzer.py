from ingestion.csv_reader import read_csv_file
from analytics.schema_analyzer import analyze_schema

# Read the dataset
data = read_csv_file("data/raw/sales.csv")

# Analyze dataset structure
schema = analyze_schema(data)

# Display schema information
for column, details in schema.items():

    print("Data type:", details["data_type"])
    print("Missing values:", details["missing_values"])
    print("Unique values:", details["unique_values"])
    print("Is numeric:", details["is_numeric"])
    print("Is date:", details["is_date"])