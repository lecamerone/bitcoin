#function to download prices

import gdax
import pandas as pd
from datetime import datetime
import datetime
import numpy as np
import matplotlib.pyplot as plt
from dateutil import parser
import warnings
warnings.filterwarnings("ignore")

#returns an array of histoical prices
def prices():
    #df column names
    client = gdax.PublicClient()
    #download historic data
    BTC = client.get_product_historic_rates('BTC-USD', granularity=60*60*24)
    ETH = client.get_product_historic_rates('ETH-USD', granularity=60*60*24)
    LTC = client.get_product_historic_rates('LTC-USD', granularity=60*60*24)
    #make into individual data frames
    column_names = [ 'time', 'low', 'high', 'open', 'close', 'volume' ]

    BTC = pd.DataFrame(BTC,columns = column_names)
    ETH = pd.DataFrame(ETH,columns = column_names)
    LTC = pd.DataFrame(LTC,columns = column_names)
    #reverse order and re-index
    BTC = BTC.iloc[::-1]
    BTC = BTC.reset_index(drop=True)
    ETH = ETH.iloc[::-1]
    ETH = ETH.reset_index(drop=True)
    LTC = LTC.iloc[::-1]
    LTC = LTC.reset_index(drop=True)

    prices_arr = pd.DataFrame()
    prices_arr['BTC'] = BTC.close
    prices_arr['ETH'] = ETH.close
    prices_arr['LTC'] = LTC.close


    return prices_arr

#prints prices
def plot_prices():
    df = prices()
    plt.plot(df.BTC)
    plt.plot(df.ETH)
    plt.plot(df.LTC)
    plt.show()
