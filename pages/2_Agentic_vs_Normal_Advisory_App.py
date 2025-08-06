import streamlit as st

st.set_page_config(page_title="Agentic vs Normal", layout="centered")

st.title("🧠 Agentic AI vs Normal Web App in Finance")

st.markdown("### 🔍 Normal Finance Web App:")
st.markdown("""
A **normal finance app** is reactive. It waits for user input and responds accordingly. For example:

- You manually enter expenses to track spending.
- You request investment advice.
- You simulate a loan by inputting your values.

💡 **Example:**
> You input ₹50,000 monthly income → App shows savings suggestions.
""")

st.markdown("### 🤖 Agentic Personal Finance Advisor:")
st.markdown("""
An **agentic AI** behaves more like an assistant:
- It understands your financial patterns without you asking.
- It proactively gives advice (e.g., "Cut down food delivery spending").
- It simulates outcomes and sends alerts (e.g., "Your EMI is due tomorrow").

💡 **Example:**
> “You spent ₹12,000 on food delivery this month. Consider switching to home-cooked meals to save ₹5,000.”

✨ **Agentic AI = Intent + Autonomy + Proactiveness**
""")

st.markdown("---")
st.markdown("➡️ Use the sidebar to go try the **Agentic Advisor** in action.")
