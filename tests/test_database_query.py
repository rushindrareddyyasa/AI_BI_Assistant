from sqlalchemy import text
from database.database import engine

with engine.connect() as connection:

    sales_count = connection.execute(
        text("SELECT COUNT(*) FROM sales")
    ).scalar()

    quarantine_count = connection.execute(
        text("SELECT COUNT(*) FROM quarantined_sales")
    ).scalar()

    print("Sales records:", sales_count)
    print("Quarantined records:", quarantine_count)