#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import os
import urllib.parse
import pdb
import videomanager.config as config

class pyVideoClient:
    _base_url = "https://hwind-linux.cloudapp.net/rest/"

    def _get(self, url):
        cert_path  = config.get_client_cert_path()
        return requests.get(url, verify=False, cert=cert_path)

    def _post(self, url, data):
        cert_path = config.get_client_cert_path()
        return requests.post(url, verify=False, cert=cert_path, data=data)

    def  _delete(self, url):
        cert_path = config.get_client_cert_path()
        return requests.delete(url, verify=False, cert=cert_path)


    def getStorageInfo(self):
        storage_url = urllib.parse.urljoin(self._base_url, "storage")
        ret = []
        try:
            result = self._get(storage_url)
            if result.status_code == 200:
                ret = result.json()
        except:
            pass
        finally:
            return ret

    def getVideoList(self):
        video_url = urllib.parse.urljoin(self._base_url, "video")
        ret = []
        try:
            result = self._get(video_url)
            if result.status_code == 200:
                ret = result.json()
        except:
            pass
        finally:
            return ret

    def createVideo(self, video):
        video_url = urllib.parse.urljoin(self._base_url, "video")
        data = {'name': video.name, "size": video.size, "md5": video.md5, "state": 0}
        ret = None
        try:
            result = self._post(video_url, data)
            if result.status_code == 201:
                ret = result.json()
        except :
            pass
        finally:
            return ret

    def getVideo(self, id):
        video_detail_url = urllib.parse.urljoin(urllib.parse.urljoin(self._base_url, "video/"), id)
        ret = []
        try:
            result = self._get(video_detail_url)
            if result.status_code == 200:
                ret = result.json()
        except :
            pass
        finally:
            return ret

    def deleteVideo(self, id):
        video_detail_url = urllib.parse.urljoin(urllib.parse.urljoin(self._base_url, "video/"), id)
        ret = False
        try:
            result = self._delete(video_detail_url)
            if result.status_code == 204:
                ret = True
        except:
            pass
        finally:
            return ret