import streamlit as st

st.set_page_config(page_title="AI Agent Compliance", layout="wide")
st.title("🤖 Agentic AI vs 🧾 Normal Compliance System")

st.markdown("""
| Feature | Normal App | Agentic AI App |
|--------|------------|----------------|
| **Monitoring** | Manual or periodic rule checks | Real-time autonomous monitoring |
| **Action on Violation** | Logs violation, waits for human | Flags, blocks, and notifies autonomously |
| **Adaptability** | Static rules | Learns patterns and adapts |
| **Audit Trail** | Manual entry | Auto-generated with detailed context |
| **Notification** | Human triggered | Auto-sent via defined workflows |
| **Example Message** | "Transaction over 50k, please check" | "Detected 3 transactions breaching AML. Flagged and notified compliance officer." |
""")

st.markdown("#### 🧠 Agentic AI acts like a proactive assistant:")
st.info("""
"I’ve identified 3 transactions breaching AML thresholds and initiated a risk flag to the compliance officer."
""")
