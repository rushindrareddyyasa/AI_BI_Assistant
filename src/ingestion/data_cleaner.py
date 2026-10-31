def clean_data(data):

    data = data.copy()

    # Impute missing unit prices using product-wise median
    for product in data["Product"].unique():

        product_data = data[data["Product"] == product]

        median_price = product_data["Unit_price"].median()

        missing_price = (
            (data["Product"] == product) &
            (data["Unit_price"].isnull())
        )

        data.loc[missing_price, "Unit_price"] = median_price

    # Separate invalid quantity records
    invalid_quantity = data["Quantity"] <= 0

    quarantined_data = data[invalid_quantity].copy()

    cleaned_data = data[~invalid_quantity].copy()

    return cleaned_data, quarantined_data