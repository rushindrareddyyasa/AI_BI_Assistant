from ingestion.csv_reader import read_csv_file
from ingestion.data_validator import validate_data

data = read_csv_file("data/raw/sales.csv")

errors = validate_data(data)

print("Validation errors:", errors)

print("\nRecords with missing unit price:")
print(data[data["Unit_price"].isnull()])

print("\nRecords with invalid quantity:")
print(data[data["Quantity"] <= 0])

print("\nTXN0051:")
print(data[data["Transaction_Id"] == "TXN0051"].to_string(index=False))

print("\nTXN0034:")
print(data[data["Transaction_Id"] == "TXN0034"].to_string(index=False))