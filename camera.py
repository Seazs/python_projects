#récupere la video de la camera et l'affiche dans une fenetre
#pour quitter appuyer sur la touche q

import cv2
import numpy as np

#fonction pour détecter les coins
def detecteCoin(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,1,0.04)
    dst = cv2.dilate(dst,None)
    img[dst>0.05*dst.max()]=[0,0,255]
    return img

def detecteCoin2(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,255,-1)
    return img

def detecteLigne(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(11,11),0)
    cv2.imshow('blur',blur)
    edges = cv2.Canny(blur,10,110,apertureSize = 3)
    cv2.imshow('edges',edges)
    minLineLength = 100
    maxLineGap = 20
    lines = cv2.HoughLinesP(edges,1,np.pi/180,5,minLineLength,maxLineGap)
    return lines

def detecteLigne2(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(9,9),0)

    edges = cv2.Canny(blur,10,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180,200)
    return lines

def printLine(img, lines):
    if lines is not None:
        for i in range(len(lines)):
            for x1,y1,x2,y2 in lines[i]:
                cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    return img

def detected_door(lines):
    if lines is not None:
        for line in lines:
            for x1,y1,x2,y2 in line:
                if abs(x1 - x2) < 50:
                    return True
    return False

cap = cv2.VideoCapture(0)
i = 0
lignes = []
while(True):
    ret, frame = cap.read()
    # if i == 0:

    lignes = detecteLigne(frame)
    # if detected_door(newlines):
    #     print("Door detected")
    if lignes is not None:
        print(len(lignes))
        printLine(frame, lignes)
    # detecteCoin2(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
    # i += 1
    # if i == 2:
    #     i = 0
cap.release()
cv2.destroyAllWindows()

