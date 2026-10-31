import pandas as pd

from ingestion.csv_reader import read_csv_file


def test_read_csv_file(tmp_path):

    # Create a temporary CSV file
    csv_file = tmp_path / "test.csv"

    data = pd.DataFrame({
        "Product": ["Laptop", "Keyboard"],
        "Quantity": [2, 5]
    })

    data.to_csv(csv_file, index=False)

    # Read the CSV file
    result = read_csv_file(csv_file)

    # Verify the result
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert list(result.columns) == ["Product", "Quantity"]
    assert result.iloc[0]["Product"] == "Laptop"