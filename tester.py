from imutils.video import FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import matplotlib.pyplot as plt
import imutils
import time
import cv2

count=0
for i in range(0,1253,3):
    x=cv2.imread("datasets\\f3."+str(i)+".jpg")
    cv2.imshow("frame",x)

    if cv2.waitKey(1)==27:
        break
    count+=1
    x=cv2.resize(x,(500,500))
    cv2.imwrite("output\\"+str(count)+".JPEG",x)
