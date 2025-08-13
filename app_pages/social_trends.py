import streamlit as st
from etl.social_media import get_social_data
from textwrap import shorten
import re

PLATFORM_STYLES = {
    "Reddit": {"color": "#FF4500", "icon": "🔸"},
    "Twitter": {"color": "#1DA1F2", "icon": "🐦"},
    "YouTube": {"color": "#FF0000", "icon": "▶️"}
}

def engagement_badge(post):
    if "engagement" in post:
        return f"<span style='background:#eee;border-radius:8px;padding:2px 8px;font-size:13px;'>{post['engagement']}</span>"
    likes = post.get("likes")
    upvotes = post.get("upvotes")
    if likes is not None:
        return f"<span style='background:#eee;border-radius:8px;padding:2px 8px;font-size:13px;'>👍 {likes} likes</span>"
    if upvotes is not None:
        return f"<span style='background:#eee;border-radius:8px;padding:2px 8px;font-size:13px;'>⬆️ {upvotes} upvotes</span>"
    return ""

def run():
    st.markdown(
        """
        <style>
        .social-bg {
            background: linear-gradient(135deg, #1da1f2 0%, #ff6f61 100%);
            border-radius: 22px;
            padding: 2.5rem 2rem 2rem 2rem;
            margin: 2.5rem auto 2rem auto;
            max-width: 1100px;
            min-width: 350px;
            box-shadow: 0 4px 32px #0002;
        }
        .social-title {
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
        .social-sub {
            font-size: 1.18rem;
            color: #fff;
            margin-bottom: 2.2rem;
            text-align: center;
        }
        .social-post-card {
            border-radius: 12px;
            border: 1.5px solid #e3f0fa;
            background: #fff;
            margin-bottom: 1.2rem;
            box-shadow: 0 2px 8px #0001;
            padding: 1.2rem 1.5rem;
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
            height: auto !important;
            box-shadow: 0 2px 8px #1da1f210 !important;
        }
        .stTextInput>div>div>input:focus {
            border: 2px solid #ff6f61 !important;
            background: #f4f8fb !important;
        }
        div[data-testid="stTextInput"] label {
            display: none !important;
        }
        .custom-label {
            font-size: 2rem;
            color: #ff6f61;
            text-align: center;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }
        </style>
        <div class="social-bg">
            <div class="social-title">🌐 Social Media Trends</div>
            <div class="social-sub">
                Discover what people are saying about your product across <b>Reddit</b>, <b>Twitter</b>, and <b>YouTube</b>.<br>
                <span style="color:#ffe066;font-weight:600;">See live opinions, trending topics, and real engagement!</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Custom label above search bar
    st.markdown('<div class="custom-label">🔍 Enter product name</div>', unsafe_allow_html=True)

    product_name = st.text_input(
        "Product Name",  # Non-empty label for accessibility
        key="social_trends_input",
        label_visibility="collapsed",
        help="Type a product name to see trending social media posts."
    )

    if product_name:
        with st.spinner("Gathering top social media posts..."):
            data = get_social_data(product_name)

        if not data:
            st.info("No social media mentions found.")
            return

        # Sort posts by engagement
        def engagement_score(post):
            if "likes" in post and post["likes"] is not None:
                return post["likes"]
            if "upvotes" in post and post["upvotes"] is not None:
                return post["upvotes"]
            if "engagement" in post:
                nums = re.findall(r"\d+", post["engagement"])
                return int(nums[0]) if nums else 0
            return 0

        sorted_data = sorted(data, key=engagement_score, reverse=True)

        for post in sorted_data:
            platform = post.get("platform", "Unknown")
            user = post.get("user", "anonymous")
            text = post.get("text", "")
            style = PLATFORM_STYLES.get(platform, {"color": "#555", "icon": "💬"})

            st.markdown(
                f"""
                <div class="social-post-card">
                    <div class="social-post-header">
                        <span style="font-size:1.6rem;">{style['icon']}</span>
                        <span class="social-post-platform" style="color:{style['color']};">{platform}</span>
                    </div>
                    <div class="social-post-user">👤 {user}</div>
                    <div class="social-post-text">{shorten(text, width=320, placeholder='...')}</div>
                    <div>{engagement_badge(post)}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    run()
