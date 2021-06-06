import pprint
from datetime import datetime
from datetime import timedelta
import datetime
import pandas as pd
import sys
import xlwt
import matplotlib.pyplot as plt


import td_ameritrade.start as start
import td_ameritrade.utils.get_movers as get_movers 


def run():

    # initiate log in/ login and refresh token if needed
    TDSession = start.run()

    v = (TDSession.get_price_history(symbol = 'AAPL',
                                period_type = 'year',
                                period = '1',
                                #start_date = 1464148800000,
                                #end_date = 1464825600000,
                                frequency_type = 'daily',
                                frequency = '1',
                                extended_hours = True))
    

    # to df
    df = pd.DataFrame(v['candles'])
    # edit datetime
    df['datetime'] = pd.to_datetime(df['datetime'],unit='ms')
    # plot
    df = df.set_index(['datetime'])
    print(df)
    df.plot(y = ['low','close','high'])
    plt.show()

 
