import streamlit as st
import praw
import tweepy
from googleapiclient.discovery import build

# --- Reddit ---
def fetch_reddit_mentions(product_name, limit=5):
    reddit = praw.Reddit(
        client_id=st.secrets["REDDIT_CLIENT_ID"],
        client_secret=st.secrets["REDDIT_SECRET"],
        user_agent=st.secrets["REDDIT_USER_AGENT"]
    )
    results = []
    try:
        for submission in reddit.subreddit('all').search(product_name, limit=limit, sort='top'):
            if submission.score > 0:
                results.append({
                    'platform': 'Reddit',
                    'user': submission.author.name if submission.author else 'unknown',
                    'text': submission.title.strip(),
                    'engagement': f"⬆️ {submission.score} upvotes"
                })
    except Exception as e:
        print("Reddit Error:", e)
    return results

# --- Twitter ---
def fetch_twitter_mentions(product_name, max_results=10):
    bearer_token = st.secrets["TWITTER_BEARER_TOKEN"]
    client = tweepy.Client(bearer_token=bearer_token)
    results = []
    try:
        tweets = client.search_recent_tweets(
            query=product_name,
            max_results=max_results,
            tweet_fields=['public_metrics', 'author_id']
        )
        if tweets.data:
            for tweet in tweets.data:
                likes = tweet.public_metrics.get('like_count', 0)
                if likes > 0:
                    results.append({
                        'platform': 'Twitter',
                        'user': f"User-{tweet.author_id}",
                        'text': tweet.text.strip(),
                        'engagement': f"❤️ {likes} likes"
                    })
    except Exception as e:
        print("Twitter Error:", e)
    return results

# --- YouTube ---
def fetch_youtube_comments(product_name, max_results=3):
    api_key = st.secrets["YOUTUBE_API_KEY"]
    youtube = build('youtube', 'v3', developerKey=api_key)
    results = []
    try:
        search_response = youtube.search().list(
            q=product_name,
            part='id,snippet',
            maxResults=2
        ).execute()
        for item in search_response.get('items', []):
            video_id = item['id'].get('videoId')
            if video_id:
                comments_response = youtube.commentThreads().list(
                    videoId=video_id,
                    part='snippet',
                    order='relevance',
                    maxResults=max_results
                ).execute()
                for comment in comments_response.get('items', []):
                    snippet = comment['snippet']['topLevelComment']['snippet']
                    text = snippet.get('textDisplay', '').strip()
                    if text:
                        results.append({
                            'platform': 'YouTube',
                            'user': snippet.get('authorDisplayName', 'unknown'),
                            'text': text,
                            'engagement': f"👍 {snippet.get('likeCount', 0)} likes"
                        })
    except Exception as e:
        print("YouTube Error:", e)
    return results

# --- Aggregator ---
def get_social_data(product_name):
    data = []
    data.extend(fetch_reddit_mentions(product_name))
    data.extend(fetch_twitter_mentions(product_name))
    data.extend(fetch_youtube_comments(product_name))
    return data
