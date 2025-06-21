import streamlit as st

def run():
    st.header("Power BI Dashboard")
    embed_url = st.secrets["POWERBI_EMBED_URL"]
    st.components.v1.iframe(embed_url, height=600, scrolling=True)
