# Face-Detection
Amazon Rekognition with Python

This program will take a picture of user when run, upload to Amazon Web Services' to be compared to the face of the registered person(s). It will identify people in the picture that are registered in a database.

Current progress:
- Takes picture using opencv - Takes about 2.58 seconds
- Uploads the picture along side with hte pctuer of the registered person to Amazon Web Services' Rekognition program to be analyzed against each other
- Returns the similarity in percentage and decides whether they are similar or not

Planned Progress:
- Increased speed by uploading only one picture, the target, to the cloud
- Increase speed of taking a picture
- Add database of faces to scan for in picture
- Add GUI

Libraries being used:
- opencv3
- boto3
- botocore
