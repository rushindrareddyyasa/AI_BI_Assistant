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
│   ├── ingestion/
│   ├── analytics/
│   ├── llm/
│   ├── database/
│   ├── schemas/
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

