#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import io
import time
import azure
from azure.storage.blob import BlobService
from azure.common import AzureHttpError
import pdb

from time import gmtime, strftime

from datetime import datetime
from btcc_client import btcc_client
from btcc_client import huobi_client
from btcc_client import Market
from btcc_log import create_timed_rotating_log

class huobi_trade_collector(object):

    def __init__(self, config):
        self._config = config
        self._type = self._config["type"]
        #self._market = Market(self._config["market"])
        #self._client = btcc_client(self._market)
        self._client = huobi_client()
        self._interval = self._config["interval"]
        self._schema = self._config["schema"]

        self._prefix = self._config["prefix"]
        self._account_name = self._config["account_name"]
        self._account_key = self._config["account_key"]
        self._container = self._config["container"]
        self._writer = azure_storage_writer(self._account_name, self._account_key, self._container, self._prefix)
        self._logger = create_timed_rotating_log()

    def _process_cur_price_result(self, result):
        self._logger.info("Begin process the current price result")
        ret = None
        try:
            values = []
            timestamp = int(result["time"])
            values.append(str(timestamp))
            for i in range(0, len(self._schema)):
                key = self._schema[i]
                if (key in result["ticker"]):
                    value = str(result["ticker"][key])
                    values.append(value)
                else:
                    values.append("")
            ret = (timestamp, '\t'.join(values))
            self._writer.write_log(ret)
        except Exception as e:
            self._logger.warn("Hit an Exception " + str(e))
            pass
        finally:
            return ret

    def run(self):
        while (True):
            self._logger.info("Start a new round with type:" + self._type)
            if (self._type == "cur_price"):
                ret = self._client.get_current_price()
                if (ret == None):
                    continue
                entity = self._process_cur_price_result(ret)
                if (entity == None):
                    continue

            elif (self._type == "24hr_trade"):
                pass
            elif (self._type == "trade_history"):
                pass

            elif (self._type == "cur_order"):
                pass

            elif (self._type == "cur_price_and_order"):
                pass
            else:
                break
            time.sleep(self._interval)


