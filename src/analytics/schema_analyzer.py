def analyze_schema(data):

    schema = {}

    for column in data.columns:

        is_numeric = data[column].dtype.kind in "iuf"

        is_date = "date" in column.lower()

        schema[column] = {
            "data_type": str(data[column].dtype),
            "missing_values": int(data[column].isnull().sum()),
            "unique_values": int(data[column].nunique()),
            "is_numeric": is_numeric,
            "is_date": is_date
        }

    return schema