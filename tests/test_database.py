import pandas as pd
from sqlalchemy import create_engine

import database.database as database_module


def test_save_data(tmp_path, monkeypatch):

    database_path = tmp_path / "test.db"
    test_engine = create_engine(f"sqlite:///{database_path}")

    # Replace the application engine with the temporary test engine
    monkeypatch.setattr(database_module, "engine", test_engine)

    data = pd.DataFrame({
        "Product": ["Laptop", "Mouse"],
        "Quantity": [2, 3]
    })

    database_module.save_data(data, "sales")

    result = pd.read_sql("SELECT * FROM sales", test_engine)

    assert len(result) == 2
    assert list(result.columns) == ["Product", "Quantity"]
    assert result.iloc[0]["Product"] == "Laptop"

    test_engine.dispose()