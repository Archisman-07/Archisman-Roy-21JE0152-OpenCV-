import cv2 
import math
import numpy as np
import cv2.aruco as aruco

angle=0

def subimage(image):                       
   arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_250)
   arucoParams = cv2.aruco.DetectorParameters_create()
   (corners1, ids1, rejected1) = cv2.aruco.detectMarkers(image, arucoDict,
       parameters=arucoParams)
       
   for (markerCorner,markerId) in zip (corners1,ids1):
       bbox=markerCorner.reshape((4,2))
       (tl,tr,br,bl)=bbox
       
                        
       shape = ( image.shape[1], image.shape[0] ) 
       center=(tl+br)/2
       matrix = cv2.getRotationMatrix2D( center=center, angle=angle, scale=1 )
       image = cv2.warpAffine( src=image, M=matrix, dsize=shape )
       

       return image
       


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
           

           slope=(topLeft[1]-bottomLeft[1])/(topLeft[0]-bottomLeft[0])
           angle=np.degrees(math.atan(slope))
           
           cx=int((topLeft[0]+bottomRight[0])/2.0)
           cy=int((topLeft[1]+bottomRight[1])/2.0)
           
          
           return markerId,angle
       
        
def crop(img):
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
           
           print(topRight)
           print(topLeft)
           print(bottomLeft)
           print(bottomRight)

           
           cx=int((topLeft[0]+bottomRight[0])/2.0)
           cy=int((topLeft[1]+bottomRight[1])/2.0)
           
           cropped_image = img[65:529, 66:530]
           cv2.imshow("cropped",cropped_image)
           cv2.imwrite("XD_cropped.jpg",cropped_image)
           cv2.waitKey(0)
           cv2.destroyAllWindows()
           

    
      
img3 = cv2.imread("D:\RONY\IIT Dhanbad\Atulya\My Project\XD.jpg")
markerId,angle=findAruco(img3)
a=subimage(img3)
cv2.imshow("output",a)
cv2.waitKey(0)
cv2.destroyAllWindows()

crop(a)

