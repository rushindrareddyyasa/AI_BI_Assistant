AI Development Report — AI BI Assistant

1. AI Tools Used

The following AI tools were used in this project:

Tool

Purpose

Google Gemini

Generate SQL queries from business questions written in natural language

LangChain

Connect Gemini with the application and manage prompts and responses

2. How AI Was Used During Development

A. AI Integration in the Application

Google Gemini was connected to the application using LangChain.

When a user asks a question, the application sends the question and dataset column details to Gemini. Gemini understands the question and generates an SQL query.

Before running the query, the application checks whether the SQL query is allowed. If it is valid, the query is executed using SQLite.

B. Development Assistance

AI assistance was used during development for:

Understanding new Python libraries and how to use them.

Finding and fixing errors in the code.

Understanding error messages and handling errors.

Preparing and improving project documentation.

Finding possible ways to improve the application.

All suggested changes were checked and tested locally.

3. Problems Encountered and Debugging

Problem 1: Date Format in SQLite

Issue: The uploaded dataset had dates in DD-MM-YYYY format. SQLite could not directly use this format for monthly revenue calculations.

Debugging: I checked the generated SQL query and its output to understand why the monthly revenue values were returning NULL.

Solution: I converted the date format into YYYY-MM-DD using SQLite string functions before calculating monthly revenue.

Problem 2: SQL Validator Rejected CTE Queries

Issue: Initially, the SQL validator allowed only queries starting with SELECT. Some generated queries used CTEs, which start with WITH.

Debugging: I tested different SQL queries to identify why valid CTE queries were being rejected.

Solution: I updated the validator to accept both SELECT and WITH queries while continuing to block modification operations.

Problem 3: Handling Missing Values in API Responses

Issue: Pandas missing values caused problems when converting query results into JSON responses.

Debugging: I inspected the API responses using FastAPI Swagger documentation.

Solution: I converted missing values into Python None before returning the results as JSON.

4. Testing and Verification

I used Pytest to create automated tests for different parts of the application.

Currently, 17 automated tests are passing.

Test area

Number of tests

CSV reading

1

Data validation

4

Data cleaning

3

Database operations

1

SQL validation

6

SQL query execution

2

Total

17

I also tested the application manually using the Streamlit interface and FastAPI Swagger documentation.

5. Improvements Possible With One Additional Day

If I had one more day to work on this project, I would focus on the following improvements:

More testing: Add more tests for API endpoints and different error cases.

Better error handling: Show clearer error messages for invalid CSV files, unsupported questions, and database errors.

Charts and visualizations: Allow users to view results as charts instead of only tables. For example, if a user asks about monthly revenue, the application could display a line chart. It could also generate bar charts and pie charts based on the question and query results.

Better documentation: Add more examples and explain the known limitations of the application.

6. Conclusion

This project helped me understand how AI can be used to make data analysis easier.

The application uses Google Gemini and LangChain to generate SQL queries from natural-language questions. FastAPI handles backend operations, SQLite stores the uploaded data, and Streamlit provides the user interface.

Through this project, I gained practical experience in Python, data processing, SQL, API development, database operations, LLM integration, testing, and debugging.