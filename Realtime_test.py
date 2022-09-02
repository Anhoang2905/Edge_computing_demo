#Use this to test the 
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox
import concurrent.futures
url='http://192.168.1.47:8080/shot.jpg'
frame=None        
def run2():
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    while True:
        frame_resp=urllib.request.urlopen(url)
        framenp=np.array(bytearray(frame_resp.read()),dtype=np.uint8)
        frame = cv2.imdecode(framenp,-1)
        bbox, label, conf = cv.detect_common_objects(im)
        im = draw_bbox(im, bbox, label, conf)
        cv2.imshow('detection',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break   
    cv2.destroyAllWindows()
if __name__ == '__main__':
    print("started")
    run2()