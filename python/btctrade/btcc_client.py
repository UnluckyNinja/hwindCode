#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
import time
import requests
import urllib.parse

class Market(Enum):
    All = "all"
    BtcCny = "btccny"
    LtcCny = "ltccny"
    LtcBtc = "ltcbtc"



class btcc_client (object):
    """a wrapper for btcc trade info"""

    

    def __init__(self, market=Market.BtcCny):
        if (not isinstance(market, Market)):
            raise ValueError("market is not defined")

        self._base_url = "https://data.btcchina.com/data/"
        self._market = market


    @property
    def market(self):
        return self._market
    
    def _request_and_return(self, url):
        ret = None
        try:
            result = requests.get(url)
            if (result.status_code == 200):
                ret = result.json()
        except:
            pass
        finally:
            return ret

    def get_current_price(self):
        url = urllib.parse.urljoin(self._base_url, "ticker?market="+self._market.value)
        return self._request_and_return(url)

    def get_last_24hr_trade(self):
        url = urllib.parse.urljoin(self._base_url, "trades?market="+self._market.value)
        return self._request_and_return(url)

    def get_trade_history_since_time(self, time, limit=100):
        if (limit < 0 or limit > 5000):
            raise ValueError("limit should between 0 and 5000")
        if (time > int(time.time()):
            raise ValueError("since time should be a past datetime")

        url = urllib.parse.urljoin(self._base_url, "historydata?market="+self._market.value+"&since="+time+"&limit="+limit+"&sincetype=time")
        return self._request_and_return(url)

    def get_trade_history_since_id(self, id, limit=100):
        if(limit < 0 or limit > 5000):
            raise ValueError("limit should between 0 and 5000")

        url = urllib.parse.urljoin(self._base_url, "historydata?market="+self._market.value+"&since="+id+"&limit="+limit)
        return self._request_and_return(url)


a = btcc_client()
print(a.get_current_price())
print(a.get_current_price(Market.BtcCny))

