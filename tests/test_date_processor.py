from ingestion.csv_reader import read_csv_file
from analytics.date_processor import process_date_column

# Read dataset
data = read_csv_file("data/raw/sales.csv")

# Process date column
processed_data = process_date_column(data, "Order_date")

# Display date information
print("Original data type:", data["Order_date"].dtype)
print("Processed data type:", processed_data["Order_date"].dtype)

print("\nFirst 5 processed dates:")
print(processed_data["Order_date"].head())

print("\nInvalid dates:", processed_data["Order_date"].isnull().sum())

print("\nOriginal data type after processing:", data["Order_date"].dtype)