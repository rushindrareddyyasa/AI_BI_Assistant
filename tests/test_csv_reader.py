from ingestion.csv_reader import read_csv_file

data = read_csv_file("data/raw/sales.csv")

assert not data.empty
assert len(data.columns) == 10

print()

print("CSV reader test passed!")