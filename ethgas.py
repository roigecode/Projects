from urllib import response
import config
import requests
import pandas_datareader as web
import datetime as dt

class EthGasFees:
    """
    Esta clase contiene las Gas Fees y el precio de ETH
    """
    # Constructor:
    def __init__(self,_req,_fastest,_fast,_average,_safeLow):
        self.request = _req
        self.fastest = _fastest
        self.fast = _fast
        self.average = _average
        self.safeLow = _safeLow

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
        return round(gwei/10 * ethusd/1000,2)

    # GETTERS:

    # Fastest:
    def get_fastest(self):
        return self.fastest
    
    def get_fastest_usd(self):
        return self.conversor_gwei_usd(self.fastest)

    # Fast:
    def get_fast(self):
        return self.fast
    
    def get_fast_usd(self):
        return self.conversor_gwei_usd(self.fast)

    # Average:
    def get_average(self):
        return self.average
    
    def get_average_usd(self):
        return self.conversor_gwei_usd(self.average)

    # Safe Low:
    def get_safeLow(self):
        return self.safeLow
    
    def get_safeLow_usd(self):
        return self.conversor_gwei_usd(self.safeLow)

    # Printers:
    def display_gwei(self):
        return "\nGWEI >> Fastest: {}  Fast: {}  Average: {}  Safe Low: {}".format(self.get_fastest(), 
                                                                                   self.get_fast(),
                                                                                   self.get_average(), 
                                                                                   self.get_safeLow())

    # 1 ether son 1,000,000,000 Gwei
    def display_usd(self):
        return "\nUDS >> Fastest: {}$  Fast: {}$  Average: {}$  Safe Low: {}$".format(self.get_fastest_usd(),
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
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # Convertimos los datos en json:
    json_resp = req.json()

    # Cogemos los datos:
    fastest = json_resp['fastest']
    fast = json_resp['fast']
    average = json_resp['average']
    safeLow = json_resp['safeLow']

    eth_object = EthGasFees(req,fastest,fast,average,safeLow)

    print(eth_object.display_gwei())
    print(eth_object.display_usd())
