import streamlit as st

st.set_page_config(
    page_title="ResearchForge",
    page_icon="⚒️"
)

st.title("⚒️ ResearchForge")

st.write("Testing Streamlit Secrets...")

try:
    st.success("Streamlit Secrets Loaded")

    if "GEMINI_API_KEY" in st.secrets:
        st.success("✅ GEMINI_API_KEY Found")

        key = st.secrets["GEMINI_API_KEY"]

        st.write("Key Length:", len(key))

        st.write("First 4 Characters:", key[:4])

        st.write("Last 4 Characters:", key[-4:])

    else:
        st.error("❌ GEMINI_API_KEY Not Found")

except Exception as e:
    st.error(f"Error: {e}")