'''
Created on Aug 27, 2014

@author: hwind
'''

import json
import urllib.request
import urllib.parse
import os
import ctypes
import pythoncom
from win32com.shell import shell, shellcon
from datetime import date, datetime
from pathlib import Path
from lib2to3.fixer_util import String

def GetCharsetFromResponse (response):
    contentType = response.getheader("content-type")
    for item in contentType.split(' '):
        if item.lower().startswith("charset"):
            return item[item.index("="):]


def LogWarning (msg):
    print("%s    %s" % (datetime.today().isoformat(), msg))

def DownloadImage(url, dest):
    if os.path.exists(dest):
        print("path already exists")
        return
    fp = open(dest, "wb")
    response = urllib.request.urlopen(url)
    fp.write(response.read())
    fp.close()
    response.close()
    
"""
This version doesn't work on Windows8
def UpdateDesktopBackground(dest):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, dest, 3)
"""
def UpdateDesktopBackground(dest):
    iad = pythoncom.CoCreateInstance(shell.CLSID_ActiveDesktop, None,
                                     pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IActiveDesktop)
    iad.SetWallpaper(dest, 0)
    iad.ApplyChanges(shellcon.AD_APPLY_ALL)
    

bingImageInfoURL = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
baseFolder = "D:\documents\OneDrive\图片\wallpaper"
response = urllib.request.urlopen(bingImageInfoURL)
charset = GetCharsetFromResponse(response)
content = response.read().decode(charset)
response.close()

imageInfo = json.loads(content)
for img in imageInfo["images"]:
    if img["startdate"] != date.today().strftime("%Y%m%d"):
        LogWarning("Didn't find today's image info")
    elif img["wp"] == False:
        LogWarning("Today's image is not for desktop")
    else:
        imgHighResolution = img["urlbase"]+"_1920x1200.jpg"
        imageUrl = urllib.parse.urljoin("http://www.bing.com", imgHighResolution)
        path, imgName = os.path.split(imgHighResolution)
        filename = date.today().strftime("%Y%m%d")+"_"+imgName            
        dest = os.path.join(baseFolder, filename)
        DownloadImage(imageUrl, dest)
        UpdateDesktopBackground(dest)
        break
