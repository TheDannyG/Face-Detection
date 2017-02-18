#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:24:12 2017

@author: dad
"""

#defines index_face function
#function returns number of faces found/indexed
#input param: 
#   client: rekognition client from boto3.client('rekognition')
#   image_bytes: image bytes
#   collection_name: Name of collection to add faces to
#   face_name: Name of the face (strored in ExternalImageId)
#use:
#from index_faces import index_face 


def index_face(client, image_bytes, collection_name, face_name):

    response_index = client.index_faces(
        CollectionId = collection_name,
        Image = {'Bytes': image_bytes},
        ExternalImageId = face_name
    )
    return len(response_index['FaceRecords'])