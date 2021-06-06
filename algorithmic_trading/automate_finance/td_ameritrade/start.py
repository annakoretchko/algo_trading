# Import the client
from td_ameritrade.td.client import TDClient
from td_ameritrade.config.secrets import CLIENT_ID, REDIRECT_URI , JSON_PATH ,ACCOUNT_NUMBER
import pprint
from datetime import datetime
from datetime import timedelta

def run():

    """[Initiates the login or gets new token if needed. Sourced from:
    https://github.com/areed1192/td-ameritrade-python-api]

    Returns:
        [TDSession]: [Part of TDClient Class that is logged in and ready to
         get functions for data selection]
    """
    TDSession = TDClient(
                    client_id=CLIENT_ID,
                    redirect_uri=REDIRECT_URI,
                    account_number=ACCOUNT_NUMBER,
                    credentials_path=JSON_PATH
                )



    # Login to the session
    TDSession.login()


    return TDSession


