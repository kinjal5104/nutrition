from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from app_pages import home, nutrition_info, reviews, social_trends, powerbi_dashboard, about

# ---- GLOBAL STYLES ----

st.markdown("""
    <style>
    /* App background */
    body, .stApp {
        background: linear-gradient(120deg, #f4f8fb 0%, #fbeeee 100%) !important;
    }
    /* Softer sidebar (navbar) */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #e3f0fa 0%, #fbeeee 100%);
        color: #222 !important;
        border-right: 1.5px solid #e0e0e0;
    }
    [data-testid="stSidebar"] * {
        color: #222 !important; /* Force dark text */
    }
    .stSidebar .st-radio label, .stSidebar .st-radio div {
        color: #222 !important;
    }
    .stSidebar .stTitle {
        color: #1da1f2 !important;
    }

    /* Make input fields stand out */
    input, textarea, select, .stTextInput>div>div>input {
        background: #fff !important;
        border: 1.5px solid #1da1f2 !important;
        border-radius: 8px !important;
        color: #222 !important;
        font-size: 1.08rem !important;
        box-shadow: 0 2px 8px #1da1f210 !important;
    }
    input:focus, textarea:focus, select:focus, .stTextInput>div>div>input:focus {
        border: 2px solid #ff6f61 !important;
        outline: none !important;
        background: #f4f8fb !important;
    }

    /* MOBILE FIX: Override Streamlit's white text on small screens */
    @media (max-width: 768px) {
        [data-testid="stSidebar"] * {
            color: #222 !important;
        }
    }
    </style>
""", unsafe_allow_html=True)


PAGES = {
    "Home": home,
    "Nutrition Info": nutrition_info,
    # "Customer Reviews": reviews,
    "Social Trends": social_trends,
    "Power BI Dashboard": powerbi_dashboard,
    "About": about
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.run()
