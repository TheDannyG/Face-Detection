#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 14:54:06 2017

@author: dad
"""

#defines search_face() function
#returns face name
#input param: 
#   client: rekognition client from boto3.client('rekognition')
#   image_bytes: image bytes
#   collection_name: Name of collection to add faces to
#   match_threshhold: Match threshold
#use:
#from search_faces import search_face 

def search_face(client, image_bytes, collection_name, match_threshold):
    #call AWS search_faces_by_image API
    response_search = client.search_faces_by_image(
        CollectionId = collection_name,
        Image={'Bytes': image_bytes},
        FaceMatchThreshold = match_threshold
    )
    #print debug messages
    for l in response_search['FaceMatches']:
        print l['Face']['ExternalImageId'], ', similarity: ', l['Similarity']
    
    #check if any face found and return face name or UNKNOWN if not found
    if len(response_search['FaceMatches']) > 0:
        face_name = response_search['FaceMatches'][0]['Face']['ExternalImageId']
    else:
        face_name = 'UNKNOWN'
        
    return face_name