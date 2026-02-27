

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Forecasting-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Deep%20Learning-LSTM-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/NLP-Sentiment%20Analysis-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Data%20Visualization-Plotly-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Crypto-Bitcoin-yellow?style=for-the-badge&logo=bitcoin" />
</p>

<p align="center">

---

## 🌐 Live Demo

🚀 **Try the AI-Powered Cryptocurrency Intelligence Dashboard here:**

👉 **[Launch Streamlit App](https://ai-powered-crypto-dashboard.streamlit.app/)**

---

# 🚀 AI-Powered Cryptocurrency Intelligence Dashboard 

An end-to-end cryptocurrency analytics platform that integrates **time-series forecasting**, **sentiment analysis**, and **automated trading signal generation** into a unified interactive dashboard.

This project combines **statistical modeling, deep learning, and NLP-based sentiment intelligence** to support data-driven cryptocurrency market decisions.

---

## 📌 Project Overview

The system is designed to:

- 📈 Forecast Bitcoin price trends using multiple models  
- 📰 Analyze real-time news sentiment  
- 🎯 Generate confidence-based trading signals  
- 🔊 Trigger automated audio alerts  
- 📊 Visualize insights through an interactive Streamlit dashboard  

This project demonstrates applied skills in:

- Time-Series Analysis  
- Machine Learning & Deep Learning  
- Natural Language Processing  
- Signal Engineering  
- Full-Stack Data Application Development  

---

## 🧠 System Architecture

```
Yahoo Finance (BTC Data)
            │
            ▼
    Data Preprocessing
            │
            ▼
  Forecasting Engine
 (ARIMA | Prophet | LSTM)
            │
            ▼
     Model Evaluation
   (MAE | RMSE Comparison)
            │
            ▼
     Forecast Visualization
            │
            ▼
 News Sources → NLP Sentiment Engine
            │
            ▼
   Confidence Filtering (>75%)
            │
            ▼
   Trading Signal Generator
 (BUY | SELL | HOLD)
            │
            ▼
     Streamlit Dashboard
            │
     Audio Alerts + Signal Logs
```

---

## 📊 Module 1: Cryptocurrency Forecasting Engine

This module predicts Bitcoin price movements using three different approaches.

### 🔹 ARIMA
- Statistical autoregressive model  
- Captures short-term linear dependencies  
- Serves as baseline forecasting model  

### 🔹 Prophet
- Trend + seasonality modeling  
- Handles missing values and outliers  
- Suitable for financial time-series  

### 🔹 LSTM (Deep Learning)
- Neural network for sequential modeling  
- Captures nonlinear temporal dependencies  
- Uses sliding window time-step training  

### 📈 Model Evaluation Metrics
- **MAE** – Mean Absolute Error  
- **RMSE** – Root Mean Squared Error  

---

## 📰 Module 2: Sentiment Intelligence Engine

This module analyzes cryptocurrency-related news to quantify market sentiment.

### Process Flow

1. Fetch cryptocurrency news  
2. Apply NLP-based sentiment scoring  
3. Normalize sentiment score to range **[-1, +1]**  
4. Compute confidence score  
5. Classify trend as:
   - Positive Trend  
   - Negative Trend  
   - Sideways Trend  

---

## 🎯 Module 3: Trading Signal Generator

Signals are generated using sentiment thresholds and confidence filtering.

| Condition | Signal | Interpretation |
|------------|--------|---------------|
| Sentiment > 0.2 & Confidence > 75% | **BUY** | Strong Positive Trend |
| Sentiment < -0.2 & Confidence > 75% | **SELL** | Strong Negative Trend |
| Otherwise | **HOLD** | Sideways Market |

🔔 Audio alerts are triggered only for high-confidence signals.  
📜 Signal history is stored for tracking and analysis.

---

## 🖥️ Module 4: Interactive Dashboard (Streamlit UI)

The dashboard provides:

- 📈 Live BTC price display  
- 📊 Sentiment gauge visualization  
- 📉 Forecast comparison charts  
- 🎯 Trading signal display  
- 🔊 Automated voice alerts  
- 📜 Signal history logging  

Built using **Streamlit + Plotly** for interactive visualization.

---

## 🛠️ Technology Stack

| Category | Tools Used |
|----------|------------|
| Programming | Python |
| Dashboard | Streamlit |
| Data Processing | Pandas, NumPy |
| Forecasting | ARIMA, Prophet |
| Deep Learning | TensorFlow / Keras (LSTM) |
| NLP | TextBlob / Custom Sentiment Engine |
| Visualization | Plotly |
| Data Source | yfinance |
| Audio Alerts | gTTS |

---

## 📂 Project Structure

```
btc_dashboard/
│
├── data/
│   ├── cleaned_dataset.csv
│   ├── final_training_dataset.csv
│
├── models/
│   ├── arima_model.pkl
│   ├── lstm_model.h5
│
├── pages/
│   ├── 1_Home.py
│   ├── 2_Forecasting.py
│   ├── 3_Model_Comparison.py
│   ├── 4_Sentiment_Intelligence.py
│
├── sentiment_engine.py
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ Installation & Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv btc_env
```

### 2️⃣ Activate Environment (Windows)

```bash
btc_env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🎯 Applications

- Cryptocurrency trading analytics  
- Sentiment-driven investment strategy  
- Quantitative financial research  
- AI-based market forecasting  
- Academic experimentation in time-series modeling  

---

## 🔮 Future Enhancements

- Multi-asset support (ETH, SOL, etc.)  
- Real-time streaming sentiment pipeline  
- Telegram / Email trading alerts  
- Risk-adjusted portfolio optimization  
- Cloud deployment (AWS / Streamlit Cloud)  
- Reinforcement learning trading agent  

---


## 👩‍💻 Author

**Shravani Kavle**  
AI & Data Analytics Enthusiast  
