#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import azure
from azure.storage import BlobService
import azure.http
import os.path
import sys
import os
import pdb

storage_name = ""
storage_key = ""

def list_files_from_path(container, path):
    blob_service = BlobService(account_name=storage_name, account_key=storage_key)
    next_marker = None
    results = []
    while True:
        blobs = blob_service.list_blobs(container, prefix=path, maxresults=2000, marker=next_marker)
        for blob in blobs:
            results.append(blob.name)
        next_marker = blobs.next_marker
        if not next_marker:
            break
    return results

def download_file(container, path, dest):
    blob_service = BlobService(account_name=storage_name, account_key=storage_key)
    loop = 0
    while True:
        try:
            blob_service.get_blob_to_path(container, path, dest)
            break
        except azure.http.HTTPError as e:
            loop = loop + 1
            if loop >= 3:
                return


if __name__ == '__main__':
    storage_name = input(">>storage_name:")
    storage_key = input(">>storage_key:")
    container = input(">>container:")
    path = input(">>path")
    #container="azurefilesystem2"
    #path="Ver0v1/2015-03-26"
    print(storage_name)
    print(storage_key)
    print(container)
    print(path)

    if not os.path.exists(container):
        os.makedirs(container)
    files = list_files_from_path(container, path)
    print("total files count is {0}".format(len(files)))

    for f in files:
        f_name = os.path.basename(f)
        dest = os.path.join(container, f_name)
        print("download from {0}:{1} to {2}".format(container, f, dest))
        download_file(container, f, dest)


