from analytics.schema_analyzer import analyze_schema


def profile_dataset(data):

    schema = analyze_schema(data)

    numerical_columns = []
    categorical_columns = []
    date_columns = []

    for column, details in schema.items():

        if details["is_numeric"]:
            numerical_columns.append(column)

        elif details["is_date"]:
            date_columns.append(column)

        else:
            categorical_columns.append(column)

    profile = {
        "total_rows": len(data),
        "total_columns": len(data.columns),
        "numerical_columns": numerical_columns,
        "categorical_columns": categorical_columns,
        "date_columns": date_columns,
        "schema": schema
    }

    return profile