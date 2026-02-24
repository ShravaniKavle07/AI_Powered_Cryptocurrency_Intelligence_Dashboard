import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📉 Volatility Analysis")

data = pd.read_csv("data/02_clean_historical.csv", parse_dates=["Date"])
data["Returns"] = data["Close"].pct_change()
data["Volatility"] = data["Returns"].rolling(30).std()

fig = px.line(data, x="Date", y="Volatility", template="plotly_dark")

st.plotly_chart(fig, width="stretch")
