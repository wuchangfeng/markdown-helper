#! /usr/bin/python
#-*- coding: utf-8 -*-
···
https://tinypng.com/developers/reference/python 压缩图片的 API URL
···

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
from qiniu import BucketManager
import sys,time
import os
import msvcrt
import datetime
import subprocess
import tinify


# you will get md_url in this file
result_file = "ss.txt"  

if os.path.exists(result_file):
    os.remove(result_file)
os.chdir(sys.path[0])

# you need get yours msg here
tinify.key = "xxxx"
access_key = "xxxx"
secret_key = "xxxx"
bucket_name = 'xxxx'
bucket_url = 'xxxx'
md_url_result = "md_url.txt"

img_suffix = ["jpg", "jpeg", "png", "bmp", "gif"]

def upload_img(bucket_name,file_name,file_path):
    # generate token
    token = q.upload_token(bucket_name, file_name, 3600)
    info = put_file(token, file_name, file_path)
    # delete local imgFile
    os.remove(file_path)
    return

def get_img_url(bucket_url,file_name):
    img_url = 'http://%s/%s' % (bucket_url,file_name)
    # generate md_url
    md_url = "![%s](%s)\n" % (file_name, img_url)
    return md_url


def save_to_txt(bucket_url,file_name):
    url_before_save = get_img_url(bucket_url,file_name)
    # save to clipBoard
    addToClipBoard(url_before_save)
    # save md_url to txt
    with open(md_url_result, "a") as f:
        f.write(url_before_save)
    return

# save to clipboard
def addToClipBoard(text):
	command = 'echo ' + text.strip() + '| clip'
	os.system(command)

if __name__ == '__main__':
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    imgs = sys.argv[1:]
    for img in imgs:
        source = tinify.from_file(img)
        up_filename = time.strftime("%Y/%m/%d/%X ", time.localtime())
        # os.remove(img)
        source.to_file(img)
        upload_img(bucket_name,up_filename,img)
        save_to_txt(bucket_url,up_filename)
