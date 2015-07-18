#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os

config = None

def init_config():
    global config
    if config == None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fp = open(os.path.join(base_dir, "config/config.json"), "r")
        config = json.load(fp)
        fp.close()

def is_encrypt():
    return config["pwd"] != None and config["pwd"] != ""

def get_client_cert_path():
    return config["client_cert"]
    pass
    
    