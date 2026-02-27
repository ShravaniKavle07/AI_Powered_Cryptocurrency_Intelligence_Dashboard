import streamlit as st
import yfinance as yf
from gtts import gTTS
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from sentiment_engine import get_news_sentiment

st.title("📰 News-Based Market Sentiment")

# ---------------------------------------------------
# 1️⃣ Fetch BTC Data
# ---------------------------------------------------

btc = yf.download("BTC-USD", period="1mo", progress=False)
btc.reset_index(inplace=True)
btc.columns = [col[0] if isinstance(col, tuple) else col for col in btc.columns]

# ---------------------------------------------------
# 2️⃣ Get Sentiment Score
# ---------------------------------------------------

sentiment_score = get_news_sentiment()   # assumed range: -1 to +1

# Simulated confidence logic (you can replace with real confidence from NLP model)
confidence_score = min(abs(sentiment_score) + 0.5, 1.0)

# ---------------------------------------------------
# 3️⃣ Generate Finance-Friendly Signal
# ---------------------------------------------------

def generate_signal(sentiment_score, confidence):

    if confidence < 0.75:
        return "HOLD", "Sideways Trend"

    if sentiment_score > 0.2:
        return "BUY", "Positive Trend"
    elif sentiment_score < -0.2:
        return "SELL", "Negative Trend"
    else:
        return "HOLD", "Sideways Trend"

signal, trend_label = generate_signal(sentiment_score, confidence_score)

# ---------------------------------------------------
# 4️⃣ Display Metrics
# ---------------------------------------------------

col1, col2 = st.columns(2)
col1.metric("📰 News Sentiment Index", round(sentiment_score, 3))
col2.metric("Latest BTC Price", f"${btc['Close'].iloc[-1]:,.2f}")

# ---------------------------------------------------
# 5️⃣ Sentiment Gauge
# ---------------------------------------------------

st.subheader("Market Sentiment Gauge")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=sentiment_score * 100,
    title={"text": trend_label},
    gauge={
        "axis": {"range": [-100, 100]},
        "bar": {"color": "green" if sentiment_score > 0 else "red"},
        "steps": [
            {"range": [-100, -20], "color": "lightcoral"},
            {"range": [-20, 20], "color": "lightgray"},
            {"range": [20, 100], "color": "lightgreen"}
        ],
    }
))

st.plotly_chart(fig, width="stretch")

# ---------------------------------------------------
# 6️⃣ Trading Signal Display
# ---------------------------------------------------

st.subheader("📈 Trading Signal")

if signal == "BUY":
    st.success("🟢 BUY — Positive Trend")
elif signal == "SELL":
    st.error("🔴 SELL — Negative Trend")
else:
    st.warning("🟡 HOLD — Sideways Trend")

# ---------------------------------------------------
# 7️⃣ Audio Alert (Only If Confidence > 75%)
# ---------------------------------------------------

def play_signal_audio(signal, confidence):

    if signal == "BUY":
        text = f"Strong buy signal detected. Market shows a positive trend with {int(confidence*100)} percent confidence."
    
    elif signal == "SELL":
        text = f"Strong sell signal detected. Market shows a negative trend with {int(confidence*100)} percent confidence."
    
    else:
        text = f"Market is moving sideways with {int(confidence*100)} percent confidence."

    tts = gTTS(text=text, lang="en")
    tts.save("signal_audio.mp3")

    audio_file = open("signal_audio.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")


# Trigger only for strong signals and avoid repetition
if confidence_score > 0.75:

    if "last_signal" not in st.session_state:
        st.session_state.last_signal = None

    if signal != st.session_state.last_signal:
        play_signal_audio(signal, confidence_score)
        st.session_state.last_signal = signal

# ---------------------------------------------------
# 8️⃣ Signal History Log
# ---------------------------------------------------

if "signal_history" not in st.session_state:
    st.session_state.signal_history = pd.DataFrame(
        columns=["Timestamp", "Sentiment Score", "Confidence", "Signal"]
    )

new_entry = pd.DataFrame([{
    "Timestamp": datetime.now(),
    "Sentiment Score": sentiment_score,
    "Confidence": confidence_score,
    "Signal": signal
}])

if st.session_state.signal_history.empty:
    st.session_state.signal_history = new_entry
else:
    st.session_state.signal_history = pd.concat(
        [st.session_state.signal_history, new_entry],
        ignore_index=True
    )

st.subheader("📜 Signal History Log")

st.dataframe(st.session_state.signal_history.tail(10))
