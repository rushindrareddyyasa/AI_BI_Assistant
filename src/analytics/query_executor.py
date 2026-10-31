import pandas as pd
from sqlalchemy import text
from database.database import read_only_engine
from analytics.sql_validator import validate_query


def execute_query(query):
    is_valid,message = validate_query(query)

    if not is_valid:
        raise ValueError(message)

    with read_only_engine.connect() as connection:

        result = connection.execute(text(query))

        data = pd.DataFrame(
            result.fetchall(),
            columns=result.keys()
        )

    return data
    