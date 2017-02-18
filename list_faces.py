#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:43:25 2017

@author: dad
"""

#list faces currently in collection
import boto3

#connect to AWS
client = boto3.client('rekognition')

#set collection name
collection_name = 'authorized_faces'

#check if collection exists and fetch all faces from collection
response_list = client.list_collections()
if collection_name in response_list['CollectionIds']: 
    response_faces = client.list_faces(CollectionId=collection_name)
    print collection_name, 'contains ', len(response_faces['Faces']), ' faces'
    for l in response_faces['Faces']:
        print l['ExternalImageId'], ', confidence: ', l['Confidence']
else: 
    print 'Collection ', collection_name, ' does not exists.'
    



