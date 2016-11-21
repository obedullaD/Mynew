import cv2
import numpy as np

img = cv2.imread('sudo.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 200*(-b))
    y1 = int(y0 + 200*(a))
    x2 = int(x0 - 200*(-b))
    y2 = int(y0 - 200*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('sudo_out.png',img)

