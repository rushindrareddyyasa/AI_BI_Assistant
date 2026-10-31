def build_query(instruction, schema):

    if not instruction.answerable:
        raise ValueError(instruction.reason)

    operation = instruction.operation
    value_column = instruction.value_column
    group_column = instruction.group_column

    available_columns = list(schema.keys())

    # Handle Revenue as a derived column
    if value_column == "Revenue":
        value_expression = (
            "(Quantity * Unit_price) - Discount_amount"
        )
    elif value_column in available_columns:
        value_expression = value_column
    else:
        raise ValueError("Invalid value column")

    # Validate grouping column
    if group_column and group_column not in available_columns:
        raise ValueError("Invalid group column")

    # Build SQL for maximum total
    if operation == "max_sum":

        if not group_column:
            raise ValueError("Group column is required")

        query = f"""
            SELECT
                {group_column},
                SUM({value_expression}) AS Total_Value
            FROM sales
            GROUP BY {group_column}
            ORDER BY Total_Value DESC
        """

        if instruction.limit:
            query += f" LIMIT {instruction.limit}"

    else:
        raise ValueError("Unsupported operation")

    return query.strip()