#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import test.encrypt_test as encrypt_test

suite = unittest.TestLoader().loadTestsFromTestCase(encrypt_test.EncryptTest)
unittest.TextTestRunner(verbosity=2).run(suite)