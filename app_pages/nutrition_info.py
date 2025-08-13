import streamlit as st
import pandas as pd
import numpy as np
from etl.nutrition import get_nutrition_data

def safe_numeric(val):
    try:
        if val in [None, '', 'N/A']:
            return np.nan
        return float(val)
    except Exception:
        return np.nan

def run():
    st.markdown(
        """
        <style>
        .nutri-bg {
            background: linear-gradient(135deg, #1da1f2 0%, #ff6f61 100%);
            border-radius: 22px;
            padding: 2.5rem 2rem 2rem 2rem;
            margin: 2.5rem auto 2rem auto;
            max-width: 1100px;
            min-width: 350px;
            box-shadow: 0 4px 32px #0002;
        }
        .nutri-title {
            font-size: 2.5rem;
            font-weight: 900;
            letter-spacing: 1px;
            color: #fff;
            margin-bottom: 0.5rem;
            text-align: center;
            text-shadow: 0 2px 8px #0001;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.7rem;
        }
        .nutri-sub {
            font-size: 1.18rem;
            color: #fff;
            margin-bottom: 2.2rem;
            text-align: center;
        }
        .nutri-table-container {
            background: #fff;
            border-radius: 16px;
            box-shadow: 0 2px 16px #1da1f210;
            padding: 1.5rem 1.2rem;
            margin-top: 1.5rem;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }
        /* Input styling */
        .stTextInput {
            width: 100% !important;
        }
        .stTextInput>div>div>input {
            background: #fff !important;
            border: 2px solid #1da1f2 !important;
            border-radius: 8px !important;
            color: #222 !important;
            font-size: 1.1rem !important;
            padding: 0.6rem !important; /* smaller padding */
            height: auto !important; /* no fixed height */
            box-shadow: 0 2px 8px #1da1f210 !important;
        }
        .stTextInput>div>div>input:focus {
            border: 2px solid #ff6f61 !important;
            background: #f4f8fb !important;
        }
        /* Hide default label */
        div[data-testid="stTextInput"] label {
            display: none !important;
        }
        /* Custom label style */
        .custom-label {
            font-size: 2rem;
            color: #ff6f61;
            text-align: center;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }
        </style>
        <div class="nutri-bg">
            <div class="nutri-title">🍽️ Nutrition Information</div>
            <div class="nutri-sub">
                Instantly discover nutrition facts for thousands of foods.<br>
                <span style="color:#ffe066;font-weight:600;">Search any product to get energy, macros, Nutri-Score, NOVA group, and more!</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Large custom label
    st.markdown('<div class="custom-label">Enter product name</div>', unsafe_allow_html=True)

    product_name = st.text_input(
        "Product Name",  # Non-empty label for accessibility
        key="big_input",
        label_visibility="collapsed"  # Hides it visually
    )

    if product_name:
        data = get_nutrition_data(product_name)
        products = data.get('openfoodfacts', [])

        if not products:
            st.warning("No products found.")
            return

        rows = []
        for product in products:
            nutriments = product.get('nutriments', {})
            rows.append({
                "Product Name": product.get('product_name', ''),
                "Brand": product.get('brands', ''),
                "Quantity": product.get('quantity', ''),
                "Energy (kcal)": safe_numeric(nutriments.get('energy-kcal_100g')),
                "Fat (g)": safe_numeric(nutriments.get('fat_100g')),
                "Carbs (g)": safe_numeric(nutriments.get('carbohydrates_100g')),
                "Proteins (g)": safe_numeric(nutriments.get('proteins_100g')),
                "Nutri-Score": product.get('nutriscore_grade', ''),
                "NOVA Group": safe_numeric(product.get('nova_group'))
            })
        df = pd.DataFrame(rows)

        st.markdown('<div class="nutri-table-container">', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    run()
