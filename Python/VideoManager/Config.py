#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

config = None

def init_config():
	global config
	if config == None:
		fp = open("config.json", "r")
		config = json.load(fp)
		fp.close()
	
	