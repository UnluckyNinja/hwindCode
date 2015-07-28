#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import videomanager.pyVideoClient as pyVideoClient
import videomanager.videostoreoperator as videostoreoperator

class pyVideoClientTest(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test_storage_get(self):
        client = pyVideoClient.pyVideoClient()
        storages = client.getStorageInfo()
        for s in storages:
            print("id={0}, name={1}, container={2}, key={3}".format(s["id"], s["name"], s["container"], s["key"]))


    def test_create_video(self):
        client = pyVideoClient.pyVideoClient()
        video = videostoreoperator.Video('', 'api test', 1010, 'hello api')
        ret = client.createVideo(video)
        print(ret)

    def test_video(self):
        client = pyVideoClient.pyVideoClient()
        videos = client.getVideoList()
        if len(videos) == 0:
            return
        pdb.set_trace()
        video = videos[0]
        state = video['state']

        client.updateVideoState(video['id'], state+1)
        new_video = client.getVideo(video['id'])
        print("old state is {0}, and new state is {1}".format(state, new_video['video']['state']))