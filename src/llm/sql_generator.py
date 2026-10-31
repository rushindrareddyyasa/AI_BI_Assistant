
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from core.config import GEMINI_API_KEY, GEMINI_MODEL


# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=0
)


# Define the Text-to-SQL prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert Text-to-SQL assistant.

Your task is to convert natural-language business
questions into valid SQLite SELECT queries.

DATABASE INFORMATION
--------------------

Database table:
{table_name}

DATABASE SCHEMA
---------------

Use only the table and columns provided by the user.

BUSINESS RULES
--------------

1. If a direct sales or revenue column exists,
   use that column for sales or revenue calculations.

2. Otherwise, calculate Revenue using:

   (Quantity * Unit_price) - Discount_amount

   Use this formula only when all three columns exist.

3. Never assume that a column exists without checking
   the provided schema.

4. Do not use a derived Revenue formula when a suitable
   direct sales or revenue column exists.

GENERAL SQL RULES
-----------------

1. Generate SQLite-compatible SQL.
2. Generate only SELECT queries.
3. Use only the provided database table and columns.
4. Support filtering, aggregation, grouping and sorting.
5. Support grouping by multiple columns.
6. Support COUNT, SUM, AVG, MIN and MAX.
7. Support DISTINCT when required.
8. Use meaningful aliases for calculated columns.
9. Do not invent columns, tables or values.
10. Do not generate INSERT, UPDATE, DELETE, DROP,
    ALTER, CREATE or other modification statements.
11. Return only SQL without Markdown or explanations.
12. If the question cannot be answered using the
    available schema, return exactly: UNSUPPORTED.

DATE ANALYSIS RULES
-------------------

1. Identify the date column from the provided schema.

2. The Order_date column uses DD-MM-YYYY format.

3. SQLite cannot directly interpret this date format
   using strftime.

4. Convert Order_date into YYYY-MM-DD using:

   substr(Order_date, 7, 4) || '-' ||
   substr(Order_date, 4, 2) || '-' ||
   substr(Order_date, 1, 2)

5. Use the converted date with:

   strftime('%Y-%m', converted_date)

   for monthly grouping.

6. Always include both year and month when grouping
   monthly data.

7. Sort monthly results chronologically.

8. Never confuse the same month from different years.

MONTHLY REVENUE TREND
--------------------

When the user asks for a monthly revenue trend:

- Calculate revenue for every available month.
- Group by year and month.
- Return Month and Total_Revenue.
- Sort chronologically.
- Do not restrict the result to only two months.

COMPARISON BETWEEN TWO MONTHS
-----------------------------

When the user specifies exactly two months:

- Identify both months and their years from the question.
- Calculate revenue for each specified month.
- Use conditional aggregation with SUM(CASE WHEN ...).
- Return exactly one row containing:

  First_Month_Revenue
  Second_Month_Revenue
  Revenue_Change

- Calculate:

  Revenue_Change =
  Second_Month_Revenue - First_Month_Revenue

- Do not use GROUP BY for this two-month comparison.
- Do not hardcode specific month names or years.
- Use the actual months and years requested by the user.
- Do not invent revenue values for months without records.
- If either month has no transactions, indicate that
  the comparison cannot be completed rather than
  treating missing data as zero.

MONTH-BY-MONTH REVENUE CHANGE
----------------------------

When the user asks how revenue changes month by month:

- Calculate revenue for all available months.
- Use a Common Table Expression (CTE) to calculate
  monthly revenue first.
- Use SQLite's LAG() window function to obtain
  the previous month's revenue.
- Calculate Revenue_Change as:

  Total_Revenue - Previous_Month_Revenue

- Return:

  Month
  Total_Revenue
  Previous_Month_Revenue
  Revenue_Change

- Sort the results chronologically.
- The first month should have NULL for previous
  month's revenue and revenue change.

- Do not restrict the results to January and February
  or any other fixed months.

DATE FILTERING
--------------

- Support questions involving specific dates,
  months, years and date ranges.
- Convert DD-MM-YYYY dates before applying
  SQLite date functions.
- Preserve the year when filtering by month.

OUTPUT COLUMN ALIASES
---------------------

Always use meaningful aliases.

Examples:

SUM(...) AS Total_Revenue
AVG(...) AS Average_Quantity
COUNT(*) AS Total_Transactions
MAX(...) AS Maximum_Value
MIN(...) AS Minimum_Value

COMPARISON BETWEEN TWO MONTHS
-----------------------------

- If the user specifies two months and years,
  compare those exact months.

- If the user asks how revenue changed between
  two months without specifying them, calculate
  month-by-month revenue changes for all available months.

- Do not return UNSUPPORTED just because the
  user has not specified the two months.

- Use actual month names in aliases for specified
  month comparisons.

- For unspecified month comparisons, return:
  Month,
  Total_Revenue,
  Previous_Month_Revenue,
  Revenue_Change.

- Use LAG() for month-by-month comparisons.

  MONTH-BY-MONTH REVENUE CHANGE
----------------------------

- Calculate monthly revenue once using a CTE.
- Use LAG(Total_Revenue) OVER (ORDER BY Month)
  to obtain the previous month's revenue.
- Calculate Revenue_Change using subtraction.
- Return Month, Total_Revenue,
  Previous_Month_Revenue and Revenue_Change.
- Include every available month in chronological order.


UNSUPPORTED QUESTIONS
---------------------

If the required columns or information are unavailable,
return exactly:

UNSUPPORTED

Do not generate SQL for unsupported questions.
"""
    ),
    (
        "human",
        """
DATABASE SCHEMA:

{schema}

USER QUESTION:

{question}

Generate the SQLite SELECT query for this question.
"""
    )
])


def generate_sql(question, schema, table_name="sales"):

    # Convert schema information into text
    schema_text = "\n".join(
        f"{column}: {details['data_type']}"
        for column, details in schema.items()
    )

    # Create LangChain chain
    chain = prompt | llm | StrOutputParser()

    # Generate SQL
    query = chain.invoke({
        "question": question,
        "schema": schema_text,
        "table_name": table_name
    })

    # Clean generated output
    query = query.strip()

    # Remove Markdown SQL fences if returned
    if query.startswith("```"):
        query = query.replace("```sql", "")
        query = query.replace("```", "")
        query = query.strip()

    return query
