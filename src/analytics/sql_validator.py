import re


def validate_query(query):

    query = query.strip()

    if not query:
        return False, "Query cannot be empty"

    # Reject multiple SQL statements
    if ";" in query.rstrip(";"):
        return False, "Multiple SQL statements are not allowed"

    # Allow only SELECT and withqueries
    if not re.match(r"^(SELECT|WITH)\b", query, re.IGNORECASE):
        return False, "Only SELECT queries are allowed"

    # Check for dangerous SQL keywords
    blocked_keywords = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "TRUNCATE",
        "CREATE",
        "REPLACE"
    ]

    for keyword in blocked_keywords:

        pattern = rf"\b{keyword}\b"

        if re.search(pattern, query, re.IGNORECASE):
            return False, f"Blocked SQL operation: {keyword}"

    return True, "Valid SQL query"