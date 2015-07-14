#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import test.encrypt_test as encrypt_test
import test.pyVideoClient_test as pyVideoClient_test

suite = unittest.TestLoader().loadTestsFromTestCase(encrypt_test.EncryptTest)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(pyVideoClient_test.pyVideoClientTest)
unittest.TextTestRunner(verbosity=2).run(suite)