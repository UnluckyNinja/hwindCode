#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
import json
import time
import requests
import urllib.parse
from btcc_log import create_timed_rotating_log

class Market(Enum):
    All = "all"
    BtcCny = "btccny"
    LtcCny = "ltccny"
    LtcBtc = "ltcbtc"


class huobi_client(object):

    def __init__(self):
        self._logger = create_timed_rotating_log()
        self._base_url = "http://api.huobi.com/staticmarket/"

    def _request_and_return(self, url, payload={}):
        self._logger.info("Web request. url:{0}, payload:{1}".format(url, json.dumps(payload)))
        ret = None
        try:
            result = requests.get(url, params=payload)
            if (result.status_code == 200):
                self._logger.info("Web request succeeded")
                ret = result.json()
        except Exception as e:
            self._logger.warn(str(e))
        finally:
            return ret

    def get_current_price(self):
        url = urllib.parse.urljoin(self._base_url, "ticker_btc_json.js")
        return self._request_and_return(url)


class btcc_client (object):
    """a wrapper for btcc trade info"""

    def __init__(self, market=Market.BtcCny):
        if (not isinstance(market, Market)):
            raise ValueError("market is not defined")

        self._base_url = "https://data.btcchina.com/data/"
        self._market = market
        self._logger = create_timed_rotating_log()

    @property
    def market(self):
        return self._market

    def _request_and_return(self, url, payload={}):
        self._logger.info("Web request. url:{0}, payload:{1}".format(url, json.dumps(payload)))
        payload["market"] = self._market.value
        ret = None
        try:
            result = requests.get(url, params=payload)
            if (result.status_code == 200):
                self._logger.info("Web request succeeded")
                ret = result.json()
        except Exception as e:
            self._logger.warn(str(e))
        finally:
            return ret

    def get_current_price(self):
        url = urllib.parse.urljoin(self._base_url, "ticker")
        return self._request_and_return(url)

    def get_last_24hr_trade(self):
        url = urllib.parse.urljoin(self._base_url, "trades")
        return self._request_and_return(url)

    def get_trade_history_since_time(self, start_time, limit=100):
        if (limit < 0 or limit > 5000):
            raise ValueError("limit should between 0 and 5000")
        if (start_time > int(time.time())):
            raise ValueError("since time should be a past datetime")

        payload = {}
        payload["since"] = start_time
        payload["limit"] = limit
        payload["sincetype"] = "time"
        url = urllib.parse.urljoin(self._base_url, "historydata")

        print(start_time)
        return self._request_and_return(url, payload)

    def get_trade_history_since_id(self, id, limit=100):
        if (limit < 0 or limit > 5000):
            raise ValueError("limit should between 0 and 5000")

        payload = {}
        payload["since"] = id
        payload["limit"] = limit
        print(payload)
        url = urllib.parse.urljoin(self._base_url, "historydata")
        return self._request_and_return(url, payload)

    def get_current_order(self, limit=None):
        payload = {}
        if (limit != None):
            if (limit < 0):
                raise ValueError("limit should be great than 0")
            else:
                payload["limit"] = limit

        url = urllib.parse.urljoin(self._base_url, "orderbook")
        return self._request_and_return(url, payload)