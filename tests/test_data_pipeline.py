from ingestion.csv_reader import read_csv_file
from ingestion.data_validator import validate_data
from ingestion.data_cleaner import clean_data
from database.database import save_data, engine
from sqlalchemy import text

# Read CSV
data = read_csv_file("data/raw/sales.csv")

# Validate data
errors = validate_data(data)
print("Validation errors:", errors)

# Clean data
cleaned_data, quarantined_data = clean_data(data)

# Save processed CSV files
cleaned_data.to_csv("data/processed/cleaned_sales.csv", index=False)
quarantined_data.to_csv("data/processed/quarantined_sales.csv", index=False)

# Save to database
save_data(cleaned_data, "sales")
save_data(quarantined_data, "quarantined_sales")

# Verify database
with engine.connect() as connection:
    sales_count = connection.execute(
        text("SELECT COUNT(*) FROM sales")
    ).scalar()

    quarantine_count = connection.execute(
        text("SELECT COUNT(*) FROM quarantined_sales")
    ).scalar()

print("Valid records:", sales_count)
print("Quarantined records:", quarantine_count)

print("Data pipeline completed!")