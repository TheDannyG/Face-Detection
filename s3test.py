# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:11:23 2017

@author: Daniel
"""
import boto3
import botocore

client = boto3.resource(
        's3',
        region_name = 'us-east-1', 
        aws_access_key_id = 'AKIAJSBBWLF7LNQYLUOQ',
        aws_secret_access_key = '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',
)

bucket = s3.Bucket('Rekognition')
