import pandas as pd

from fastapi import FastAPI, HTTPException, UploadFile, File

from schemas.question import QuestionRequest

from ingestion.csv_reader import read_csv_file
from database.database import save_data, read_only_engine

from analytics.schema_analyzer import analyze_schema
from analytics.query_executor import execute_query

from llm.sql_generator import generate_sql


app = FastAPI(title="AI BI Assistant")


TABLE_NAME = "uploaded_data"


@app.get("/")
def home():

    return {
        "message": "Welcome to AI BI Assistant"
    }


@app.post("/upload")
def upload_dataset(file: UploadFile = File(...)):

    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported."
        )

    try:

        # Read uploaded CSV
        data = read_csv_file(file.file)

        # Check empty dataset
        if data.empty:
            raise HTTPException(
                status_code=400,
                detail="Uploaded dataset is empty."
            )

        # Check duplicate column names
        if data.columns.duplicated().any():
            raise HTTPException(
                status_code=400,
                detail="Dataset contains duplicate column names."
            )

        # Store uploaded dataset in SQLite
        save_data(data, TABLE_NAME)

        return {
            "success": True,
            "filename": file.filename,
            "rows": len(data),
            "columns": data.columns.tolist(),
            "message": "Dataset uploaded successfully."
        }

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    finally:
        file.file.close()


@app.get("/schema")
def get_dataset_schema():

    try:

        # Read currently uploaded dataset
        data = pd.read_sql_query(
            f"SELECT * FROM {TABLE_NAME}",
            read_only_engine
        )

        if data.empty:
            raise HTTPException(
                status_code=404,
                detail="No uploaded dataset found."
            )

        # Analyze dataset schema
        schema = analyze_schema(data)

        return {
            "success": True,
            "table": TABLE_NAME,
            "rows": len(data),
            "columns": schema
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=404,
            detail="No uploaded dataset found. Please upload a CSV first."
        )


@app.post("/ask")
def ask_question(request: QuestionRequest):

    try:

        # Read uploaded dataset
        data = pd.read_sql_query(
            f"SELECT * FROM {TABLE_NAME}",
            read_only_engine
        )

        if data.empty:
            raise HTTPException(
                status_code=400,
                detail="Please upload a dataset first."
            )

        # Analyze uploaded dataset schema
        schema = analyze_schema(data)

        # Generate SQL using Gemini
        query = generate_sql(
            request.question,
            schema,
            TABLE_NAME
        )

        # Handle unsupported questions
        if query.strip().upper() == "UNSUPPORTED":
            raise HTTPException(
                status_code=400,
                detail="This question cannot be answered using the dataset."
            )

        # Execute SQL through existing validator and executor
        result = execute_query(query)


        # Replace missing values with None
        result = result.astype(object).where(
            pd.notna(result),
            None
        )

        # Convert DataFrame into JSON-compatible records
        records = result.to_dict(orient="records")

        return {
            "success": True,
            "question": request.question,
            "sql": query,
            "columns": result.columns.tolist(),
            "data": records,
            "error": None
        }

    except HTTPException:
        raise

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )