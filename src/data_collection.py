# src/data_collection.py
import pandas as pd

def create_sample_data():
    data = {
        "review": [
            "I loved the movie! It was amazing.",
            "The film was terrible and boring.",
            "An excellent story with great acting.",
            "Poorly directed and too long.",
            "A masterpiece with emotional depth."
        ],
        "sentiment": ["positive", "negative", "positive", "negative", "positive"]
    }
    df = pd.DataFrame(data)
    df.to_csv("data/movie_reviews.csv", index=False)
    print("✅ Data collected and saved to data/movie_reviews.csv")

if __name__ == "__main__":
    create_sample_data()