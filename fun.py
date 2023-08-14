import streamlit as st
import yfinance as yf    


st.write("""
# Stock Price of Doosan Corp

Shown is the stocks **Opening Price**, **Closing Price** and ***Daily Volume***

""")
tickerSymbol = '000150.KS'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2018-01-01', end='2023-08-12')
# Open  High  Low   Close   Volume    Dividends   Stock Splits

st.write("""
## Opening Price""")

st.line_chart(tickerDf.Open)
st.write(""" 
## Closing Price""")
st.line_chart(tickerDf.Close)
st.write(""" 
## Daily Volume
""")
st.line_chart(tickerDf.Volume)