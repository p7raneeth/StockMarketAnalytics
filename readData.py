import csv
import yfinance as yf
import streamlit as st
import numpy as np
import pandas as pd
import sys
import datetime
import time

def get_data(ticker_list, from_date, to_date):
    """    
    function to get data as per the ticker selected within the specified time ran
    """
    try:
        data = yf.download(tickers=ticker_list,
                        period='ytd',
                        group_by='ticker',
                        auto_adjust = True,
                        prepost = True,
                        threads = True,)

        data = data[from_date:to_date]
    except:
        print(sys.exc_info()[0])
    return(data)


if __name__ == '__main__':
    st.write('Hello welcome to the Stock Market Analytics Web App!!')
    today = datetime.date.today()
    def_start_date = time.strftime('%Y-%m-1')
    def_start_date = datetime.datetime.strptime(def_start_date, '%Y-%m-%d')
    option = st.selectbox('Please choose the stock tickers you are interested to Analyze', ['SPY', 'AAPL', 'AMZN'])
    from_date = st.date_input('from date', (def_start_date))
    to_date = st.date_input('to date', )
    st.write('You have selected:', option)
    data = get_data(''.join(option), from_date, to_date)
    st.write(data)