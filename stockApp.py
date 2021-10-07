import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Select the options from left sidebar to see stockprices and volume of companies
""")
st.sidebar.header('User Input Features')

date=list(range(1,31))
months=list(range(1,12))

st.sidebar.subheader('FROM DATE')
selected_start_date = st.sidebar.selectbox('Start date',date )
selected_start_month = st.sidebar.selectbox('Start month', months)
selected_start_year = st.sidebar.selectbox('Start Year', list(reversed(range(2010,2020))))

st.sidebar.subheader('TO DATE')
selected_end_date= st.sidebar.selectbox('End date', date)
selected_end_month = st.sidebar.selectbox('End month', months)
selected_end_year = st.sidebar.selectbox('End Year', list(reversed(range(selected_start_year,2020))))

st.sidebar.subheader('COMPANY')
companies={'GOOGL', 'AAPL', 'NFLX', 'AMZN', 'MSFT', 'FB', 'NVDA', 'INTC', 'TSLA', 'SPY'}
sorted_company=sorted(companies)
tickerSymbol= st.sidebar.selectbox('Team', sorted_company)
tickerData = yf.Ticker(tickerSymbol)

date_beg=str(selected_start_year)+'-'+str(selected_start_month)+'-'+str(selected_start_date)
date_end=str(selected_end_year)+'-'+str(selected_end_month)+'-'+str(selected_end_date)

tickerDf = tickerData.history(period='1d', start=date_beg, end=date_end)


if st.button('Close Values'):
    st.line_chart(tickerDf.Close)

if st.button('Volume'):
    st.line_chart(tickerDf.Volume)

if st.button('Price to Earning ratio'):
    st.write(tickerData.info["forwardEps"])

if st.button('Regular market Price'):
    st.write(tickerData.info["regularMarketPrice"])

if st.button('Record'):
    st.table(tickerData.history(period="max", interval="3mo"))
