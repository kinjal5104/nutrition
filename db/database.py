from sqlalchemy import create_engine
import os

engine = create_engine(os.getenv("DATABASE_URL"))

def save_nutrition_data(data):
    # Save to DB
    pass

def save_reviews(data):
    # Save to DB
    pass

def save_social_data(data):
    # Save to DB
    pass
