import numpy as np
import cv2
import sys

# Update path to the Haar cascades file if necessary, e.g. if OpenCV version is different
faceCascadeFile = '/usr/local/opt/opencv/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(faceCascadeFile)
if faceCascade.empty(): raise Exception('faceCascade is empty. Double-check the path.')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    # Press 'Q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
