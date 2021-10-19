import cv2
import numpy as np


#   SETTINGS START
CAMERA_ID = 0
#   SETTINGS END


cap = cv2.VideoCapture(CAMERA_ID, cv2.CAP_DSHOW)

while (True):

    #   Get new frame
    ret, frame = cap.read()
   
   #    Show framw
    cv2.imshow("Move camera... (Press q for quit)", frame)

    #   If press q or the mapping stops: exit the cycle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#   Release the webcam
cap.release()
cv2.destroyAllWindows()
