
import numpy as np
import pandas as pd
import datetime as dt
from pylab import mpl, plt
from itertools import product
from sklearn.linear_model import LinearRegression

# import simple_trade.utils.general_utils as utils

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

def sma(raw,symbol):
    """
    [
    Simple Moving Average (SMA) is a commonly used trading strategy. Mathematically speaking, SMA calculates the average of a selected range of prices, ususally closing prices, by the number of periods in that range.
    
    The trading rules for this are the following:
    
    * Go long (=+1) when the shorter SMA is above the longer SMA.
    * Go short (=-1) when the shorter SMA is below the longer SMA.
    
    ]

    Args:
        file_path (str): [path to csv with financial data]
    """


    print(raw)
    print(raw.info())

    data = (pd.DataFrame(raw[symbol]).dropna())

    print(data)

    SMA1 = 42  
    SMA2 = 252  

    data['SMA1'] = data[symbol].rolling(SMA1).mean()  
    data['SMA2'] = data[symbol].rolling(SMA2).mean()  
    data.plot(figsize=(10, 6))
    #utils.save_image(fig)
    plt.show()

    data.dropna(inplace=True)
    data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
    data.tail()
    ax = data.plot(secondary_y='Position', figsize=(10, 6))
    ax.get_legend().set_bbox_to_anchor((0.25, 0.85))
    #utils.save_image(fig)
    plt.show()

    # vectorized backtesting
    data['Returns'] = np.log(data[symbol] / data[symbol].shift(1))
    data['Strategy'] = data['Position'].shift(1) * data['Returns']
    print(data.round(4).head())
    print(np.exp(data[['Returns', 'Strategy']].sum()))
    print(data[['Returns', 'Strategy']].std() * 252 ** 0.5)

    data.dropna(inplace=True)

    ax = data[['Returns', 'Strategy']].cumsum().apply(np.exp).plot(figsize=(10, 6))
    data['Position'].plot(ax=ax, secondary_y='Position', style='--')
    ax.get_legend().set_bbox_to_anchor((0.25, 0.85))
    plt.show()
    

def optimization(raw,symbol):

    sma1 = range(20, 61, 4)  
    sma2 = range(180, 281, 10)


    results = pd.DataFrame()
    for SMA1, SMA2 in product(sma1, sma2):  
        data = pd.DataFrame(raw[symbol])
        data.dropna(inplace=True)
        data['Returns'] = np.log(data[symbol] / data[symbol].shift(1))
        data['SMA1'] = data[symbol].rolling(SMA1).mean()
        data['SMA2'] = data[symbol].rolling(SMA2).mean()
        data.dropna(inplace=True)
        data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
        data['Strategy'] = data['Position'].shift(1) * data['Returns']
        data.dropna(inplace=True)
        perf = np.exp(data[['Returns', 'Strategy']].sum())
        results = results.append(pd.DataFrame(
                    {'SMA1': SMA1, 'SMA2': SMA2,
                    'MARKET': perf['Returns'],
                    'STRATEGY': perf['Strategy'],
                    'OUT': perf['Strategy'] - perf['Returns']},
                    index=[0]), ignore_index=True)

    print(results.info())
    print(results.sort_values('OUT', ascending=False).head(7))


def random_walk_hypothesis(raw,symbol):

    data = pd.DataFrame(raw[symbol])
    lags = 5
    cols = []
    for lag in range(1, lags + 1):
        col = 'lag_{}'.format(lag)  
        data[col] = data[symbol].shift(lag)  
        cols.append(col)

    data.head(7)    
    data.dropna(inplace=True)
    reg = np.linalg.lstsq(data[cols], data[symbol], rcond=-1)[0]
    reg.round(3)
    
    plt.figure(figsize=(10, 6))
    plt.bar(cols, reg)
    plt.show()

    data['Prediction'] = np.dot(data[cols], reg)
    data[[symbol, 'Prediction']].iloc[-75:].plot(figsize=(10, 6))
    plt.show()

    return


def linear_OLS_regression(raw,symbol):

    data = pd.DataFrame(raw[symbol])
    data['returns'] = np.log(data / data.shift(1))
    data.dropna(inplace=True)
    data['direction'] = np.sign(data['returns']).astype(int)
    print(data.head())
    
    data['returns'].hist(bins=35, figsize=(10, 6))
    plt.show()
    
    lags = 2
    def create_lags(data):
        global cols
        cols = []
        for lag in range(1, lags + 1):
            col = 'lag_{}'.format(lag)
            data[col] = data['returns'].shift(lag)
            cols.append(col)
    
    create_lags(data)

    print(data.head())
    data.dropna(inplace=True)

    data.plot.scatter(x='lag_1', y='lag_2', c='returns', 
                  cmap='coolwarm', figsize=(10, 6), colorbar=True)
    plt.axvline(0, c='r', ls='--')
    plt.axhline(0, c='r', ls='--')
    plt.show()

    return data


def regression(data):

    model = LinearRegression()
    
    data['pos_ols_1'] = model.fit(data[cols], data['returns']).predict(data[cols])




    return
if __name__ == "__main__":
    file_path = '../data/tr_eikon_eod_data.csv'
    raw = pd.read_csv(file_path, index_col=0, parse_dates=True)
    symbol = 'AAPL.O'

    #sma(raw,symbol)
    #optimization(raw,symbol)
    #random_walk_hypothesis(raw,symbol = '.SPX')

    
    raw = pd.read_csv('http://hilpisch.com/tr_eikon_eod_data.csv',
                  index_col=0, parse_dates=True).dropna()
    
    data = linear_OLS_regression(raw,symbol = 'EUR=')
    regression(data)
                  

    

