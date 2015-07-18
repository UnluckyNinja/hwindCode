#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import shlex
import time
import pdb
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import bypy.bypy as bypy

class ByExecutor(object):
    """docstring for ByExecutor"""
    def __init__(self):
        self.__by = bypy.ByPy(bypy.DefaultSliceSize, bypy.DefaultDlChunkSize)

    def run(self):
        cmd = sys.stdin.readline().strip()
        #pdb.set_trace()
        if cmd.lower() == "list":
            #now = time.strftime("%Y-%m-%d--%H-%M-%S")
            #print(now)
            self.__by.list(fmt='$t $f')
        elif cmd.lower().startswith("download"):
            args = shlex.split(cmd)
            if len(args) == 3:
                src = args[1]
                dest = args[2]
                #with open(dest, 'w') as f:
                #    f.write(src)
                self.__by.downfile(src, dest)

if __name__ == '__main__':
    executor = ByExecutor()
    executor.run()
