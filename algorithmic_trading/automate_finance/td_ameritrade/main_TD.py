import pprint
from datetime import datetime
from datetime import timedelta
import pandas as pd


import td_ameritrade.start as start
import td_ameritrade.utils.get_movers as get_movers 

def run(flag):

    # initiate log in/ login and refresh token if needed
    TDSession = start.run()

    if flag == "Mover":
        # gets the movers
        COMPX_df = get_movers.run(TDSession)
        
        return COMPX_df


   

    # TDSession.get_streamer_subscription_keys(accounts=['492476213'])

    # defining streaming session
    TDStreamSession = TDSession.create_streaming_session()

    TDStreamSession.write_behavior(file_path='/Users/anna/Dev/automate_finance/automate_finance/stream_data/data_dump.csv')
    # TDStreamSession.charts(
    #             service='CHART_OPTIONS', 
    #             symbols=['AAPL_040920C115'], 
    #             fields=[0,1,2,3,4,5,6,7]
    #         )

    TDStreamSession.level_one_quotes(symbols=['AAPL'],fields =[2,3])
    TDStreamSession.stream()
    #TDStreamSession.close_stream()
# if __name__ == "__main__":
#     flag = "Mover"

#     COMPX_df = main(flag)