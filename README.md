# OpenCV_task
In this task I had to autonomously put aruco markers on square boxes. My task was to write a python code, for finding square boxes in an image and then place aruco markers exactly overlapping on it with some given rules and keeping the orientations in mind.


First, I defined a function named findAruco() which gave me the corresponding Ids of the aruco markers of which I kept a note of.
However I did not rename those files with their corresponding Ids. It also displayed the aruco markers centre and this program I have submitted in a separate Python file named 'Aruco_info.py'

Secondly, I rotated the aruco markers by rotating them through suitable angle determined by the slope and cropped those to get only the aruco markers and not their white background. The cropped images are attached in a separate folder and also their python codes.

Finally, I read the larger image ,determined its contours and also determined their colors.Simultaneously I pasted the cropped images according to the ids.

