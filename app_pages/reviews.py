# import streamlit as st
# from etl.reviews import get_reviews_by_keyword

# def run():
#     st.title("🛍️ Amazon & Flipkart Product Reviews")
#     keyword = st.text_input("🔍 Enter product keyword")

#     if keyword:
#         with st.spinner("Fetching reviews..."):
#             reviews = get_reviews_by_keyword(keyword)

#         if not reviews:
#             st.warning("No reviews found or APIs failed.")
#             return

#         for r in reviews:
#             st.subheader(r["title"])
#             st.markdown(f"**Source**: {r['source']}")
#             st.markdown(f"**Rating**: {r['rating']}")
#             st.markdown(f"**Review / Description**: {r['review']}")
#             st.markdown(f"[🔗 Product Link]({r['url']})")
#             st.markdown("---")
