import streamlit as st
import pandas as pd
import pandas_ta as ta
import yfinance as yf

st.title("Stock Analyzer with pandas_ta")

symbol = st.text_input("Enter Stock Symbol", value="AAPL")
if st.button("Analyze"):
    df = yf.download(symbol, period="6mo", interval="1d")
    
    if df.empty:
        st.error("Failed to fetch data.")
    else:
        df.ta.sma(length=20, append=True)
        st.line_chart(df[['Close', 'SMA_20']])
        st.dataframe(df.tail())
