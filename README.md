# AI BI Assistant

An AI-powered Business Intelligence application that allows users to upload CSV datasets and ask business questions using natural language. The application uses Google Gemini through LangChain to generate SQL queries, validates those queries, executes them against an SQLite database, and displays structured results through a Streamlit interface.

## Features

- Upload CSV datasets.
- Validate and clean uploaded data.
- Store dataset information in SQLite.
- Analyze dataset schemas.
- Ask business questions using natural language.
- Generate SQL queries using Google Gemini and LangChain.
- Validate SQL before execution.
- Execute read-only SQL queries.
- Display query results in tabular format.
- View generated SQL as supporting information.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| LLM | Google Gemini |
| LLM Framework | LangChain |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Database Integration | SQLAlchemy |
| Visualization | Plotly |
| Testing | Pytest, HTTPX |
| Code Quality | Ruff |
| Package Management | uv |

## Project Structure

```text
AI_BI_Assistent/
├── app/
│   ├── main.py
│   └── streamlit_app.py
├── src/
│   ├── api/
│   ├── ingestion/
│   ├── analytics/
│   ├── llm/
│   ├── database/
│   ├── schemas/
│   ├── visualization/
│   └── core/
├── tests/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

## Prerequisites

- Python 3.13 or compatible version.
- uv package manager.
- Google Gemini API key.

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI_BI_Assistent
```

Create a virtual environment:

```bash
uv venv --python 3.13
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
uv sync
```

## Environment Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash-lite
```

Never commit your `.env` file or expose your API key.

## Running the Application

### 1. Start the FastAPI backend

```powershell
$env:PYTHONPATH="src"
uvicorn main:app --reload --app-dir app
```

Backend URL:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 2. Start the Streamlit frontend

Open another terminal, activate the virtual environment, and run:

```powershell
streamlit run app/streamlit_app.py
```

The Streamlit interface will open in your browser.

## Application Workflow

1. Upload a CSV dataset.
2. The backend reads and stores the uploaded dataset.
3. Enter a business question in natural language.
4. Gemini generates an SQL query based on the dataset schema.
5. The backend validates the generated SQL.
6. The validated query executes against SQLite.
7. Results are returned through the API and displayed as a table.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Backend welcome endpoint |
| POST | `/upload` | Upload a CSV dataset |
| GET | `/schema` | Retrieve uploaded dataset schema |
| POST | `/ask` | Ask a business question |

## Running Automated Tests

Run the complete test suite:

```powershell
pytest -v
```

Run a specific test file:

```powershell
pytest tests/test_sql_validator.py -v
```

## Security Considerations

- API keys are stored in environment variables.
- Uploaded datasets are stored locally.
- SQL validation allows read-only query execution.
- Multiple SQL statements are rejected.
- Company-provided confidential datasets must not be committed to Git.

## Documentation

Additional project documentation is available in the `docs/` directory:

- `architecture.md` — system architecture and data flow.
- `AI_DEVELOPMENT_REPORT.md` — AI tools, development experience, encountered problems, debugging, and future improvements.

## Limitations

- The application currently uses SQLite for data storage.
- SQL generation depends on the configured Gemini model and API availability.
- SQL validation uses basic query checks and is not a complete SQL security parser.
- Results depend on the quality and structure of the uploaded dataset.

## License

This project was developed as part of a Graduate Engineer Trainee assessment.
