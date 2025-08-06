# loan_advisor_app.py
import streamlit as st
import openai
import os
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Load API Key from .streamlit/secrets.toml
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Agentic AI Loan Advisor", layout="wide")
st.title("Agentic AI Loan Advisory System")

# Sample loan customer data
sample_data = [
    {"name": "John Doe", "income": 50000, "credit_score": 680, "loan_amount": 20000, "existing_loans": 2},
    {"name": "Jane Smith", "income": 80000, "credit_score": 750, "loan_amount": 30000, "existing_loans": 1},
    {"name": "Raj Kumar", "income": 30000, "credit_score": 600, "loan_amount": 15000, "existing_loans": 3}
]

# Display and allow user to select profile
st.sidebar.header("User Profile")
selected_name = st.sidebar.selectbox("Select a customer", [d["name"] for d in sample_data])
user_data = next(d for d in sample_data if d["name"] == selected_name)
st.sidebar.write("### Selected User Info")
st.sidebar.json(user_data)

# LangChain LLM Setup
llm = ChatOpenAI(temperature=0.5, model_name="gpt-4")
memory = ConversationBufferMemory(memory_key="chat_history")

loan_template = PromptTemplate(
    input_variables=["name", "income", "credit_score", "loan_amount", "existing_loans"],
    template="""
    You are a financial advisor AI agent. Based on the user's profile:
    Name: {name}
    Income: {income}
    Credit Score: {credit_score}
    Loan Amount Requested: {loan_amount}
    Existing Loans: {existing_loans}

    Offer personalized loan advisory including:
    - Loan eligibility decision
    - Risk level (low/medium/high)
    - Suggestions to improve eligibility if needed
    - Escalation advice if credit score is too low
    - Follow-up actions
    Provide actionable and helpful advice.
    """
)

prompt = loan_template.format(**user_data)

if st.button("Get Advisory"):
    response = llm.predict(prompt)
    st.subheader("🔍 AI Advisor Response:")
    st.write(response)

# Optional: File upload for user profiles
st.subheader("Or Upload Custom Customer Data")
uploaded_file = st.file_uploader("Upload a CSV with customer profiles", type=["csv"])
if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.info("You can modify the app to loop through uploaded profiles and generate reports for each.")
