import streamlit as st
import yfinance as yf
import pandas as pd
import random

st.set_page_config(layout="wide")

st.title("🤖 Crypto AI Assistant")

# ==============================
# Load Live BTC Data (Safe Mode)
# ==============================
@st.cache_data(ttl=60)
def load_data():
    data = yf.download("BTC-USD", period="5d", progress=False)

    # Handle multi-index columns (yfinance issue)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()
    return data


btc = load_data()

if not btc.empty and len(btc) > 1:
    latest_price = float(btc["Close"].iloc[-1])
    previous_price = float(btc["Close"].iloc[-2])
    price_change = ((latest_price - previous_price) / previous_price) * 100
else:
    latest_price = 0.0
    price_change = 0.0


# ==============================
# Chat Memory
# ==============================
if "messages" not in st.session_state:
    st.session_state.messages = []


# ==============================
# Display Previous Messages
# ==============================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ==============================
# AI Brain Logic
# ==============================
def crypto_brain(user_input):
    text = user_input.lower()

    if "price" in text:
        return f"📈 Current BTC price is **${latest_price:,.2f}** with a 24h change of {price_change:.2f}%."

    elif "arima" in text:
        return "ARIMA is a statistical time-series model capturing trend and autoregressive patterns. Best for linear structures."

    elif "prophet" in text:
        return "Prophet is designed for time series with strong seasonality and trend changes. Easy to tune and robust."

    elif "lstm" in text:
        return "LSTM is a deep learning recurrent neural network capable of modeling nonlinear temporal dependencies."

    elif "volatility" in text:
        return "Volatility measures how much price fluctuates. High volatility = higher risk & reward."

    elif "sentiment" in text:
        return "Sentiment analysis evaluates news & social data. Positive sentiment often supports bullish moves."

    elif "signal" in text or "buy" in text or "sell" in text:
        if price_change > 0:
            return "📊 Momentum looks bullish. Confirm with sentiment and volume before entering."
        else:
            return "📊 Short-term weakness detected. Consider risk management."

    elif "hello" in text or "hi" in text:
        return "Hello 👋 I'm your Crypto AI Assistant. Ask me about price, models, volatility or signals."

    else:
        return random.choice([
            "Ask about price, ARIMA, Prophet, LSTM, volatility or signals.",
            "Do you want model explanation or live market data?",
            "I'm specialized in crypto forecasting and analytics."
        ])


# ==============================
# Chat Input
# ==============================
if prompt := st.chat_input("Ask about crypto models, price, signals..."):

    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    response = crypto_brain(prompt)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)