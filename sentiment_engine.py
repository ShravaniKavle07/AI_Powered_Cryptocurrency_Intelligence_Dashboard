import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st

analyzer = SentimentIntensityAnalyzer()


@st.cache_data(ttl=600)  # cache for 10 minutes
def get_news_sentiment():

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=bitcoin OR crypto&"
        f"language=en&"
        f"sortBy=publishedAt&"
        f"pageSize=30&"
        f"apiKey={st.secrets['NEWS_API_KEY']}"
    )

    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])

    if not articles:
        return 0

    scores = []

    for article in articles:
        text = (article["title"] or "") + " " + (article["description"] or "")
        sentiment = analyzer.polarity_scores(text)["compound"]
        scores.append(sentiment)

    return sum(scores) / len(scores)


def generate_signal(price_series, sentiment_index):

    price_return = price_series.pct_change().iloc[-1]

    if sentiment_index > 0.25 and price_return > 0:
        return "🟢 STRONG BUY"
    elif sentiment_index < -0.25 and price_return < 0:
        return "🔴 STRONG SELL"
    elif sentiment_index > 0:
        return "🟢 BUY"
    elif sentiment_index < 0:
        return "🔴 SELL"
    else:
        return "⚪ HOLD"
