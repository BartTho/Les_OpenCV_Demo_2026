import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def teken_cirkel(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(255,0,0),-1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),20,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',teken_cirkel)

while True:
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()