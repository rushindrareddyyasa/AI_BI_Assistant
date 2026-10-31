from ingestion.csv_reader import read_csv_file
from analytics.data_profiler import profile_dataset

# Read dataset
data = read_csv_file("data/raw/sales.csv")

# Generate dataset profile
profile = profile_dataset(data)

# Display profile
print("Total rows:", profile["total_rows"])
print("Total columns:", profile["total_columns"])

print("Numerical columns:", profile["numerical_columns"])
print("Categorical columns:", profile["categorical_columns"])
print("Date columns:", profile["date_columns"])
