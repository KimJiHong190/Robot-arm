import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
cap.set(3, 1280) # set the resolution
cap.set(4, 720)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1) # turn the autofocus off
detector=HandDetector(maxHands=1, detectionCon=1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)