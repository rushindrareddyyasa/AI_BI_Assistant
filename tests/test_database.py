from ingestion.csv_reader import read_csv_file
from ingestion.data_cleaner import clean_data
from database.database import save_data

data = read_csv_file("data/raw/sales.csv")

cleaned_data, quarantined_data = clean_data(data)

save_data(cleaned_data, "sales")
save_data(quarantined_data, "quarantined_sales")