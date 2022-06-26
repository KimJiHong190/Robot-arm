#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64MultiArray, String
from cvzone.HandTrackingModule import HandDetector
import cv2

def main():
    
    cap = cv2.VideoCapture(-1)
    detector=HandDetector(maxHands=1, detectionCon=1)
    while True:
        try:
            success,img = cap.read()
            img = detector.findHands(img)
            lmList,bbox=detector.findPosition(img)
            if lmList:
                fingers=detector.fingersUp()
                print(fingers)
                
            cv2.imshow("Image",img)
            cv2.waitKey(1)
            return fingers
            
            
        except:
            continue
        
    
if __name__ == "__main__":
    main()