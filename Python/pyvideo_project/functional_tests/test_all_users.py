# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from django.core.urlresolvers import reverse
#from django.contrib.staticfiles.testing import LiveServerTestCase  
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

 
 
#class HomeNewVisitorTest(LiveServerTestCase):
class HomeNewVisitorTest(StaticLiveServerTestCase):
 
    def setUp(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe')
        self.browser = webdriver.Chrome(path)
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
 
    def test_home_title(self):
        print(self.get_full_url("home"))
        self.browser.get(self.get_full_url("home"))
        self.assertIn("PyVideo", self.browser.title)
 
    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"), 
                         "rgba(200, 50, 255, 1)")
