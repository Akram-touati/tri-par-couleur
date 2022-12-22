import cv2
import numpy as np
import imutils
import argparse
import RPi.GPIO as GPIO
import time
import csv


ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
                help="max buffer size")
args = vars(ap.parse_args())
"""if not args.get("video", False):
    camera = cv2.VideoCapture(0)



# otherwise, grab a reference to the video file
else:
    camera = cv2.VideoCapture(args["video"])
"""
camera = cv2.VideoCapture(0)
while True:

    ret,frame=camera.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_brown=np.array([0,0,0])
    upper_brown=np.array([50,100,100])
    lower_green = np.array([40, 70, 80])
    upper_green = np.array([70, 255, 255])
    lower_bleu = np.array([97,100, 117])
    upper_bleu = np.array([117, 255, 255])
    lower_red = np.array([0, 50, 120])
    upper_red = np.array([10, 255, 255])
    mask1= cv2.inRange(hsv,lower_brown,upper_brown)
    mask2 = cv2.inRange(hsv,lower_green,upper_green)
    mask3 = cv2.inRange(hsv,lower_red,upper_red)
    mask4 = cv2.inRange(hsv, lower_bleu, upper_bleu)
    cnts1=cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts1=imutils.grab_contours(cnts1)

    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)
    cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)
    cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts4 = imutils.grab_contours(cnts4)
    
#     
    for c in cnts1:
        areal = cv2.contourArea(c)
        if areal > 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            m = cv2.moments(c)
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "brown", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)
            print("maron")
            with open('myCSVfile.csv', mode='w') as x:
                x = csv.writer(x, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                x.writerow('m')
           
#     for c in cnts2:
#         area2 = cv2.contourArea(c)
#        
#         if area2 > 5000:
#             cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
#             m = cv2.moments(c)
#             cx = int(m["m10"] / m["m00"])
#             cy = int(m["m01"] / m["m00"])
#             cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
#             cv2.putText(frame, "vert", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)
#             print("vert") 
#             with open('myCSVfile.csv', mode='w') as x:
#                 x = csv.writer(x, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                 x.writerow('v')
    

        
    for c in cnts3:
        area3 = cv2.contourArea(c)
        if area3 > 5000:
            #print("i")
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            m = cv2.moments(c)
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "rouge", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)
            print("rouge")
            with open('myCSVfile.csv', mode='w') as x:
                x = csv.writer(x, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                x.writerow('r')

           

    for c in cnts4:
        area4 = cv2.contourArea(c)
        if area4 > 5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            m = cv2.moments(c)
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "bleu", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)
            print("bleu")
            with open('myCSVfile.csv', mode='w') as x:
                x = csv.writer(x, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                x.writerow('b')


        
    cv2.imshow("Hello World",frame)
    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
    

print("ekhrej manes7a9ekch hna")
f = open('myCSVfile.csv', "w+")
f.close()
camera.release()
cv2.destroyAllWindows()


