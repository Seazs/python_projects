import sys
import math
import cv2 as cv
import numpy as np

def line_detection(src):
    blur = cv.GaussianBlur(src,(3,3),0)

    # #prewitt
    # kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    # kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    # img_prewittx = cv.filter2D(blur, -1, kernelx)
    # img_prewitty = cv.filter2D(blur, -1, kernely)
    # img_prewitt = img_prewittx + img_prewitty
    # dst = np.where(img_prewitt >= 1, 1, 0)
    # print(dst)

    dst = cv.Canny(blur, 50, 170, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)    
    
    linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(src, (l[0], l[1]), (l[2], l[3]), (0,0,255), 2, cv.LINE_AA)
    
    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)

    return src, linesP

def corner_detection(src):
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray,25,0.01,10)
    corners = np.int0(corners)
    corners_list = []
    for i in corners:
        x,y = i.ravel()
        corners_list.append((x,y))
        cv.circle(src,(x,y),3,255,-1)
    return src, corners_list

def paralel_line_detection(lines):
    # check if there are parallel lines that are close to each other
    parralel_pairs = []
    if lines is None:
        return False
    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)):
            l1 = lines[i][0]
            l2 = lines[j][0]
            angle1 = np.arctan2(l1[3] - l1[1], l1[2] - l1[0])
            angle2 = np.arctan2(l2[3] - l2[1], l2[2] - l2[0])
            angle_diff = abs(angle1 - angle2)

            if angle_diff < 0.1 :
                parralel_pairs.append((l1, l2))
    return parralel_pairs

def detect_corners_on_lines(corners_list, lines):
    pass

def main(argv):
    cap = cv.VideoCapture(0)

    while  True:

        ret, src = cap.read() 

        src, corners_list = corner_detection(src)
        src, lines = line_detection(src)

        parralel_pairs = paralel_line_detection(lines)
        lines_with_corners = detect_corners_on_lines(corners_list, lines)
        
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])