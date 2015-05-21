#!/usr/bin/env python
# -*- coding: utf-8 -*-
from azure.storage import BlobService
from FileProcessor import FileProcessor
from VideoStoreOperator import *

def upload_chunck(buf, path, storagename, container, key):
	blob_service = BlobService(account_name=storagename, account_key=key)
	blob_service.put_block_blob_from_bytes(
		container,
		path,
		buf
    )

def  download_chunck(path, storagename, container, key):
	blob_service = BlobService(account_name=storagename, account_key=key)
	return blob_service.get_blob_to_bytes(container, path)

def upload_video(file_path):
	vs_operator = VideoStoreOperator()
	video_id = vs_operator.create(file_path)
	video_detils = vs_operator.get(video_id)

	processor = FileProcessor(file_path)
	count = len(video_detils.chuncks)
	for i in range(count):
		buf = processor.get_chunck(i)
		chk = video_detils.chuncks[i]
		upload_chunck(buf, chk.path, chk.storagename, chk.container, chk.key)

def list_videos():
	vs_operator = VideoStoreOperator()
	videos = vs_operator.list()
	count = len(videos)
	print u"id\t\t\t\tname"
	for i in range(count):
		print u"{0}\t\t\t\t{1}".format(videos[i].id, videos[i].name)

	return videos

def download_video(id, path=None):
	vs_operator = VideoStoreOperator()
	video_detils = vs_operator.get(id)

	if path == None:
		path = video_detils.video.name
	f = open(path, "wb")
	count = len(video_detils.chuncks)
	for i in range(count):
		chk = video_detils.chuncks[i]
		buf = download_chunck(chk.path, chk.storagename, chk.container, chk.key)
		f.write(buf)
	f.close()