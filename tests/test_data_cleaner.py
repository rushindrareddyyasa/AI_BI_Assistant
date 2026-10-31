from ingestion.csv_reader import read_csv_file
from ingestion.data_cleaner import clean_data

data = read_csv_file("data/raw/sales.csv")

cleaned_data, quarantined_data = clean_data(data)

print("Original records:", len(data))
print("Cleaned records:", len(cleaned_data))
print("Quarantined records:", len(quarantined_data))

print("\nImputed transaction:")
print(cleaned_data[cleaned_data["Transaction_Id"] == "TXN0051"])

print("\nQuarantined transaction:")
print(quarantined_data)

cleaned_data.to_csv("data/processed/cleaned_sales.csv", index=False)

quarantined_data.to_csv("data/processed/quarantined_sales.csv", index=False)

print("Processed files saved successfully!")
