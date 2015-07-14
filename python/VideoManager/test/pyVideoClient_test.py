#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import videomanager.pyVideoClient as pyVideoClient


class pyVideoClientTest(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test_storage_get(self):
        client = pyVideoClient.pyVideoClient()
        storages = client.getStorageInfo()
        print(storages)
        for s in storages:
            print("id={0}, name={1}, container={2}, key={3}".format(s["id"], s["name"], s["container"], s["key"]))