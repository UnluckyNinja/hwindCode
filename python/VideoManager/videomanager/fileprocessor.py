#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import hashlib
import videomanager.config as config
import videomanager.encrypt as encrypt

class FileProcessor:
    """docstring for FileProcessor"""

    name = None
    size = 0
    __file_path = None

    __CHUNCK_SIZE = 0

    def __init__(self, file_path):
        self.__file_path = file_path
        self.name = os.path.basename(file_path)
        self.size = os.path.getsize(file_path)
        FileProcessor.__CHUNCK_SIZE = config.config["ChunckSizeMB"] * 1024 * 1024
        self.__md5 = None
        self.__chuncks = None

    def __del__(self):
        if config.is_encrypt() and os.path.exists(self.__file_path + ".tmp"):
            os.remove(self.__file_path + ".tmp")

    @property
    def chuncks(self):
        if self.__chuncks == None:
            cur_size = 0
            if config.is_encrypt():
                tmp_path = self.__file_path + ".tmp"
                with open(self.__file_path, "rb") as in_f, open(tmp_path, "wb") as out_f:
                    encrypt.encrypt(in_f, out_f, config.config["pwd"])
                cur_size = os.path.getsize(tmp_path)
            else:
                cur_size = self.size

            if cur_size % FileProcessor.__CHUNCK_SIZE == 0:
                self.__chuncks = cur_size // FileProcessor.__CHUNCK_SIZE
            else:
                self.__chuncks = cur_size // FileProcessor.__CHUNCK_SIZE + 1
        
        return self.__chuncks

    @property
    def md5(self):
        if self.__md5 == None:
            md5 = hashlib.md5()
            f = open(self.__file_path, "rb")
            while True:
                data = f.read(2**20)
                if not data:
                    break
                md5.update(data)
            f.close()
            self.__md5 = md5.hexdigest()
        return self.__md5

    def get_chunck(self, index):
        #use self.chuncks instead of self.__chuncks to forth encryption happened
        if index < 0 or index >= self.chuncks:
            return None

        cur_path = self.__file_path
        if config.is_encrypt():
            cur_path = self.__file_path + ".tmp"

        f = open(cur_path, "rb")
        f.seek(index * FileProcessor.__CHUNCK_SIZE)

        if index == self.chuncks - 1:
            buf = f.read()
        else:
            buf = f.read(FileProcessor.__CHUNCK_SIZE)

        f.close()
        return buf

