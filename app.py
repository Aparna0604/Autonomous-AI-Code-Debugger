import streamlit as st
from fixer import fix_code

st.set_page_config(page_title="AI Debugger", layout="wide")
st.title("AI Debugger 🚀")
st.markdown("### 🧠 Fix your code instantly using AI")

code = st.text_area("Paste your code here",height=200)

language = st.selectbox("Select Language", ["Python", "Java", "C++", "JavaScript"])

if st.button("Fix Code"):
    logs = "Syntax Error"
    result = fix_code(code, logs, language)
    st.session_state["last_result"] = result
    st.markdown("## ✅ Result")
    st.markdown(result)