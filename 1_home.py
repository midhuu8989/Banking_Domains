import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Agentic AI App Suite", page_icon="📘")

# Optional: Display a logo/banner
st.image("684910d7-36ae-4a66-a4d6-f425db6a52c4.png", use_column_width=True)

# Main Title
st.title("📘 Welcome to the Agentic AI App Suite")
st.markdown("Explore the power of Agentic AI through focused applications across domains.")

st.markdown("---")

# 2_Agentic_vs_Normal_Advisory_App.py
st.subheader("🧠  Normal vs Agentic Advisor")
st.markdown("""
Compare the capabilities of a traditional web application with an AI Agent solution. Understand how agentic systems can reason, adapt, and operate autonomously to perform smarter decision-making.
""")

# 3_Agentic_Advisor.py
st.subheader("🧑‍💼 Agentic Advisor")
st.markdown("""
An AI-powered intelligent assistant that helps you make decisions like a real advisor. It plans, reasons, and interacts with context to support tasks like career planning, writing, and learning.
""")

# 4_Agentic_vs_Normal_Compliance.py
st.subheader("⚖️ Agentic vs Normal WebApp (Compliance)")
st.markdown("""
A side-by-side comparison of a static compliance tool versus an agentic AI compliance assistant. Learn how agentic AI can extract, interpret, and reason over policy documents automatically.
""")

# 5_Compliance_AI.py
st.subheader("📜 Compliance AI")
st.markdown("""
Upload your policy documents and let the agentic system extract rules, highlight gaps, and simulate audits. Uses retrieval-augmented generation (RAG) and reasoning agents for advanced legal understanding.
""")

# 6_loan_advisory.py
st.subheader("💰 Loan Advisory")
st.markdown("""
A personal finance and loan advisor that simulates various loan options, analyzes your financial data, and provides smart investment and debt recommendations using AI agents.
""")

st.markdown("---")
st.success("👈 Use the sidebar to navigate through the apps and experience how agentic AI transforms traditional solutions.")
