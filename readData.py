import csv

import yfinance as yf

def get_data(ticker_list):
    """    
    function to get data 
    """
    data = yf.download(tickers=' '.join(ticker_list),
                       period='ytd',
                       group_by='ticker',
                       auto_adjust = True,
                       prepost = True,
                       threads = True,)
    return(data)
lst = ['SPY', 'AAPL']
data = get_data(lst) 