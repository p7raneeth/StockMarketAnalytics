import csv
import statistics
import yfinance as yf
import streamlit as st
import numpy as np
import pandas as pd
import sys
import datetime
import time
import matplotlib.pyplot as plt

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

        
        print(data)
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
    

    # col_option = st.multiselect('Select the column to perform Uni-Variate Analysis', ['Open','High', 'Low', 'Close', 'Volume'])
    col_option = st.selectbox('Select the column to perform Uni-Variate Analysis', ['Open','High', 'Low', 'Close', 'Volume'])
    st.write('column:', col_option)
    print('column selection', col_option)
    data = data.loc[:, col_option]
    st.write(data)
    st.line_chart(data)

    
    st.write('Univariate Analysis')
    st.write('Mean', data.values.mean())
    st.write('Median', statistics.median(data.values))
    st.write('Mode', statistics.mode(data.values))
    st.write(f'Min: {min(data.values)} - Max: {max(data.values)}')

