def validate_data(data):
    errors = []

    if data.isnull().sum().sum() > 0:
        errors.append("Missing values found")

    if data["Transaction_Id"].duplicated().any():
        errors.append("Duplicate transaction IDs found")

    if (data["Quantity"] <= 0).any():
        errors.append("Invalid quantity found")

    if (data["Unit_price"] <= 0).any():
        errors.append("Invalid unit price found")

    return errors