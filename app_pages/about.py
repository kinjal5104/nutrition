import streamlit as st

def run():
    st.markdown(
        """
        <style>
        .about-bg {
            background: linear-gradient(135deg, #1da1f2 0%, #ff6f61 100%);
            border-radius: 20px;
            padding: 2.8rem 2.5rem 2.5rem 2.5rem;
            margin: 2.5rem auto 2rem auto;
            max-width: 1100px;
            min-width: 350px;
            box-shadow: 0 4px 32px #0002;
        }
        .about-flex {
            display: flex;
            flex-wrap: wrap;
            gap: 2.5rem;
            justify-content: space-between;
        }
        .about-section {
            flex: 1 1 320px;
            background: rgba(255,255,255,0.92);
            border-radius: 12px;
            padding: 1.5rem 1.2rem;
            margin-bottom: 1.2rem;
            box-shadow: 0 2px 12px #0001;
            min-width: 300px;
        }
        .about-title {
            font-size: 2.5rem;
            font-weight: 900;
            letter-spacing: 1px;
            color: #222;
            margin-bottom: 0.5rem;
        }
        .about-sub {
            font-size: 1.25rem;
            color: #444;
            margin-bottom: 1.5rem;
        }
        .about-feature-list {
            margin: 0.7rem 0 0 0;
            padding: 0 0 0 1.2rem;
            color: #1da1f2;
            font-size: 1.08rem;
        }
        .about-highlight {
            background: linear-gradient(90deg, #ff6f61 30%, #1da1f2 100%);
            color: #fff;
            font-weight: 700;
            border-radius: 8px;
            padding: 0.2rem 0.7rem;
            font-size: 1.1rem;
            display: inline-block;
            margin-bottom: 0.7rem;
        }
        </style>
        <div class="about-bg">
            <div class="about-title">🥗 Real-Time Nutrition Intelligence Dashboard</div>
            <div class="about-sub">
                Empowering you with <span class="about-highlight">data-driven food choices</span> and <span class="about-highlight">real-time health insights</span>.
            </div>
            <div class="about-flex">
                <div class="about-section">
                    <h3>🔍 Multi-Source Nutrition Analysis</h3>
                    <ul class="about-feature-list">
                        <li>Integrates <b>Nutritionix</b>, <b>Open Food Facts</b>, and <b>FatSecret</b> APIs</li>
                        <li>Instant nutrition facts for thousands of foods</li>
                        <li>Barcode & product search support</li>
                    </ul>
                </div>
                <div class="about-section">
                    <h3>💬 Social & Consumer Intelligence</h3>
                    <ul class="about-feature-list">
                        <li>Live sentiment from <b>Twitter</b>, <b>Reddit</b>, and <b>YouTube</b></li>
                        <li>Aggregates <b>e-commerce reviews</b> (Amazon, Flipkart)</li>
                        <li>Detects trending health topics & public opinion</li>
                    </ul>
                </div>
                <div class="about-section">
                    <h3>📊 Interactive Power BI Visualizations</h3>
                    <ul class="about-feature-list">
                        <li>Explore nutrition trends & product comparisons</li>
                        <li>Dynamic dashboards for deep-dive analytics</li>
                        <li>Visualize public perception & market sentiment</li>
                    </ul>
                </div>
                <div class="about-section">
                    <h3>👥 Who is it for?</h3>
                    <ul class="about-feature-list">
                        <li>Individuals & families making healthy choices</li>
                        <li>Researchers & nutritionists</li>
                        <li>Health professionals & wellness coaches</li>
                        <li>Product analysts & food brands</li>
                    </ul>
                </div>
            </div>
            <div style="margin-top:2rem; text-align:center; color:#fff; font-size:1.15rem;">
                <b>Built with ❤️ using Python, Streamlit, and Power BI.<br>
                Your one-stop dashboard for <span style="color:#ffe066;">smart, healthy, and informed eating!</span></b>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )