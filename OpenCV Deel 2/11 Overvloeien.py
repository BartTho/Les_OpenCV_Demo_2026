import numpy as np
import cv2

img = cv2.imread('Afbeeldingen/logo.png')

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    img_resized = cv2.resize(img, (frame.shape[1], frame.shape[0]))
    dst = cv2.addWeighted(frame,0.7,img_resized,0.3,0)
    cv2.imshow('Overvloeien',dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()