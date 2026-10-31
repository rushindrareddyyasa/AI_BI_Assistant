import pandas as pd
import pytest
from sqlalchemy import create_engine

import analytics.query_executor as executor_module


def test_execute_select_query(tmp_path, monkeypatch):

    database_path = tmp_path / "test.db"
    test_engine = create_engine(f"sqlite:///{database_path}")

    data = pd.DataFrame({
        "Product": ["Laptop", "Mouse"],
        "Quantity": [2, 3]
    })

    data.to_sql("sales", test_engine, index=False)

    monkeypatch.setattr(
        executor_module,
        "read_only_engine",
        test_engine
    )

    result = executor_module.execute_query(
        "SELECT * FROM sales"
    )

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert list(result.columns) == ["Product", "Quantity"]

    test_engine.dispose()


def test_reject_invalid_query():

    with pytest.raises(ValueError):
        executor_module.execute_query(
            "DELETE FROM sales"
        )