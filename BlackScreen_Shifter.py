import cv2
import numpy as np
import time

capture = cv2.VideoCapture(0)
video_writer = cv2.VideoWriter_fourcc(*"XVID")
output_file = cv2.VideoWriter('Output.avi',video_writer,24,(640,450))
time.sleep(2)

backG = 0
for i in range(60):
    rt,backG = capture.read()
backG = np.flip(backG,axis=1)
backG = cv2.resize(backG,640,480)

while(capture.isOpened()):
    tf,image = capture.read()
    if not tf :
        break
    image = np.flip(image,axis=1)
    image = cv2.resize(image,640,480)
    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    mask = cv2.inRange(backG,u_black,l_black)
    res = cv2.bitwise_and(backG,backG,mask = mask)
    f = backG - res
    f = np.where(f == 0,image,f)

    output = cv2.addWeighted(res,1,0)
    output_file.write(output)
    cv2.imshow('Background Change',output)