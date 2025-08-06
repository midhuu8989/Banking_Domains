import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Agentic vs Normal",
        "Agentic Advisor",
        "Agentic vs Normal WebApp",
        "Compliance AI",
        "Loan Advisory"
    ],
    index=0
)

# Load corresponding page
if page == "Home":
    st.switch_page("1_home.py")
elif page == "Agentic vs Normal":
    st.switch_page("pages/2_Agentic_vs_Normal.py")
elif page == "Agentic Advisor":
    st.switch_page("pages/3_Agentic_Advisor.py")
elif page == "Agentic vs Normal WebApp":
    st.switch_page("pages/4_Agentic_vs_Normal_WebApp.py")
elif page == "Compliance AI":
    st.switch_page("pages/5_Compliance_AI.py")
elif page == "Loan Advisory":
    st.switch_page("pages/6_loan_advisory.py")
