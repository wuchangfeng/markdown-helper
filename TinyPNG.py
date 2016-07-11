#! /usr/bin/python
#-*- coding: utf-8 -*-

import tinify,os
import sys
import os


'''
参数配置很简单:https://tinypng.com/developers/reference/python
1:注册获取 key 填入 xxxx 中
2:pip install --upgrade tinify
'''

# you need get yours msg here
tinify.key = "xxxx"

if __name__ == '__main__':
    
    # drop and handle
    imgs = sys.argv[1:]

    for img in imgs:
        source = tinify.from_file(img)
        # what size you nedd
	resized = source.resize(
 	   method="fit",
    	   width=200,
           height=300
	)
	# delete original img
        os.remove(img)
        # generate new img
	resized.to_file(img)
