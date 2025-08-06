import streamlit as st
import openai

# Set OpenAI API key from secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Agentic Personal Finance Advisor", layout="centered")
st.title("🔐 Agentic Personal Finance Advisor")
st.markdown("Let me help you manage your money smarter! Provide your details and ask for advice.")

# --- User Inputs ---

st.header("📥 Enter Your Financial Information")

monthly_income = st.number_input("Monthly Income (₹)", min_value=0, step=1000)

st.subheader("Monthly Spending")
expenses = {
    'groceries': st.number_input("Groceries (₹)", min_value=0, step=500),
    'utilities': st.number_input("Utilities (₹)", min_value=0, step=500),
    'entertainment': st.number_input("Entertainment (₹)", min_value=0, step=500),
    'savings': st.number_input("Savings (₹)", min_value=0, step=500),
    'loans': st.number_input("Loan Payments (₹)", min_value=0, step=500),
    'misc': st.number_input("Miscellaneous (₹)", min_value=0, step=500)
}

st.subheader("Investments")
investments = {
    'mutual_funds': st.number_input("Mutual Funds (₹)", min_value=0, step=1000),
    'stocks': st.number_input("Stocks (₹)", min_value=0, step=1000),
    'fixed_deposit': st.number_input("Fixed Deposit (₹)", min_value=0, step=1000)
}

st.subheader("Loan Info")
loan_balance = st.number_input("Total Loan Balance (₹)", min_value=0, step=1000)
loan_emi = st.number_input("Monthly Loan EMI (₹)", min_value=0, step=500)

st.subheader("Upcoming Bills")
upcoming_bills = st.text_area("Enter Upcoming Bills (comma-separated)", placeholder="e.g., Electricity - ₹1800 on 10th, Credit Card - ₹5500 on 15th")
bills_list = [bill.strip() for bill in upcoming_bills.split(",")] if upcoming_bills else []

# Data summary
finance_data = {
    "monthly_income": monthly_income,
    "monthly_spending": expenses,
    "investments": investments,
    "loan_balance": loan_balance,
    "loan_emi": loan_emi,
    "upcoming_bills": bills_list
}

with st.expander("📊 Review Your Financial Data"):
    st.json(finance_data)

st.header("💬 Ask Your Finance Assistant")
query = st.text_area("Type your query", placeholder="e.g., How can I save more or invest smarter?")

if st.button("💡 Get Smart Advice"):
    if not query:
        st.warning("Please enter your question.")
    else:
        with st.spinner("Analyzing your data..."):

            prompt = f"""
You are a smart personal finance agent. The user has provided their income, expenses, investments, loans, and bills.
Use this data to assess their financial health, suggest improvements, highlight risks, and recommend next steps.

Financial Data:
{finance_data}

User Query:
{query}

Respond with clear, helpful, and proactive advice.
"""

            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful and proactive financial advisor."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )

                result = response.choices[0].message.content
                st.success("Here's your personalized financial advice:")
                st.markdown(result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
