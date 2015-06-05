#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
import json
import collections
import bypy.bypy as bypy


SCAN_INTERVAL = 3

class bymonitor:
	def __init__(self, queue):
		self.__by = bypy.ByPy(bypy.DefaultSliceSize, bypy.DefaultDlChunkSize)
		self.__queue = queue
		self.__running = False
	
	@property
	def is_running(self):
		return self.__running
	
	def start_monitoring(self):
		if self.__running == True:
			return
		self.__t = threading.Thread(target=self.do)
		self.__t.start()
		
	
	def stop_monitoring(self):
		self.__running = False
		self.__t.join(30)
		if self.__t.isAlive() == True:
			self.__t.close()
	
	def get_task_from_queue(self):
		task_str = self.__queue.dequeue()
		if task_str != None:
			return json.loads(task_str)
		return None
	
	def exe_task(self, task):
		print "task execution start"
		self.__by.downfile(task["src"], task["dest"])
		print "task execution done"
	
	def scan(self):
		print "scanning"
		pass
	
	def do(self):
		self.__running = True
		while self.__running:
			try:			
				task = self.get_task_from_queue()
				if task == None:
					self.scan()
				else:
					self.exe_task(task)
					continue
			except Exception as e:
				print e
			time.sleep(SCAN_INTERVAL)

class task_queue:
	def dequeue(self):
		raise NotImplementedError()
	
	def enqueue(self, msg):
		raise NotImplementedError()

class local_task_queue(task_queue):
	def __init__(self):
		self.__buf = collections.deque([])
	
	def dequeue(self):
		if len(self.__buf) > 0:
			return self.__buf.popleft()
		return None
	
	def enqueue(self, msg):
		self.__buf.append(msg)

class azure_task_queue(task_queue):
	def __init__(self):
		pass
	
	def dequeue(self):
		raise NotImplementedError()
	
	def enqueue(self, msg):
		raise NotImplementedError()