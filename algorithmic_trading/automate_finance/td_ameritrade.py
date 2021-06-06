# import requests
# import json

# # import secrets


# # td_consumer_key = secrets.CONSUMER_KEY

# ### Good Resource: https://github.com/areed1192/td-ameritrade-python-api/blob/master/td/client.py ####




# ##### GET NON ACCOUNT DATA #####
# def stock_quote():

#     endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/quotes?'

#     full_url = endpoint.format(stock_ticker='AAL')
#     page = requests.get(url=full_url,
#                         params={'apikey' : td_consumer_key})
#     content = json.loads(page.content)
#     print(content)


# def historical_price():

#     endpoint = 'https://api.tdameritrade.com/v1/marketdata/{stock_ticker}/pricehistory'

#     full_url = endpoint.format(stock_ticker='AAL')
#     page = requests.get(url=full_url,
#                         params={'apikey' : td_consumer_key})
#     content = json.loads(page.content)
#     print(content)


# def fundemental_data():

#     base_url = 'https://api.tdameritrade.com/v1/instruments?&symbol={stock_ticker}&projection={projection}'
#     endpoint = base_url.format(stock_ticker = 'AAL',
#         projection = 'fundamental')
#     page = requests.get(url=endpoint, 
#                 params={'apikey' : td_consumer_key})
#     content = json.loads(page.content)
#     print(content)


# def options_data():
#     base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}'
#     endpoint = base_url.format(stock_ticker = 'AAL')
#     page = requests.get(url=endpoint, 
#                 params={'apikey' : td_consumer_key})
#     content = json.loads(page.content)
#     print(content)

# def specific_option():

#     base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}&contractType={contractType}&fromDate={date}&toDate={date}'
#     endpoint = base_url.format(stock_ticker = 'AAL',
#         contractType = 'PUT',
#         date='2021-11-20')
#     page = requests.get(url=endpoint, 
#                 params={'apikey' : td_consumer_key})
#     content = json.loads(page.content)
#     print(content)

# def specific_option2():

#     base_url = 'https://api.tdameritrade.com/v1/marketdata/chains?&symbol={stock_ticker}\
# &contractType={contract_type}&strike={strike}&fromDate={date}&toDate={date}'
#     endpoint = base_url.format(stock_ticker = 'AAL',
#         contract_type = 'PUT',
#         strike = 9,
#         date='2021-06-30')
#     page = requests.get(url=endpoint, 
#                 params={'apikey' : td_consumer_key})
#     content = json.loads(page.content)
#     print(content)


# def get_movers():
#     #Can be $DJI, $COMPX, or $SPX.X.
#     base_url = "https://api.tdameritrade.com/v1/marketdata/{index}/movers"
#     endpoint = base_url.format( index='$COMPX',
#                     direction='down',
#                     change='percent')
#     page = requests.get(url=endpoint, 
#                 params={'apikey' : td_consumer_key})
#     content = json.loads(page.content)
#     print(content)




# ##### GET ACCOUNT DATA #####
# def get_account():
#     base_url = "https://api.tdameritrade.com/v1/accounts/{accountId}"

#     endpoint = base_url.format( accountId=secrets.ACCOUNT_ID,
#                     fields=['orders','positions'])
#     page = requests.get(url=endpoint, 
#                 params={'apikey' : td_consumer_key})
#     print(endpoint)
#     content = json.loads(page.content)
#     print(content)


# if __name__ == "__main__":

#     ##### GET NON ACCOUNT DATA #####
#     #stock_quote()
#     #historical_price()
#     #fundemental_data()
#     #options_data()
#     # specific_option()
#     #specific_option2()
#     #get_movers()

#     ##### GET ACCOUNT DATA #####
#     get_account()