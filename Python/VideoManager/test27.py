#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import test.bymonitor_test as bymonitor_test

suite = unittest.TestLoader().loadTestsFromTestCase(bymonitor_test.bymonitorTest)
unittest.TextTestRunner(verbosity=2).run(suite)