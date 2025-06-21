# Real-Time Nutrition Intelligence Dashboard

## Features
- Search nutrition info from OpenFoodFacts, Nutritionix, FatSecret
- Scrape and analyze reviews from Amazon, Flipkart
- Social media and trends analysis (Reddit, Twitter, YouTube, Google Trends)
- Power BI dashboard integration

## Setup
1. Clone repo
2. Fill in `.env` with your API keys
3. `docker build -t nutrition_dashboard .`
4. `docker run -p 8501:8501 nutrition_dashboard`
