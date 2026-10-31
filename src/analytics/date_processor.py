import pandas as pd


def process_date_column(data, column):

    data = data.copy()

    data[column] = pd.to_datetime(
        data[column],
        format="%d-%m-%Y",
        errors="coerce"
    )

    return data