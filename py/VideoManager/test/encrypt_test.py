#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import videomanager.fileprocessor as fileprocessor
import videomanager.config as config
import videomanager.encrypt as encrypt

class EncryptTest(unittest.TestCase):
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
	
	def test_encrypt_decrypt(self):
		path = "testdata//test.mkv"
		with open(path, "rb") as in_f, open(path+".tmp", "wb") as out_f:
			encrypt.encrypt(in_f, out_f, "Password01!")

		with open(path+".tmp", "rb") as in_f, open(path+".tmp2", "wb") as out_f:
			encrypt.decrypt(in_f, out_f, "Password01!")

		with open(path+".tmp", "rb") as in_f, open(path+".tmp3", "wb") as out_f:
			encrypt.decrypt(in_f, out_f, "Password02!")

		p1 = fileprocessor.FileProcessor(path)
		p2 = fileprocessor.FileProcessor(path+".tmp2")
		p3 = fileprocessor.FileProcessor(path+".tmp3")
		
		self.assertEqual(p1.md5, p2.md5)
		self.assertNotEqual(p1.md5, p3.md5)