#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 15:11:40 2017

@author: dad
"""
import os
os.chdir('/home/dad/AWS/Face-Detection')

import boto3
#import index_face function
from search_faces import search_face 

#connect to AWS
client = boto3.client('rekognition')

#set collection name
collection_name = 'authorized_faces'
match_threshold = 0.9

# search Dad
with open('/home/dad/AWS/rekog/Dad.jpg', 'rb') as new_image:
    image_bytes = new_image.read()

face_name = search_face(client, image_bytes, collection_name, match_threshold)
print face_name

# search Mom
with open('/home/dad/AWS/rekog/Mom.jpg', 'rb') as new_image:
    image_bytes = new_image.read()

face_name = search_face(client, image_bytes, collection_name, match_threshold)
print face_name




