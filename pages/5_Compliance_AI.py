import streamlit as st
import pandas as pd
import openai
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os

# ========== CONFIG ==========
openai.api_key = st.secrets.get("OPENAI_API_KEY")  # Replace with your key or set in .streamlit/secrets.toml
ALERT_EMAIL = "midhuu89@gmail.com"
SENDER_EMAIL = "noreply@agenticapp.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_PASSWORD = "your_app_password"  # Replace or use secure vault

# ========== SAMPLE DATA ==========
sample_data = pd.DataFrame({
    "Transaction ID": ["TXN001", "TXN002", "TXN003", "TXN004"],
    "Customer": ["John", "Asha", "Lee", "Ravi"],
    "Amount": [1200, 8000, 15000, 450],
    "Purpose": ["Online Shopping", "Crypto Transfer", "International Wire", "Utility Bill"],
    "Status": ["Success", "Success", "Success", "Success"]
})

THRESHOLD = 10000

# ========== PAGE SETUP ==========
st.set_page_config(page_title="Agentic Compliance Monitor", layout="wide")
st.title("🔍 AI Agent Compliance")

# ========== DATA INPUT ==========
st.subheader("📥 Upload Transaction Data or Use Simulator")
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = sample_data.copy()

# ========== DETECTION ==========
st.subheader("🚨 Suspicious Transaction Detection")
suspicious_df = df[df["Amount"] > THRESHOLD]

def highlight_suspicious(row):
    return ['background-color: red' if row["Amount"] > THRESHOLD else '' for _ in row]

st.dataframe(df.style.apply(highlight_suspicious, axis=1), use_container_width=True)

# ========== AGENTIC ACTIONS ==========
if not suspicious_df.empty:
    st.warning(f"{len(suspicious_df)} suspicious transaction(s) flagged.")

    # --- Send Email Alert ---
    send_email = st.button("📧 Send Alert to Compliance Team")
    if send_email:
        try:
            msg = EmailMessage()
            msg.set_content(f"⚠️ Alert: {len(suspicious_df)} suspicious transactions flagged.\n\n{suspicious_df}")
            msg["Subject"] = "Agentic Compliance Alert"
            msg["From"] = SENDER_EMAIL
            msg["To"] = ALERT_EMAIL

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SMTP_PASSWORD)
                server.send_message(msg)
            st.success(f"Alert sent to {ALERT_EMAIL}")
        except Exception as e:
            st.error(f"Email failed: {str(e)}")

    # --- Agent Summary using LLM ---
    st.subheader("🧠 LLM Compliance Summary")
    prompt = f"Summarize this suspicious transaction list:\n{suspicious_df.to_string(index=False)}"
    if st.button("Generate Agentic Summary"):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a compliance auditor."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.info(response.choices[0].message.content.strip())
        except Exception as e:
            st.error(f"LLM failed: {str(e)}")

# ========== AUDIT LOG ==========
log_action = st.button("📝 Log Audit Trail")
if log_action:
    with open("audit_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] Audit logged: {len(suspicious_df)} flagged\n")
    st.success("Audit logged.")

# ========== DAILY REPORT ==========
st.subheader("📅 Daily Batch Report (Simulated)")
if st.button("📤 Generate Daily Report"):
    report_name = f"daily_report_{datetime.now().date()}.csv"
    df.to_csv(report_name, index=False)
    st.success(f"Daily report saved as {report_name}")

# ========== AGENTIC ENHANCEMENT ==========
st.markdown("""
---
### 🧠 Agentic AI Features Used:
- Proactive suspicious detection
- LLM-based transaction summary
- Intelligent email alert
- Automated audit logging
- Daily report generation
""")
