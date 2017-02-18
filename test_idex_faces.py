#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:47:44 2017

@author: dad
"""

#code to test index_face function (from index_faces.py)
import os
os.chdir('/home/dad/AWS/Face-Detection')

import boto3
#import index_face function
from index_faces import index_face 

#set collection name
collection_name = 'authorized_faces'

#connect to AWS
client = boto3.client('rekognition')

# Add Dad
with open('/home/dad/AWS/rekog/Dad.jpg', 'rb') as new_image:
    image_bytes = new_image.read()
face_name = 'Dad'
face_num = index_face(client, image_bytes, collection_name, face_name)

#Add Daniel    
with open('/home/dad/AWS/rekog/Daniel.jpg', 'rb') as new_image:
    image_bytes = new_image.read()
face_name = 'Daniel'
face_num = index_face(client, image_bytes, collection_name, face_name)

#Mom    
with open('/home/dad/AWS/rekog/Mom.jpg', 'rb') as new_image:
    image_bytes = new_image.read()
face_name = 'Mom'
face_num = index_face(client, image_bytes, collection_name, face_name)
    
   
    
    
#delete collection
#response = client.delete_collection(
#    CollectionId=collection_name
#)