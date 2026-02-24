import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("📊 Market Overview")

btc = yf.download("BTC-USD", period="6mo", interval="1d", progress=False)
btc.reset_index(inplace=True)
btc.columns = [col[0] if isinstance(col, tuple) else col for col in btc.columns]

latest_price = btc["Close"].iloc[-1]
change_pct = ((btc["Close"].iloc[-1] - btc["Close"].iloc[-2]) / btc["Close"].iloc[-2]) * 100

col1, col2 = st.columns(2)
col1.metric("Current BTC Price", f"${latest_price:,.2f}")
col2.metric("24h Change", f"{change_pct:.2f}%")

fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=btc["Date"],
    open=btc["Open"],
    high=btc["High"],
    low=btc["Low"],
    close=btc["Close"],
    name="BTC"
))

fig.update_layout(
    template="plotly_dark",
    height=600
)

st.plotly_chart(fig, width="stretch")