class btcc_trade_collector (object):
    """btcc trade extractor"""

    def __init__(self, config):
        self._config = config
        self._type = self._config["type"]
        self._market = Market(self._config["market"])
        self._client = btcc_client(self._market)
        self._interval = self._config["interval"]
        self._schema = self._config["schema"]

        self._prefix = self._config["prefix"]
        self._account_name = self._config["account_name"]
        self._account_key = self._config["account_key"]
        self._container = self._config["container"]
        self._writer = azure_storage_writer(self._account_name, self._account_key, self._container, self._prefix)
        self._logger = create_timed_rotating_log()


    def run(self):
        if (self._type == "trade_history"):
            last_id = self._config["start_id"]

        while (True):
            self._logger.info("Start a new round with type:" + self._type)
            if (self._type == "cur_price"):
                ret = self._client.get_current_price()
                if (ret == None):
                    continue
                entity = self._process_cur_price_result(ret)
                if (entity == None):
                    continue

            elif (self._type == "24hr_trade"):
                pass
            elif (self._type == "trade_history"):
                ret = self._client.get_trade_history_since_id(last_id)
                if (ret == None):
                    continue
                max_id = self._process_trade_history_result(ret)
                if (max_id == None):
                    continue
                else:
                    last_id = max_id

            elif (self._type == "cur_order"):
                ret = self._client.get_current_order()
                if (ret == None):
                    continue
                entity = self._process_cur_order_result(ret)
                if (entity == None):
                    continue

            elif (self._type == "cur_price_and_order"):
                price = self._client.get_current_price()
                if (price == None):
                    continue
                order = self._client.get_current_order()
                if (order == None):
                    continue
                entity = self._process_cur_price_and_order_result(price, order)
                if (entity == None):
                    continue

            else:
                break
            time.sleep(self._interval)

    def _process_trade_history_result(self, result):
        self._logger.info("Begin process the trade history")
        max_id = None
        try:
            if (len(result) == 0):
                return
            for i in range(0, len(result)):
                timestamp = result[i]["date"]
                price = str(result[i]["price"])
                amount = str(result[i]["amount"])
                tid = str(result[i]["tid"])
                type_str = str(result[i]["type"])
                values = [str(timestamp), price, amount, tid, type_str]
                ret = (timestamp, "\t".join(values))
                self._writer.write_log(ret)
                if (max_id == None or (max_id != None and max_id < int(tid))):
                    max_id = int(tid)
        except Exception as e:
            self._logger.warn("Hit an Exception " + str(e))
            pass
        finally:
            return max_id

        pass

    def _process_cur_order_result(self, result):
        self._logger.info("Begin process the current order result")
        ret = None
        try:
            values = []
            timestamp = result["date"]
            asks = result["asks"]
            for i in range(0, len(asks)):
                price = str(asks[i][0])
                amount = str(asks[i][1])
                values = [str(timestamp), "asks", price, amount]
                ret = (timestamp, "\t".join(values))
                self._writer.write_log(ret)

            bids = result["bids"]
            for i in range(0, len(bids)):
                price = str(bids[i][0])
                amount = str(bids[i][1])
                values = [str(timestamp), "bids", price, amount]
                ret = (timestamp, "\t".join(values))
                self._writer.write_log(ret)
        except Exception as e:
            self._logger.warn("Hit an Exception " + str(e))
            pass
        finally:
            return ret

    def _process_cur_price_result(self, result):
        self._logger.info("Begin process the current price result")
        ret = None
        try:
            #jobj = json.loads(result)
            values = []
            for i in range(0, len(self._schema)):
                key = self._schema[i]
                if (key in result["ticker"]):
                    value = str(result["ticker"][key])
                    values.append(value)
                else:
                    values.append("")
            timestamp = result["ticker"]["date"]
            ret = (timestamp, '\t'.join(values))
            self._writer.write_log(ret)
        except Exception as e:
            self._logger.warn("Hit an Exception " + str(e))
            pass
        finally:
            return ret

    def _process_cur_price_and_order_result(self, price, order):
        #pdb.set_trace()
        self._logger.info("Begin process the current price and order result")
        ret = None
        try:
            values = []
            for i in range(0, len(self._schema)):
                key = self._schema[i]
                if (key in price["ticker"]):
                    value = str(price["ticker"][key])
                    values.append(value)
                else:
                    values.append("")

            price_timestamp = price["ticker"]["date"]
            order_timestamp = order["date"]
            timestamp = price_timestamp
            if (abs(order_timestamp - price_timestamp) >= 5):
                return None

            #pdb.set_trace()
            order_lists = [("asks", order["asks"]), ("bids", order["bids"])]
            for order_tuple in order_lists:
                order_type = order_tuple[0]
                order_list = order_tuple[1]
                tmp = []
                for i in range(0, len(order_list)):
                    cur_price = order_list[i][0]
                    amount = order_list[i][1]
                    tmp.append([str(order_timestamp), order_type, cur_price, amount])
                if (order_type == "asks"):
                    tmp = sorted(tmp, key= lambda x: x[2])
                else:
                    tmp = sorted(tmp, key= lambda x: x[2], reverse=True)
                for i in range(0, len(tmp)):
                    item_value = values.copy()
                    item_value.append(tmp[i][0])
                    item_value.append(tmp[i][1])
                    item_value.append(str(i))
                    item_value.append(str(tmp[i][2]))
                    item_value.append(str(tmp[i][3]))
                    ret = (timestamp, "\t".join(item_value))
                    self._writer.write_log(ret)
        except Exception as e:
            self._logger.warn("Hit an Exception " + str(e))
            return None
        finally:
            return ret

class azure_storage_writer (object):
    """storage operation wrapper, desiged for writing logs to storage"""

    def __init__(self, account_name, account_key, container, prefix):
        self._blob = BlobService(account_name=account_name, account_key=account_key)
        self._cur_path = None
        self._buf = io.StringIO()
        self._prefix = prefix
        self._container = container
        self._blob.create_container(container)
        self._logger = create_timed_rotating_log()

    def write_log(self, entity):
        path = self._get_path(entity[0])
        if (self._cur_path == None):
            self._cur_path = path
        elif(self._cur_path != path):
            self._dump_buf_to_storage()
            self._buf.close()
            self._buf = io.StringIO()
            self._cur_path = path
        self._buf.write(entity[1])
        self._buf.write("\n")

    def close(self):
        if (self._cur_path != None):
            self._dump_buf_to_storage()
            self._buf.close()

    def _dump_buf_to_storage(self):
        self._logger.info("Begin dump to azure blob")
        loop = 0;
        while True:
            try:
                self._blob.put_block_blob_from_text(self._container,self._cur_path, self._buf.getvalue())
                break
            except AzureHttpError as e:
                self._logger.warn("Hit an AzureHttpError " + str(e))
                self._logger.warn("Retry times: {0}".format(loop))
                loop = loop + 1
                if loop >= 3:
                    raise e
            except Exception as e:
                self._logger.warn("Hit an Exception " + str(e))
                raise e
        self._logger.info("Dump to azure blob succeeded.")

    def _get_path(self, timestamp):
        #timestamp = int(timestamp)
        d = datetime.fromtimestamp(int(timestamp))
        part = str.format("logs-part-{}.txt", d.minute // 5)
        path_str = d.strftime('%Y-%m-%d/%H')
        return str.format("{}/{}/{}", self._prefix, path_str, part)