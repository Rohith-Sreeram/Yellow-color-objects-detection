#Simple yellow object detector
import cv2
import numpy as np
video=cv2.VideoCapture(0)
low=np.array([20,100,100])
high=np.array([30,255,255])
while True:
    ret,frame=video.read()
    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(frame_hsv,low,high)
    mask_m=cv2.dilate(mask,np.ones((5,5),dtype="int"),iterations=15)
    contours,_=cv2.findContours(mask_m,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x1,y1,w,h=cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x1,y1),(x1+w,y1+h),(255,0,0),1) 
    cv2.putText(frame,f"the total number of yellow objects: {len(contours)}", (10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)       
    cv2.imshow("live",frame)    
    if cv2.waitKey(20) & 0xFF==ord("a"):
        break 
video.release()  
cv2.destroyAllWindows()     
