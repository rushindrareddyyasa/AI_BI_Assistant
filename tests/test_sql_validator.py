from analytics.sql_validator import validate_query


def test_valid_select_query():
    is_valid, message = validate_query("SELECT * FROM sales")

    assert is_valid is True


def test_valid_cte_query():
    query = "WITH revenue AS (SELECT 100 AS total) SELECT * FROM revenue"

    is_valid, message = validate_query(query)

    assert is_valid is True


def test_reject_insert_query():
    is_valid, message = validate_query(
        "INSERT INTO sales VALUES ('Laptop', 2)"
    )

    assert is_valid is False


def test_reject_delete_query():
    is_valid, message = validate_query("DELETE FROM sales")

    assert is_valid is False


def test_reject_multiple_statements():
    is_valid, message = validate_query(
        "SELECT * FROM sales; DELETE FROM sales"
    )

    assert is_valid is False


def test_reject_empty_query():
    is_valid, message = validate_query("")

    assert is_valid is False