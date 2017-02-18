#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:05:30 2017

@author: dad
"""
import boto3

#connect to AWS
client = boto3.client('rekognition')

#set collection name
collection_name = 'authorized_faces'

#check if collection already exists
response_list = client.list_collections()
if collection_name not in response_list['CollectionIds']: 
    #create collection
    response_coll = client.create_collection(
        CollectionId = collection_name
    )
    print response_coll
else: 
    print 'Collection ', collection_name, ' already exists.'
    #get and print list of faces
    response_faces = client.list_faces(CollectionId=collection_name)
    print collection_name, 'contains ', len(response_faces['Faces']), ' faces'
    print response_faces['Faces']




