#récupere la video de la camera et l'affiche dans une fenetre
#pour quitter appuyer sur la touche q

import cv2
import numpy as np

#fonction pour détecter les coins


cap = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

i = 0
while(True):
    ret, frame = cap.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=15, minSize=(30,30))
    for (x, y, w, h) in eyes:
        cv2.circle(frame, (x+w//2, y+h//2), w//2, (255, 0,0), 1)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

