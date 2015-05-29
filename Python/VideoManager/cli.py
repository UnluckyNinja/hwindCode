#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
import videomanager.videomanager as videomanager

parser = argparse.ArgumentParser(prog='VideoManagerCommandLine')
subparsers = parser.add_subparsers(help='sub-command help')

parser_list = subparsers.add_parser('list', help='list videos')
parser_list.set_defaults(func=videomanager.list_cmd)

parser_download = subparsers.add_parser('download', help='download a video')
parser_download.add_argument('id', help='video id')
parser_download.add_argument('-d', '--dest', help='download destination')
parser_download.set_defaults(func=videomanager.download_cmd)

parser_upload = subparsers.add_parser('upload', help='upload a video')
parser_upload.add_argument('src', help='video file path')
parser_upload.set_defaults(func=videomanager.upload_cmd)

parser_delete = subparsers.add_parser('delete', help='delete a video')
parser_delete.add_argument('id', help='video id')
parser_delete.set_defaults(func=videomanager.delete_cmd)


args = parser.parse_args(sys.argv[1:])
args.func(args)