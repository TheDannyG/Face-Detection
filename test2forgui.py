# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:45:00 2017

@author: Daniel
"""

import Tkinter as tk
import cv2
from PIL import Image, ImageTk
import time
import boto3

from search_faces import search_face

#Connect to AWS
client = boto3.client('rekognition')

#Set collection name for the search_face
collection_name = 'authorized_faces'
#Set the the threshhold to be considered a match
match_threshold = 0.85

width, height = 60, 2
cap = cv2.VideoCapture(0)

root = tk.Tk()
lmain = tk.Label(root)
lmain.pack()

startTime = 0


def show_frame():
    global frame
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if (startTime >= time.time()-5) & (startTime <= time.time()):
            #Display the who is currently detected and authrization level
            cv2.putText(img,authorized,(10,30), font, 1,(0,255,0),2)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def callback():
        print "Authorize"
        #Check for faces using search_face function and out who it finds
        face_name = search_face(client, cv2.imencode('.jpg', frame)[1].tostring(), collection_name, match_threshold)
                    
        s = "";
                             
        #Checks if they are authorized
        if face_name == "UNKNOWN":
            seq = (face_name, ": ", "Not Authorized") 
            authorized = s.join(seq) 
            print authorized
            startTime = time.time()
        else:
            seq = (face_name, ": ", "Authorized")   
            authorized = s.join(seq)
            print authorized
            #check time
            startTime = time.time()
    
label = tk.Label(root, text = "Please, press the button to authorize.")
button = tk.Button(root, text="Authorize", command=callback, height=height, width=width)
label.pack(side=tk.LEFT)
button.pack(side=tk.RIGHT)


show_frame()
root.mainloop()