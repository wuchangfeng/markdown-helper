#! /usr/bin/python
#-*- coding: utf-8 -*-

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
from qiniu import BucketManager
import sys
import os

'''
allen's script for uploading img to qiniu and get md_url
'''

 

if os.path.exists(result_file):
    os.remove(result_file)
os.chdir(sys.path[0])


# you need get yours msg here
access_key = "XXXX"
secret_key = "XXXX"
bucket_name = 'XXXX'
bucket_url = 'XXXX'
md_url_result = "md_url.txt"

# upload your img to qiniu
def upload_img(bucket_name,file_name,file_path):
    # generate token
    token = q.upload_token(bucket_name, file_name, 3600)
    info = put_file(token, file_name, file_path)
    return

# get md_url 
def get_img_url(bucket_url,file_name):

    img_url = 'http://%s/%s' % (bucket_url,file_name)
    # generate md_url
    md_url = "![%s](%s)\n" % (file_name, img_url)
    return md_url

# save to txt
def save_to_txt(bucket_url,file_name):
    # get url
    url_before_save = get_img_url(bucket_url,file_name)
    # save md_url to txt
    with open(md_url_result, "a") as f:
        f.write(url_before_save)
    return



if __name__ == '__main__':

    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)

    imgs = sys.argv[1:]
    # drop more than one img to .py file and
    # it will auto run and generate txt file
    for img in imgs:
        up_filename = os.path.split(img)[1]
        upload_img(bucket_name,up_filename,img)
        save_to_txt(bucket_url,up_filename)
