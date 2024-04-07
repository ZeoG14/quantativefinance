import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import pandas as pd
import numpy as np


def download_data(stock, start_date, end_date):
    data = {}
    ticker = yf.download(stock, start_date, end_date)
    data['price'] = ticker['Adj Close']
    return pd.DataFrame(data)


if __name__ == '__main__':
    start_date = datetime.datetime(2010, 4, 2)
    end_date = datetime.datetime(2024, 4, 2)

    stock_data = download_data('IBM', start_date, end_date)

    stock_data['return'] = np.log(stock_data['price'] / stock_data['price'].shift(1))
    stock_data['move'] = np.log(stock_data['price'] - stock_data['price'].shift(1))

    # Average than the 0 values do know count
    stock_data['up'] = np.where(stock_data['move'] > 0, stock_data['move'], 0)
    stock_data['down'] = np.where(stock_data['move'] < 0, stock_data['move'], 0)

    stock_data['average_gain'] = stock_data['up'].rolling(14).mean()
    stock_data['average_loss'] = stock_data['down'].abs().rolling(14).mean()

    rs = stock_data['average_gain'] / stock_data['average_loss']

    stock_data['rsi'] = 100 - (100 / (1.0 + rs))

    stock_data = stock_data.dropna()

    print(stock_data)

    plt.plot(stock_data['rsi'])
    plt.show()
