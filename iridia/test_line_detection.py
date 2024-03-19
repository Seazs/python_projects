import sys
import math
import cv2 as cv
import numpy as np
def main(argv):
    cap = cv.VideoCapture(0)

    while  True:

        ret, src = cap.read() 
        
        blur = cv.GaussianBlur(src,(3,3),0)

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

        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
    return 0
    
if __name__ == "__main__":
    main(sys.argv[1:])
        
