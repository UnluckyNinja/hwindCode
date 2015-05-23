#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
import mysql.connector
import random
from FileProcessor import FileProcessor
import Config
#from Config import config

class VideoStoreOperator:
	"""docstring for VideoStoreOperator"""

	__config = None

	def __init__(self):
		self.__config = Config.config["ConnectionString"]

	def get_storage_info(self):
		result = []
		cnx = mysql.connector.connect(**self.__config)
		cursor = cnx.cursor()

		query = ("SELECT s.id, s.name, s.container, s.key FROM storages s")

		cursor.execute(query)
		for (id, name, container, key) in cursor:
			storage = Storage(id, name, container, key)
			result.append(storage)

		cursor.close()
		cnx.close()
		return result

	def  create(self, file_path):
		processor = FileProcessor(file_path)
		print "md5"
		print processor.getMD5()
		id = uuid.uuid4().hex

		storage_info = self.get_storage_info()
		storage_len = len(storage_info)

		cnx = mysql.connector.connect(**self.__config)
		cursor = cnx.cursor()

		query = ("INSERT INTO videos "
			"(id, name, size, md5) "
			"VALUES (%s, %s, %s, %s)")
		data_video = (id, processor.name, int(processor.size), processor.getMD5())
		cursor.execute(query, data_video)

		for i in range(processor.chuncks):
			index = random.randint(0, storage_len - 1)
			storage = storage_info[index]
			query = ("INSERT INTO files "
				"(videoId, files.index, storageId, path) "
				"VALUES (%s, %s, %s, %s)")
			data_file = (id, int(i), storage.id, uuid.uuid4().hex)
			cursor.execute(query, data_file)

		cnx.commit()
		cursor.close()
		cnx.close()

		return id

	def get(self, id):
		result = None
		cnx = mysql.connector.connect(**self.__config)
		cursor = cnx.cursor()

		query = ("SELECT v.id, v.name, v.size, v.md5, f.index, f.path, s.name as storagename, s.container, s.key  FROM videos v "
			"left join files f on v.id = f.videoId left join storages s on f.storageId = s.id "
			"WHERE v.id = %s")

		cursor.execute(query, (id,))
		
		video_details = None
		for (id, name, size, md5, index, path, storagename, container, key) in cursor:
			if video_details == None:
				video = Video(id, name, size, md5)
				video_details = VideoDetails(video)

			chunck = Chunck(index, path, storagename, container, key)
			video_details.append_chunck(chunck)

		cursor.close()
		cnx.close()
		return video_details

	def list(self):
		result = []
		cnx = mysql.connector.connect(**self.__config)
		cursor = cnx.cursor()

		query = ("SELECT id, name, size, md5 FROM videos")
		cursor.execute(query)
		
		for (id, name, size, md5) in cursor:
			video = Video(id, name, size, md5)
			result.append(video)

		cursor.close()
		cnx.close()
		return result


	def delete(self, id):
		cnx = mysql.connector.connect(**self.__config)
		cursor = cnx.cursor()
		
		query = ("DELETE FROM files WHERE videoId = %s")
		cursor.execute(query, (id,))

		query = ("DELETE FROM videos WHERE id = %s")
		cursor.execute(query, (id,))

		cnx.commit()
		cursor.close()
		cnx.close()

class Video:
	"""docstring for Video"""
	id = None
	name = None
	size = 0
	md5 = None

	def __init__(self, id, name, size, md5):
		self.id = id
		self.name = name
		self.size = size
		self.md5 = md5

class Chunck:
	"""docstring for Chunck"""

	index = -1
	path = None
	storagename = None
	container = None
	key = None

	def __init__(self, index, path, storagename, container, key):
		self.index = index
		self.path = path
		self.storagename = storagename
		self.container = container
		self.key = key
		
class VideoDetails:
	"""docstring for VideoDetails"""

	video = None
	chuncks = {}

	def __init__(self, video):
		self.video = video
	
	def append_chunck(self, chunck):
		self.chuncks[chunck.index] = chunck

class Storage(object):
	"""docstring for Storage"""

	id = None
	name = None
	container = None
	key = None
	def __init__(self, id, name, container, key):
		self.id = id
		self.name = name
		self.container = container
		self.key = key
		
		