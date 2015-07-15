#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
import mysql.connector
import random
import pdb
import videomanager.fileprocessor as fileprocessor
import videomanager.config as config
import videomanager.pyVideoClient as pyVideoClient

class VideoStoreOperator:
    """docstring for VideoStoreOperator"""

    __config = None

    def __init__(self):
        self.__config = config.config["ConnectionString"]

    def get_storage_info(self):
        result = []
        client = pyVideoClient.pyVideoClient()
        storages = client.getStorageInfo()
        for s in storages:
            storage = Storage(s["id"], s["name"], s["container"], s["key"])
            result.append(storage)
        # cnx = mysql.connector.connect(**self.__config)
        # cursor = cnx.cursor()

        # query = ("SELECT s.id, s.name, s.container, s.key FROM storages s")

        # cursor.execute(query)
        # for (id, name, container, key) in cursor:
        #     storage = Storage(id, name, container, key)
        #     result.append(storage)

        # cursor.close()
        # cnx.close()
        return result

    def  create(self, file_path):
        processor = fileprocessor.FileProcessor(file_path)
        video = Video("", processor.name, int(processor.size), processor.md5)
        client = pyVideoClient.pyVideoClient()
        ret = client.createVideo(video)
        if ret == None:
            return None
        return ret["id"]
        # id = uuid.uuid4().hex

        # storage_info = self.get_storage_info()
        # storage_len = len(storage_info)

        # cnx = mysql.connector.connect(**self.__config)
        # cursor = cnx.cursor()

        # query = ("INSERT INTO videos "
        #     "(id, name, size, md5) "
        #     "VALUES (%s, %s, %s, %s)")
        # data_video = (id, processor.name, int(processor.size), processor.md5)
        # cursor.execute(query, data_video)

        # for i in range(processor.chuncks):
        #     index = random.randint(0, storage_len - 1)
        #     storage = storage_info[index]
        #     query = ("INSERT INTO files "
        #         "(videoId, files.index, storageId, path) "
        #         "VALUES (%s, %s, %s, %s)")
        #     data_file = (id, int(i), storage.id, uuid.uuid4().hex)
        #     cursor.execute(query, data_file)

        # cnx.commit()
        # cursor.close()
        # cnx.close()

        # return id

    def get(self, id):
        result = None
        client = pyVideoClient.pyVideoClient()
        storages = client.getStorageInfo()

        data = client.getVideo(id)
        if data == None:
            return None


        video_data = data["video"]
        vf_data = data["video_files"]
        video = Video(video_data["id"], video_data["name"], video_data["size"], video_data["md5"])
        video_details = VideoDetails(video)

        for f in vf_data:
            for s in storages:
                if s["id"] == f["storageid"]:
                    chunck = Chunck(f["index"], f["path"], s["name"], s["container"], s["key"])
                    video_details.append_chunck(chunck)
                    break

        return video_details

        # cnx = mysql.connector.connect(**self.__config)
        # cursor = cnx.cursor()

        # query = ("SELECT v.id, v.name, v.size, v.md5, f.index, f.path, s.name as storagename, s.container, s.key  FROM videos v "
        #     "left join files f on v.id = f.videoId left join storages s on f.storageId = s.id "
        #     "WHERE v.id = %s")

        # cursor.execute(query, (id,))
        
        # video_details = None
        # for (id, name, size, md5, index, path, storagename, container, key) in cursor:
        #     if video_details == None:
        #         video = Video(id, name, size, md5)
        #         video_details = VideoDetails(video)

        #     chunck = Chunck(index, path, storagename, container, key)
        #     video_details.append_chunck(chunck)

        # cursor.close()
        # cnx.close()
        # return video_details

    def list(self):
        result = []
        client = pyVideoClient.pyVideoClient()
        videos = client.getVideoList()
        for v in videos:
            video = Video(v["id"], v["name"], v["size"], v["md5"])
            result.append(video)
        # cnx = mysql.connector.connect(**self.__config)
        # cursor = cnx.cursor()

        # query = ("SELECT id, name, size, md5 FROM videos order by name")
        # cursor.execute(query)
        
        # for (id, name, size, md5) in cursor:
        #     video = Video(id, name, size, md5)
        #     result.append(video)

        # cursor.close()
        # cnx.close()
        return result


    def delete(self, id):
        client = pyVideoClient.pyVideoClient()
        client.deleteVideo(id)
        # cnx = mysql.connector.connect(**self.__config)
        # cursor = cnx.cursor()
        
        # query = ("DELETE FROM files WHERE videoId = %s")
        # cursor.execute(query, (id,))

        # query = ("DELETE FROM videos WHERE id = %s")
        # cursor.execute(query, (id,))

        # cnx.commit()
        # cursor.close()
        # cnx.close()

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