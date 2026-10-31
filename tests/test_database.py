import pandas as pd
from sqlalchemy import create_engine

from database.database import save_data


def test_save_data(tmp_path):

    database_path = tmp_path / "test.db"
    engine = create_engine(f"sqlite:///{database_path}")

    data = pd.DataFrame({
        "Product": ["Laptop", "Mouse"],
        "Quantity": [2, 3]
    })

    save_data(data, "sales", engine=engine)

    result = pd.read_sql("SELECT * FROM sales", engine)

    assert len(result) == 2
    assert list(result.columns) == ["Product", "Quantity"]
    assert result.iloc[0]["Product"] == "Laptop"

    engine.dispose()