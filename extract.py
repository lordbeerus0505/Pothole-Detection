# import the necessary packages
from imutils.video import FileVideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

def skip():
    for i in range(5):
        frame=fvs.read()
# construct the argument parse and parse the arguments

# car_cascade = cv2.CascadeClassifier('cars.xml')
fvs = FileVideoStream("Flight03.mp4").start()
print(fvs)
time.sleep(1.0)
t=0
count=0
x1=1000
y1=1000
t1=0
# start the FPS timer
fps = FPS().start()
count=0
t=0
# loop over frames from the video file stream
while fvs.more():
	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale (while still retaining 3
	# channels)
    frame = fvs.read()
    f=frame
    # frame = imutils.resize(frame, width=1800)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = np.dstack([frame, frame, frame])
    # cv2.rectangle(frame,(200,250),(600,500),(0,255,0),4)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("datasets/f3."+str(count)+".jpg",f)
    count+=1
    skip()
    # cars = car_cascade.detectMultiScale(frame, 1.1, 1)
    # for (x,y,w,h) in cars:
    #     j=time.time()-t
    #     if w>150 and h>150 and w<350 and h<350 and x>150 and x<450 and y>250 and y<350:
    #         #to prevent miscount this is used, not really necessary
    #         if (y<y1 and time.time()-t>0.1) or j>0.5:
    #             #as f is not converted to BW retaining the color before sending to YOLO
    #             cv2.rectangle(frame,(x,y),(x+w,y+h),(120,0,255),5)

    #             cv2.imwrite("Frames/frame"+str(count)+".jpg",f[250:800,200:800])
    #             #skip frames as drawn
    #             count+=1
    #             print(count)
    #             t=time.time()
    #             y1=y
    #             skip()
    #             #exit the check for this frame
    #             break
    

	# display the size of the queue on the frame
	# cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),
	# 	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	

	# show the frame and update the FPS counter
    cv2.imshow("Frame", f)
    if cv2.waitKey(1)==27:
        break
    fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
fvs.stop()


