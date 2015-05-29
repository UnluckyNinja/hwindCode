#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
from azure.storage import BlobService

import videomanager.fileprocessor as fileprocessor
import videomanager.videostoreoperator as videostoreoperator
import videomanager.config as config
import videomanager.encrypt as encrypt

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
	vs_operator = videostoreoperator.VideoStoreOperator()
	video_id = vs_operator.create(file_path)
	video_detils = vs_operator.get(video_id)

	processor = fileprocessor.FileProcessor(file_path)
	count = len(video_detils.chuncks)
	for i in range(count):
		buf = processor.get_chunck(i)
		chk = video_detils.chuncks[i]
		upload_chunck(buf, chk.path, chk.storagename, chk.container, chk.key)
		
def list_videos():
	vs_operator = videostoreoperator.VideoStoreOperator()
	videos = vs_operator.list()
	count = len(videos)
	print ("id\t\t\t\tname")
	for i in range(count):
		print ("{0}\t\t\t\t{1}".format(videos[i].id, videos[i].name))

	return videos

def download_video(id, path=None):
	vs_operator = videostoreoperator.VideoStoreOperator()
	video_detils = vs_operator.get(id)

	if path == None:
		decrypt_path = video_detils.video.name
		path = video_detils.video.name + ".tmp"
	else:
		decrypt_path = path
		path = path + ".tmp"

	f = open(path, "wb")
	count = len(video_detils.chuncks)
	for i in range(count):
		chk = video_detils.chuncks[i]
		buf = download_chunck(chk.path, chk.storagename, chk.container, chk.key)
		f.write(buf)
	f.close()

	if config.is_encrypt():
		with open(path, "rb") as in_f, open(decrypt_path, "wb") as out_f:
			encrypt.decrypt(in_f, out_f, config.config["pwd"])
	else:
		shutil.move(path, decrypt_path)

	processor = fileprocessor.FileProcessor(decrypt_path)
	if processor.md5 == video_detils.video.md5:
		print ("download finished. checksum matched")
	else:
		print ("download finished, but checksum doesn't match. Download failed.")

def delete_video(id):
	vs_operator = videostoreoperator.VideoStoreOperator()
	video_detils = vs_operator.get(id)
	vs_operator.delete(id)
	
	count = len(video_detils.chuncks)
	for i in range(count):
		chk = video_detils.chuncks[i]
		blob_service = BlobService(account_name=chk.storagename, account_key=chk.key)
		blob_service.delete_blob(chk.container, chk.path)

def upload_cmd(options):
	upload_video(options.src)

def download_cmd(options):
	download_video(options.id, options.dest)

def list_cmd(options):
	return list_videos()

def delete_cmd(options):
	delete_video(options.id)