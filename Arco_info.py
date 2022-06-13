import cv2
import cv2.aruco as aruco

img1 = cv2.imread("D:\RONY\IIT Dhanbad\Atulya\My Project\Ha.jpg")
img2= cv2.imread("D:\RONY\IIT Dhanbad\Atulya\My Project\HaHa.jpg")
img3 = cv2.imread("D:\RONY\IIT Dhanbad\Atulya\My Project\LMAO.jpg")
img4 = cv2.imread("D:\RONY\IIT Dhanbad\Atulya\My Project\XD.jpg")




def findAruco(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    key=getattr(aruco,f'DICT_5X5_250')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    
    (corners,ids,rejected) =  cv2.aruco.detectMarkers(img,arucoDict,parameters=arucoParam)
    
    
    if len(corners) > 0 :
       ids= ids.flatten()
       
       for(markerCorner,markerId) in zip(corners,ids):
           corners = markerCorner.reshape((4,2))
           (topLeft,topRight,bottomRight,bottomLeft) = corners 
           
           topRight= (int(topRight[0]),int(topRight[1]))
           topLeft= (int(topLeft[0]),int(topLeft[1]))
           bottomLeft= (int(bottomLeft[0]),int(bottomLeft[1]))
           bottomRight= (int(bottomRight[0]),int(bottomRight[1]))
           
           cx=int((topLeft[0]+bottomRight[0])/2.0)
           cy=int((topLeft[1]+bottomRight[1])/2.0)
           
           cv2.circle(img,(cx,cy),5,(255,0,0),-1)
           cv2.putText(img,str(markerId),(cx,cy-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv2.LINE_AA)
           return (markerId)
           
    
a=findAruco(img4)
print(a)
cv2.imshow("output",img4)
print(img4.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
