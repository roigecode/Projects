from urllib import response
import config
import requests
import pandas_datareader as web
import datetime as dt

# @Author: roigecode
# Este archivo nos permite obtener las Gas Fees de Ethereum desde diversas fuentes.

"""
Sample Output:
--------------
DefiPulse (2022-02-12 14:20:54.983972) || GWEI >> Fast: 53.0  Average: 44.0  Safe Low: 38.0
DefiPulse (2022-02-12 14:20:54.983972) || UDS >> Fast: 1.55$  Average: 1.28$  Safe Low: 1.11$

Etherscan (2022-02-12 14:20:57.379089) || GWEI >> Fast: 40.0  Average: 39.0  Safe Low: 38.133289166
Etherscan (2022-02-12 14:20:57.379089) || UDS >> Fast: 1.17$  Average: 1.14$  Safe Low: 1.11$
"""

class EthGasFees:

    #Esta clase contiene las Gas Fees y el precio de ETH:

    # Constructor:
    def __init__(self,_resource,_req,_fast=0,_average=0,_safeLow=0):
        # De momento no uso el req pero se hará:
        self.resource = _resource
        self.request = _req
        # Dividir entre 10, docs:
        self.fast = float(_fast)
        self.average = float(_average)
        self.safeLow = float(_safeLow)
        # Fecha y hora de la llamada:
        self.datetime = dt.datetime.now()

    # Get Eth Price:
    def get_eth_usd(self):
        # Cogemos la fecha de ayer y la de hoy:
        dia_anterior = dt.datetime.now() - dt.timedelta(1)
        actual_time = dt.datetime.now()

        # Leemos el precio de ETH-USD:
        eth_price_pandas_Series = web.DataReader('ETH-USD', 'yahoo', dia_anterior, actual_time)
        closes = eth_price_pandas_Series['Close'].values
        close = closes[1]

        # Convertimos el valor a flotante y lo retornamos:
        return float(close)

    # Conversor de gwei a usd:
    def conversor_gwei_usd(self,gwei):
        ethusd = self.get_eth_usd()
        return round(gwei * ethusd/100000,2)

    # GETTERS:
    def get_resource(self):
        return self.resource

    def get_datetime(self):
        return self.datetime

    # Fast:
    def get_fast(self):
        if self.get_resource() == "Etherscan":
            return self.fast
        elif self.get_resource() == "DefiPulse":
            return self.fast/10
    
    def get_fast_usd(self):
        if self.get_resource() == "Etherscan":
            return self.conversor_gwei_usd(self.get_fast())
        elif self.get_resource() == "DefiPulse":
            return self.conversor_gwei_usd(self.get_fast())
        
    # Average:
    def get_average(self):
        if self.get_resource() == "Etherscan":
            return self.average
        elif self.get_resource() == "DefiPulse":
            return self.average/10
    
    def get_average_usd(self):
        return self.conversor_gwei_usd(self.get_average())

    # Safe Low:
    def get_safeLow(self):
        if self.get_resource() == "Etherscan":
            return self.safeLow
        elif self.get_resource() == "DefiPulse":
            return self.safeLow/10
    
    def get_safeLow_usd(self):
        return self.conversor_gwei_usd(self.get_safeLow())

    # Printers:
    def display_gwei(self):
        return "\n{} ({}) || GWEI >> Fast: {}  Average: {}  Safe Low: {}".format(
                                                                            self.get_resource(),
                                                                            self.get_datetime(),
                                                                            self.get_fast(),
                                                                            self.get_average(), 
                                                                            self.get_safeLow())

    # 1 ether son 1,000,000,000 Gwei
    def display_usd(self):
        return "{} ({}) || UDS >> Fast: {}$  Average: {}$  Safe Low: {}$".format(
                                                                           self.get_resource(),
                                                                           self.get_datetime(),
                                                                           self.get_fast_usd(),
                                                                           self.get_average_usd(),
                                                                           self.get_safeLow_usd())

# -------- #
# PROGRAMA #
# -------- #

if __name__ == "__main__":
    # If we get <200> = Success, <404> Not Found, else Generic Error:
    try:
        req = requests.get("https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json?api-key={}".format(config.API_KEY))
        req_etherscan = requests.get("https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={}".format(config.API_ETHERSCAN))
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


    # ----------- #
    # DEFI-PULSE: #
    # ----------- #

    # Convertimos los datos en json:
    json_resp = req.json()

    # Cogemos los datos:
    fast_defipulse = json_resp['fast']
    average_defipulse = json_resp['average']
    safeLow_defipulse = json_resp['safeLow']

    eth_defipulse = EthGasFees("DefiPulse",req,fast_defipulse,average_defipulse,safeLow_defipulse)

    print(eth_defipulse.display_gwei())
    print(eth_defipulse.display_usd())


    # ---------- #
    # ETHERSCAN: #
    # ---------- #

    json_resp2 = req_etherscan.json()

    fast_etherscan = json_resp2['result']['FastGasPrice']
    average_etherscan = json_resp2['result']['ProposeGasPrice']
    safeLow_etherscan = json_resp2['result']['suggestBaseFee']

    eth_etherscan = EthGasFees("Etherscan",req,fast_etherscan,average_etherscan,safeLow_etherscan)

    print(eth_etherscan.display_gwei())
    print(eth_etherscan.display_usd())