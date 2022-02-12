from statistics import mean
from urllib import response
from time import sleep
from alive_progress import alive_bar
from itsdangerous import json
import config
import requests
import pandas_datareader as web
import datetime as dt

# @Author: roigecode
# Este archivo nos permite obtener las Gas Fees de Ethereum desde diversas fuentes.

"""

TO DO: Apply Parallel Requests, one API call does not have to wait until other is finished!

Sample Output:
--------------
DefiPulse (2022-02-12 16:38:46.922449) || GWEI >> Fast: 107.0  Average: 81.0  Safe Low: 70.0
DefiPulse (2022-02-12 16:38:46.922449) || UDS >> Fast: 3.08$  Average: 2.33$  Safe Low: 2.01$

Etherscan (2022-02-12 16:38:46.922478) || GWEI >> Fast: 69.0  Average: 69.0  Safe Low: 67.94
Etherscan (2022-02-12 16:38:46.922478) || UDS >> Fast: 1.98$  Average: 1.98$  Safe Low: 1.95$

GasWatch (2022-02-12 16:38:46.922558) || GWEI >> Fast: 106.0  Average: 80.0  Safe Low: 72.0
GasWatch (2022-02-12 16:38:46.922558) || UDS >> Fast: 3.05$  Average: 2.3$  Safe Low: 2.07$

Gas station (2022-02-12 16:38:46.922564) || GWEI >> Fast: 119.0  Average: 79.0  Safe Low: 69.0
Gas station (2022-02-12 16:38:46.922564) || UDS >> Fast: 3.42$  Average: 2.27$  Safe Low: 1.98$

MyCrypto (2022-02-12 16:38:46.922570) || GWEI >> Fast: 101.0  Average: 80.0  Safe Low: 72.0
MyCrypto (2022-02-12 16:38:46.922570) || UDS >> Fast: 2.9$  Average: 2.3$  Safe Low: 2.07$

POA Network (2022-02-12 16:38:46.922576) || GWEI >> Fast: 91.0  Average: 74.5  Safe Low: 58.0
POA Network (2022-02-12 16:38:46.922576) || UDS >> Fast: 2.62$  Average: 2.14$  Safe Low: 1.67$

··· Calculating Mean ···

Result: USD >> Fast: 2.84$  Average: 2.22$  Safe Low: 1.96$

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
        if self.get_resource() == "DefiPulse":
            return round(self.fast/10,2)
        else:
            return round(self.fast,2)
    
    def get_fast_usd(self):
        return self.conversor_gwei_usd(self.get_fast())
        
    # Average:
    def get_average(self):
        if self.get_resource() == "DefiPulse":
            return round(self.average/10,2)
        else:
            return round(self.average,2)
    
    def get_average_usd(self):
        return self.conversor_gwei_usd(self.get_average())

    # Safe Low:
    def get_safeLow(self):
        if self.get_resource() == "DefiPulse":
            return round(self.safeLow/10,2)
        else:
            return round(self.safeLow,2)
    
    def get_safeLow_usd(self):
        return self.conversor_gwei_usd(self.get_safeLow())

    # Displays:
    def display_gwei(self):
        return "\n{} ({}) || GWEI >> Fast: {}  Average: {}  Safe Low: {}".format(
                                                                            self.get_resource(),
                                                                            self.get_datetime(),
                                                                            self.get_fast(),
                                                                            self.get_average(), 
                                                                            self.get_safeLow())

    # 1 ether son 1,000,000,000 Gwei
    def display_usd(self):
        return "\n{} ({}) || UDS >> Fast: {}$  Average: {}$  Safe Low: {}$".format(
                                                                           self.get_resource(),
                                                                           self.get_datetime(),
                                                                           self.get_fast_usd(),
                                                                           self.get_average_usd(),
                                                                           self.get_safeLow_usd())
    def display_both(self):
        return self.display_gwei() + self.display_usd()

# -------- #
# PROGRAMA #
# -------- #

if __name__ == "__main__":
    # If we get <200> = Success, <404> Not Found, else Generic Error:

    object_list = []

    try:
        req_defipulse = requests.get("https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json?api-key={}".format(config.API_DEFIPULSE))
        req_etherscan = requests.get("https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={}".format(config.API_ETHERSCAN))
        req_gaswatch = requests.get("https://ethgas.watch/api/gas")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


    # ----------- #
    # DEFI-PULSE: #
    # ----------- #

    # Convertimos los datos en json:
    json_resp = req_defipulse.json()

    # Cogemos los datos:
    fast_defipulse = json_resp['fast']
    average_defipulse = json_resp['average']
    safeLow_defipulse = json_resp['safeLow']

    eth_defipulse = EthGasFees("DefiPulse",req_defipulse,fast_defipulse,average_defipulse,safeLow_defipulse)
    object_list.append(eth_defipulse)

    # ---------- #
    # ETHERSCAN: #
    # ---------- #

    json_resp2 = req_etherscan.json()

    fast_etherscan = json_resp2['result']['FastGasPrice']
    average_etherscan = json_resp2['result']['ProposeGasPrice']
    safeLow_etherscan = json_resp2['result']['suggestBaseFee']

    eth_etherscan = EthGasFees("Etherscan",req_etherscan,fast_etherscan,average_etherscan,safeLow_etherscan)
    object_list.append(eth_etherscan)

    # ----------------------------------#
    # ETH GAS WATCH - MULTIPLE SOURCES: #
    # --------------------------------- #

    json_resp3 = req_gaswatch.json()

    fast_gaswatch = json_resp3['fast']['gwei']
    average_gaswatch = json_resp3['normal']['gwei']
    safeLow_gaswatch = json_resp3['slow']['gwei']

    eth_gaswatch = EthGasFees("GasWatch",req_gaswatch,fast_gaswatch,average_gaswatch,safeLow_gaswatch)
    object_list.append(eth_gaswatch)

    # ------------ #
    # GAS STATION: #
    # ------------ #

    # - From prior API Call: -

    gas_station = json_resp3['sources'][1]
    fast_gas_station = gas_station['fast']
    average_gas_station = gas_station['standard']
    safeLow_gas_station = gas_station['slow']

    eth_gas_station = EthGasFees(gas_station['name'],req_gaswatch,fast_gas_station,average_gas_station,safeLow_gas_station)
    object_list.append(eth_gas_station)

    # --------- #
    # MYCRIPTO: #
    # --------- #

    # - From prior API Call: -

    mycrypto = json_resp3['sources'][2]
    fast_mycrypto = mycrypto['fast']
    average_mycrypto = mycrypto['standard']
    safeLow_mycrypto = mycrypto['slow']

    eth_mycrypto = EthGasFees(mycrypto['name'],req_gaswatch,fast_mycrypto,average_mycrypto,safeLow_mycrypto)
    object_list.append(eth_mycrypto)

    # ------- #
    # UPVEST: #
    # ------- #

    # - From prior API Call: -

    upvest = json_resp3['sources'][3]
    fast_upvest = upvest['fast']
    average_upvest = (upvest['fast'] + upvest['slow'])/2
    safeLow_upvest = upvest['slow']

    eth_upvest = EthGasFees(upvest['name'],req_gaswatch,fast_upvest,average_upvest,safeLow_upvest)
    object_list.append(eth_upvest)

    # ------- #
    # PRINTS: #
    # ------- #
    
    for o in object_list:
        print(o.display_both())
    
    mean_slow, mean_avg, mean_fast = 0,0,0

    print("\n··· Calculating Mean ···\n")

    for o in object_list:
        mean_slow += round(o.get_safeLow_usd(),2)
        mean_avg += round(o.get_average_usd(),2)
        mean_fast += round(o.get_fast_usd(),2)
    
    mean_slow /= len(object_list)
    mean_avg /= len(object_list)
    mean_fast /= len(object_list)

    print(f"Result: USD >> Fast: {round(mean_fast,2)}$  Average: {round(mean_avg,2)}$  Safe Low: {round(mean_slow,2)}$\n")