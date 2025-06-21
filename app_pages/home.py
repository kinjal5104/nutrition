import streamlit as st

def run():
    st.markdown(
        """
        <style>
        .main-home-bg {
            background: linear-gradient(135deg, #1da1f2 0%, #ff6f61 100%);
            border-radius: 22px;
            padding: 3.2rem 2.8rem 2.8rem 2.8rem;
            margin: 2.5rem auto 2rem auto;
            max-width: 1300px;
            min-width: 350px;
            box-shadow: 0 4px 32px #0002;
        }
        .main-home-title {
            font-size: 3.1rem;
            font-weight: 900;
            letter-spacing: 1px;
            color: #fff;
            margin-bottom: 0.7rem;
            text-align: center;
            text-shadow: 0 2px 8px #0002;
        }
        .main-home-sub {
            font-size: 1.35rem;
            color: #fff;
            margin-bottom: 2.2rem;
            text-align: center;
        }
        .main-home-highlight {
            background: linear-gradient(90deg, #ff6f61 30%, #1da1f2 100%);
            color: #fff;
            font-weight: 700;
            border-radius: 8px;
            padding: 0.2rem 0.7rem;
            font-size: 1.1rem;
            display: inline-block;
            margin-bottom: 0.7rem;
        }
        .main-home-flex {
            display: flex;
            flex-wrap: wrap;
            gap: 2.2rem;
            justify-content: space-between;
            margin-top: 2.2rem;
            margin-bottom: 2.2rem;
        }
        .main-home-section {
            flex: 1 1 350px;
            background: rgba(255,255,255,0.93);
            border-radius: 14px;
            padding: 1.7rem 1.3rem;
            margin-bottom: 1.2rem;
            box-shadow: 0 2px 12px #0001;
            min-width: 320px;
        }
        .main-home-section h3 {
            margin-top: 0;
            color: #1da1f2;
            font-size: 1.25rem;
            font-weight: 800;
        }
        .main-home-feature-list {
            margin: 0.7rem 0 0 0;
            padding: 0 0 0 1.2rem;
            color: #ff6f61;
            font-size: 1.08rem;
        }
        .main-home-quickstart {
            background: rgba(29,161,242,0.12);
            border-left: 5px solid #1da1f2;
            border-radius: 10px;
            padding: 1.1rem 1.3rem;
            margin: 1.5rem 0 1.2rem 0;
            font-size: 1.08rem;
            color: #222;
        }
        .main-home-cta {
            text-align: center;
            margin-top: 2.2rem;
            color: #fff;
            font-size: 1.18rem;
        }
        </style>
        <div class="main-home-bg">
            <div class="main-home-title">🥗 Real-Time Nutrition Intelligence Dashboard</div>
            <div class="main-home-sub">
                Welcome to your all-in-one platform for <span class="main-home-highlight">nutrition analysis</span>, <span class="main-home-highlight">consumer sentiment</span>, and <span class="main-home-highlight">market trends</span>.<br>
                <span style="font-size:1.13rem; color:#ffe066;">Empowering you to make smarter, healthier, and more informed food choices!</span>
            </div>
            <div class="main-home-flex">
                <div class="main-home-section">
                    <h3>🚀 What can you do here?</h3>
                    <ul class="main-home-feature-list">
                        <li>Search any packaged food and get instant nutrition facts</li>
                        <li>Compare products across brands and categories</li>
                        <li>See live reviews and trending opinions from Amazon, Flipkart, Twitter, Reddit, and YouTube</li>
                        <li>Visualize nutrition and sentiment trends with interactive Power BI dashboards</li>
                    </ul>
                </div>
                <div class="main-home-section">
                    <h3>🌟 Why use this dashboard?</h3>
                    <ul class="main-home-feature-list">
                        <li>Make healthy, data-driven food decisions</li>
                        <li>Spot trending products and health topics in real time</li>
                        <li>Analyze consumer sentiment and market perception</li>
                        <li>Perfect for individuals, families, nutritionists, researchers, and brands</li>
                    </ul>
                </div>
                <div class="main-home-section">
                    <h3>🧑‍💻 How does it work?</h3>
                    <ul class="main-home-feature-list">
                        <li>Integrates APIs: Nutritionix, Open Food Facts, FatSecret, Amazon, Flipkart, Twitter, Reddit, YouTube</li>
                        <li>Aggregates and analyzes data instantly</li>
                        <li>Beautiful, interactive visualizations powered by Power BI</li>
                    </ul>
                </div>
            </div>
            <div class="main-home-quickstart">
                <b>Quick Start:</b><br>
                <ol>
                    <li>Type a food or product name in the search bar.</li>
                    <li>Explore nutrition facts, reviews, and social trends.</li>
                    <li>Use the dashboard tabs to dive deeper into analytics and comparisons.</li>
                </ol>
            </div>
            <div class="main-home-cta">
                <b>Ready to discover your next healthy choice?<br>
                Start exploring now and unlock the power of real-time nutrition intelligence!</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )