import cv2 
import math
import numpy as np
import cv2.aruco as aruco

(a1,b1)=(0,0)
(a2,b2)=(0,0)
(a3,b3)=(0,0)
(a4,b4)=(0,0)

img1 = cv2.imread("D:\RONY\IIT Dhanbad\Atulya\My Project\CVtask.jpg")

scale_percent = 60 # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)

img2 = cv2.imread("D:\happy python notes\RoboIsm\opencv\Ha_cropped.jpg")
img3 = cv2.imread("D:\happy python notes\RoboIsm\opencv\HaHa_cropped.jpg")
img4 = cv2.imread("D:\happy python notes\RoboIsm\opencv\LMAO_cropped.jpg")
img5= cv2.imread("D:\happy python notes\RoboIsm\opencv\XD_cropped.jpg")



def my_function(img,contours):
    
    for contour in contours:
       #cv2.drawContours(img, contours, -1, (0, 255, 0),1)
       approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
       #cv2.drawContours(img,[approx],0,(255,0,0),5)
       x=approx.ravel()[0]
       y=approx.ravel()[1]
       n=approx.ravel()
       
       i=0

        
       if (len(approx)==4):
           x,y,w,h  = cv2.boundingRect(approx)
           aspectRatio  = float(w)/h

           #print(aspectRatio)

           if (aspectRatio >=0.95) and (aspectRatio<=1.05) :
               (a1,b1)=(n[0],n[1])
               (a2,b2)=(n[2],n[3])
               (a3,b3)=(n[4],n[5])
               (a4,b4)=(n[6],n[7])
               
               M = cv2.moments(contour)
                   
               cx = int(M['m10']/M['m00'])
               cy = int(M['m01']/M['m00'])
    
               color=img[cy,cx]
               
               
               if np.any(img[cy,cx]==[79, 209, 146]):
                   
                   
                 h,w,c=img4.shape                   
                 pts1=np.array([(a1,b1),(a2,b2),(a3,b3),(a4,b4)])
                 pts2=np.float32([[0,0],[w,0],[w,h],[0,h]])
                 matrix, _ =cv2.findHomography(pts2,pts1)
                 imgOut=cv2.warpPerspective(img4,matrix,(img.shape[1],img.shape[0]))
                 cv2.fillConvexPoly(img,pts1.astype(int),(0,0,0))
                 img=img+imgOut
                
               elif np.any(img[cy,cx]==[9, 127, 240]):
                   
                 h,w,c=img5.shape                   
                 pts1=np.array([(a1,b1),(a2,b2),(a3,b3),(a4,b4)])
                 pts2=np.float32([[0,0],[w,0],[w,h],[0,h]])
                 matrix, _ =cv2.findHomography(pts2,pts1)
                 imgOut=cv2.warpPerspective(img5,matrix,(img.shape[1],img.shape[0]))
                 cv2.fillConvexPoly(img,pts1.astype(int),(0,0,0))
                 img=img+imgOut
               
               elif np.any(img[cy,cx]==[210, 222, 228]):
                   
                 h,w,c=img3.shape                   
                 pts1=np.array([(a1,b1),(a2,b2),(a3,b3),(a4,b4)])
                 pts2=np.float32([[0,0],[w,0],[w,h],[0,h]])
                 matrix, _ =cv2.findHomography(pts2,pts1)
                 imgOut=cv2.warpPerspective(img3,matrix,(img.shape[1],img.shape[0]))
                 cv2.fillConvexPoly(img,pts1.astype(int),(0,0,0))
                 img=img+imgOut
                 
               elif np.any(img[cy,cx]==[0,0,0]):
                 h,w,c=img2.shape                   
                 pts1=np.array([(a1,b1),(a2,b2),(a3,b3),(a4,b4)])
                 pts2=np.float32([[0,0],[w,0],[w,h],[0,h]])
                 matrix, _ =cv2.findHomography(pts2,pts1)
                 imgOut=cv2.warpPerspective(img2,matrix,(img.shape[1],img.shape[0]))
                 cv2.fillConvexPoly(img,pts1.astype(int),(0,0,0))
                 img=img+imgOut
                   
                  
                 
    cv2.imshow("output",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thrash = cv2.threshold(grey,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thrash,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
my_function(img,contours)

   
