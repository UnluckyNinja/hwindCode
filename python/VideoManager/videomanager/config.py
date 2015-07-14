#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

config = None

def init_config():
	global config
	if config == None:
		fp = open("config/config.json", "r")
		config = json.load(fp)
		fp.close()

def is_encrypt():
	return config["pwd"] != None and config["pwd"] != ""

def get_client_cert_path():
    return config["client_cert"]
    pass
	
	