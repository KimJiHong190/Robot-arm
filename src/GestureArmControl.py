import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector=HandDetector(maxHands=1, detectionCon=1)
mySerial= SerialObject("/dev/ttyACM0", 9600, 1)
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList,bbox=detector.findPosition(img)
    if lmList:
        fingers=detector.fingersUp()
        print(fingers)
    cv2.imshow("Image",img)
    cv2.waitKey(1)