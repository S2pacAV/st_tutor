import streamlit as st
import yfinance as yf

st.set_page_config(page_title='Apple')

st.title('Данные о котировках компании Apple')


ticker_symbol = 'AAPL'
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(
    period='1d', start='2013-12-12', end='2024-01-01'
)


st.write('''
## Closing price
''')
st.line_chart(ticker_df.Close)

st.write('''
## Volume price
''')
st.line_chart(ticker_df.Volume)
