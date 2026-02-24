import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("🔮 Forecasting Models")

forecast = pd.read_csv("data/04_forecast_results.csv", parse_dates=["Date"])

model = st.selectbox("Select Model", ["ARIMA", "Prophet", "LSTM"])

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=forecast["Date"],
    y=forecast["Actual"],
    name="Actual"
))

fig.add_trace(go.Scatter(
    x=forecast["Date"],
    y=forecast[f"{model}_Pred"],
    name=f"{model} Prediction"
))

fig.update_layout(template="plotly_dark", height=600)

st.plotly_chart(fig, width="stretch")
