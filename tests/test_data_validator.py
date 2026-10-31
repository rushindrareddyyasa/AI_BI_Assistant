import pandas as pd

from ingestion.data_validator import validate_data


def test_missing_values():

    data = pd.DataFrame({
        "Transaction_Id": ["TXN001", "TXN002"],
        "Quantity": [2, 3],
        "Unit_price": [100, None]
    })

    errors = validate_data(data)

    assert "Missing values found" in errors


def test_duplicate_transaction_ids():

    data = pd.DataFrame({
        "Transaction_Id": ["TXN001", "TXN001"],
        "Quantity": [2, 3],
        "Unit_price": [100, 200]
    })

    errors = validate_data(data)

    assert "Duplicate transaction IDs found" in errors


def test_invalid_quantity():

    data = pd.DataFrame({
        "Transaction_Id": ["TXN001", "TXN002"],
        "Quantity": [2, 0],
        "Unit_price": [100, 200]
    })

    errors = validate_data(data)

    assert "Invalid quantity found" in errors


def test_invalid_unit_price():

    data = pd.DataFrame({
        "Transaction_Id": ["TXN001", "TXN002"],
        "Quantity": [2, 3],
        "Unit_price": [100, 0]
    })

    errors = validate_data(data)

    assert "Invalid unit price found" in errors