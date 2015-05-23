#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import hashlib
import Config

class FileProcessor:
	"""docstring for FileProcessor"""

	name = None
	size = 0
	chuncks = 0
	__file_path = None

	__CHUNCK_SIZE = 0

	def __init__(self, file_path):
		self.__file_path = file_path
		self.name = os.path.basename(file_path)
		self.size = os.path.getsize(file_path)
		FileProcessor.__CHUNCK_SIZE = Config.config["ChunckSizeMB"] * 1024 * 1024

		if self.size % FileProcessor.__CHUNCK_SIZE == 0:
			self.chuncks = self.size // FileProcessor.__CHUNCK_SIZE
		else:
			self.chuncks = self.size // FileProcessor.__CHUNCK_SIZE + 1

	
	def getMD5(self):
		md5 = hashlib.md5()
		f = open(self.__file_path, "rb")
		while True:
			data = f.read(2**20)
			if not data:
				break
			md5.update(data)
		f.close()
		return md5.hexdigest()

	def get_chunck(self, index):
		if index < 0 or index >= self.chuncks:
			return None

		f = open(self.__file_path, "rb")
		f.seek(index * FileProcessor.__CHUNCK_SIZE)


		if index == self.chuncks - 1:
			buf = f.read()
		else:
			buf = f.read(FileProcessor.__CHUNCK_SIZE)

		f.close()
		return buf

