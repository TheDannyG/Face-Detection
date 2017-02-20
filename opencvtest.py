# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:07:03 2017

@author: Daniel
"""
import cv2
import numpy as np

switch = '0 : OFF \n1 : ON'

def get_image(x):
    '''retval, im = camera.read()
    cv2.imwrite(test.jpg, im)
    return im'''
    print x
    
def show_webcam(mirror=False):
    #print __name__
    cv2.namedWindow('my webcam')
    cam = cv2.VideoCapture(0)
    
    while True:
        cv2.createTrackbar(switch, 'my webcam',0,1,get_image)
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
        s = cv2.getTrackbarPos(switch,'my webcam')
        if s == 1:
            print "debug"
            cv2.imwrite("opencv.jpg", img)
        

    cv2.destroyAllWindows()

def main():
    #switch = '0 : OFF \n1 : ON'
    
    show_webcam(mirror=True)
    

if __name__ == '__main__':
    main()