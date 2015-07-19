#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import time
import collections
import threading
import sys
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import videomanager.videomanager as videomanager
import pdb

class Monitor(object):
    def __init__(self):
        self.__base_dir = os.path.dirname(os.path.abspath(__file__))
        self.__upload_dir = os.path.join(self.__base_dir, ".tmp_upload")
        self.__download_dir = os.path.join(self.__base_dir, ".tmp_download")
        self.__all_processed = {}
        self.QueryIntervalSecond = 5

        if not os.path.exists(self.__upload_dir):
            os.makedirs(self.__upload_dir)
        if not os.path.exists(self.__download_dir):
            os.makedirs(self.__download_dir)

        downloaded_files = self.__list_files(self.__download_dir)
        uploaded_files = self.__list_files(self.__upload_dir)
        for f in downloaded_files:
            basename = os.path.basename(f)
            self.__all_processed[basename] = 1
        for f in uploaded_files:
            basename = os.path.basename(f)
            self.__all_processed[basename] = 1

        self.__to_download_queue = collections.deque([])
        self.__to_upload_queue = collections.deque(downloaded_files)
        self.__complete_queue = collections.deque(uploaded_files)

        self.__stop = False
        self.__running_state = {}

    def __list_files(self, path):
        if not os.path.isdir(path):
            return []

        result = []
        for name in os.listdir(path):
            f = os.path.join(path, name)
            if os.path.isfile(f):
                result.append(f)
        return result

    def run(self):
        self.__list_worker = threading.Thread(target=self.list_worker)
        self.__download_worker = threading.Thread(target=self.download_worker)
        self.__upload_worker = threading.Thread(target=self.upload_worker)

        self.__list_worker.start()
        self.__download_worker.start()
        self.__upload_worker.start()

        self.respond_to_cmd()

    def respond_to_cmd(self):
        while not self.__stop:
            cmd = sys.stdin.readline()
            cmd = cmd.strip()
            print(cmd)
            if cmd == "quit":
                self.__stop = True
                self.__list_worker.join()
                self.__download_worker.join()
                self.__upload_worker.join()
            elif cmd == "state":
                self.__show_state()

    def __show_state(self):
        print("download queue:")
        print(self.__to_download_queue)
        print("upload queue:")
        print(self.__to_upload_queue)
        print("workers:")
        print(self.__running_state)

    def __set_state(self, key, value):
        self.__running_state[key] = value

    def list_worker(self):
        while not self.__stop:
            files = self.__by_list()
            for f in files:
                if f in self.__all_processed:
                    continue
                else:
                    self.__all_processed[f] = 1
                    self.__to_download_queue.append(f)

            time.sleep(self.QueryIntervalSecond)

    def download_worker(self):
        while not self.__stop:
            #pdb.set_trace()
            if len(self.__to_download_queue) == 0:
                time.sleep(self.QueryIntervalSecond)
                continue
            f = self.__to_download_queue.popleft()
            new_name = os.path.join(self.__download_dir, f)
            self.__by_download(f, new_name)
            self.__to_upload_queue.append(new_name)

    def upload_worker(self):
        while not self.__stop:
            #pdb.set_trace()
            if len(self.__to_upload_queue) == 0:
                time.sleep(self.QueryIntervalSecond)
                continue
            f = self.__to_upload_queue.popleft()
            new_name = self.__move_to_upload_dir(f)
            self.__upload_file(new_name)
            self.__complete_queue.append(new_name)

    def __move_to_upload_dir(self, path):
        file_name = os.path.basename(path)
        new_path = os.path.join(self.__upload_dir, file_name)
        shutil.move(path, new_path)
        return new_path

    def __upload_file(self, path):
        self.__set_state("uploading", path)
        videomanager.upload_video(path)
        print("file {0} is uploaded".format(path))
        self.__set_state("uploading", "")

    def __by_execute(self, cmd):
        byexecutor = os.path.join(self.__base_dir, "byexecutor.py")
        if os.name == 'posix':
            cmdline = ["/usr/local/bin/python", byexecutor]
        else:
            cmdline = ["C:\\Python27\\Python.exe", byexecutor]
        with subprocess.Popen(cmdline, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True) as proc:
            out, err = proc.communicate(cmd)
            return out

    def __parse_file_name(self, output):
        if output[0] == 'F':
            return output[2:]
        fields = output.split(' ')
        if fields[0] == 'F':
            return fields[1]
        return None

    def __by_list(self):
        self.__set_state("listing", True)
        cmd = "list"
        results = self.__by_execute(cmd)
        #result_lines = results.split('\n')
        result_lines = results.splitlines()
        find_flag = False
        files = []

        #pdb.set_trace()
        for i in range(0, len(result_lines)):
            if find_flag == True:
                item = self.__parse_file_name(result_lines[i])
                if item != None:
                    files.append(item)

            elif result_lines[i] == "/apps/bypy ($t $f):":
                find_flag = True

        self.__set_state("listing", False)
        return files

    def __by_download(self, src, dest):
        self.__set_state("downloading", src)
        cmd = "download '{0}' '{1}'".format(src, dest)
        results = self.__by_execute(cmd)
        self.__set_state("downloading", "")

if __name__ == '__main__':
    monitor = Monitor()
    monitor.run()