import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import pandas as pd


def download_data(stock, start_date, end_date):
    data = {}
    ticker = yf.download(stock, start_date, end_date)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)


def construct_signals(data, short_period, long_period):
    data['Short SMA'] = data['Price'].rolling(window=short_period).mean()
    data['Long SMA'] = data['Price'].rolling(window=long_period).mean()


def plot_data(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Price'], label='Stock Price', color='black')
    plt.plot(data['Short SMA'], label='Short MA', color='red')
    plt.plot(data['Long SMA'], label='Long MA', color='blue')
    plt.title('Moving Average (MA) Indicators')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.show()


if __name__ == '__main__':
    start_date = datetime.datetime(2010, 4, 2)
    end_date = datetime.datetime(2024, 4, 2)

    stock_data = download_data('IBM', start_date, end_date)
    construct_signals(stock_data, 50, 200)
    stock_data = stock_data.dropna()
    plot_data(stock_data)
