import pandas as pd

from ingestion.data_cleaner import clean_data


def test_missing_price_imputation():

    data = pd.DataFrame({
        "Product": ["Laptop", "Laptop", "Mouse"],
        "Quantity": [2, 3, 4],
        "Unit_price": [1000, None, 500]
    })

    cleaned_data, quarantined_data = clean_data(data)

    assert cleaned_data.loc[1, "Unit_price"] == 1000
    assert quarantined_data.empty


def test_invalid_quantity_quarantine():

    data = pd.DataFrame({
        "Product": ["Keyboard", "Mouse"],
        "Quantity": [0, 3],
        "Unit_price": [500, 300]
    })

    cleaned_data, quarantined_data = clean_data(data)

    assert len(cleaned_data) == 1
    assert len(quarantined_data) == 1
    assert quarantined_data.iloc[0]["Quantity"] == 0


def test_original_data_is_preserved():

    data = pd.DataFrame({
        "Product": ["Laptop", "Laptop"],
        "Quantity": [2, 3],
        "Unit_price": [1000, None]
    })

    original_data = data.copy(deep=True)

    clean_data(data)

    pd.testing.assert_frame_equal(data, original_data)