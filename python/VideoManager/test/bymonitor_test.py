#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
import bymonitor.bymonitor as bymonitor

class bymonitorTest(unittest.TestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
	
	def test_bymonitor(self):
		queue = bymonitor.local_task_queue()
		mo = bymonitor.bymonitor(queue)
		
		self.assertFalse(mo.is_running)
		mo.start_monitoring()
		self.assertTrue(mo.is_running)
		
		time.sleep(5)
		task_str = '{"src":"/apps/bypy/test.avi", "dest":"test.mp3"}'
		queue.enqueue(task_str)
		
		time.sleep(10)
		self.assertTrue(mo.is_running)
		mo.stop_monitoring()
		self.assertFalse(mo.is_running)