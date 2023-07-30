import streamlit as st
import yfinance as yf
import datetime

st.write("""
            # Stock Price Analyzer """)

## get data from apple

symbol = "AAPL"

option = st.selectbox(
    'Which Stock would you want to analyze?',
    ('AAPL', 'GOOG', 'TSLA','MSFT'))

st.write('You selected:', option)

col1,col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter start date", datetime.date(2019, 7, 6))

with col2:
    end_date = st.date_input("Please enter end date", datetime.date(2019, 7, 6))


ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period = "1d",start = start_date,end = end_date)

st.write(f"""
         ### {symbol}'s Stock price data """)

st.dataframe(ticker_df)

st.write(f"""
         # {symbol}'s Closing Price Chart """)

st.line_chart(ticker_df["Close"])

st.write(f"""
         # {symbol}'s Volume Chart """)

st.line_chart(ticker_df["Volume"])



