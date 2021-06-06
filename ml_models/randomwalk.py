In [26]: symbol = '.SPX'

In [27]: data = pd.DataFrame(raw[symbol])

In [28]: lags = 5
         cols = []
         for lag in range(1, lags + 1):
             col = 'lag_{}'.format(lag)  1
             data[col] = data[symbol].shift(lag)  2
             cols.append(col)  3

In [29]: data.head(7)
Out[29]:                .SPX    lag_1    lag_2    lag_3    lag_4    lag_5
         Date
         2010-01-01      NaN      NaN      NaN      NaN      NaN      NaN
         2010-01-04  1132.99      NaN      NaN      NaN      NaN      NaN
         2010-01-05  1136.52  1132.99      NaN      NaN      NaN      NaN
         2010-01-06  1137.14  1136.52  1132.99      NaN      NaN      NaN
         2010-01-07  1141.69  1137.14  1136.52  1132.99      NaN      NaN
         2010-01-08  1144.98  1141.69  1137.14  1136.52  1132.99      NaN
         2010-01-11  1146.98  1144.98  1141.69  1137.14  1136.52  1132.99

In [30]: data.dropna(inplace=True)