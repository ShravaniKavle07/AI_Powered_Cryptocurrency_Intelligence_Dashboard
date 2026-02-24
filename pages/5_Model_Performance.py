import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⚙️ Model Performance")

metrics = pd.read_csv("data/05_model_metrics.csv")

fig = px.bar(
    metrics,
    x="Model",
    y="RMSE",
    text="RMSE",
    template="plotly_dark"
)

st.plotly_chart(fig, width="stretch")
