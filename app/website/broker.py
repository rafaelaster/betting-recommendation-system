from datetime import time
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
import pandas as pd
from typing import dict

class CasinoApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data: dict[int , pd.DataFrame] ={}
        self.contracts: dict[int, Contract] = {}

    def get_historical_data(self, reqId:int , contract:Contract) -> pd.DataFrame:
        self.data[reqId] = pd.DataFrame(columns=['event_type' , 'event_group'])
        self.data[reqId].set_index('event_type' , inplace=True)
        self.contracts[reqId] = contract
        self.historicalData()
        return self.data[reqId]
    
#Overriding get_historical_data method to create queue bar 
    def historicalData(self, reqId, bar):

        empty_dataframe = self.data[reqId]
        #popularte empty dataframe
        empty_dataframe.loc[ pd.DataFrame(bar.date , unit="s"), ["event_type" , "event_group"]] = [bar.event_type , bar.event_group]
        df = df.astype(str)
        self.data[reqId] = df








