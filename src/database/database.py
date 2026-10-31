import re
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/processed/sales.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

read_only_engine = create_engine(
    "sqlite:///file:data/processed/sales.db?mode=ro&uri=true"
)

def save_data(data, table_name):

    table_name = re.sub(r"\W+", "_", table_name.lower())

    if table_name[0].isdigit():
        table_name = "table_" + table_name

    data.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Data saved to table: {table_name}")