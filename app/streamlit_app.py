import streamlit as st
import httpx


API_URL = "http://127.0.0.1:8000"


# Page configuration
st.set_page_config(
    page_title="AI BI Assistant",
    page_icon="📊",
    layout="wide"
)


# Application title
st.title("AI BI Assistant")

st.write(
    "Upload your dataset and ask questions "
    "using natural language."
)


# Dataset upload section
st.header("1. Upload Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)


if uploaded_file is not None:

    if st.button("Upload Dataset"):

        try:

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "text/csv"
                )
            }

            response = httpx.post(
                f"{API_URL}/upload",
                files=files,
                timeout=60
            )

            if response.status_code == 200:

                result = response.json()

                st.session_state["dataset_uploaded"] = True

                st.success(result["message"])

                st.write("Filename:", result["filename"])
                st.write("Total Rows:", result["rows"])
                st.write("Total Columns:", len(result["columns"]))

                st.write("Dataset Columns:")
                st.write(result["columns"])

            else:

                st.error(response.text)

        except Exception as error:

            st.error(str(error))


# Question section
st.header("2. Ask a Question")

question = st.text_area(
    "Enter your business question",
    placeholder="Example: Show total sales by region"
)


if st.button("Submit Question"):

    if not st.session_state.get("dataset_uploaded", False):

        st.warning("Please upload a dataset first.")

    elif not question.strip():

        st.warning("Please enter a question.")

    else:

        try:

            response = httpx.post(
                f"{API_URL}/ask",
                json={"question": question},
                timeout=120
            )

            if response.status_code == 200:

                result = response.json()

                st.header("3. Answer")

                st.dataframe(
                    result["data"],
                    use_container_width=True
                )

                st.header("4. Supporting Data")

                with st.expander("View Generated SQL"):

                    st.code(
                        result["sql"],
                        language="sql"
                    )

            else:

                st.error(response.text)

        except Exception as error:

            st.error(str(error))