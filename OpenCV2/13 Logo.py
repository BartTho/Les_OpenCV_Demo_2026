import numpy as np
import cv2
def nothing(x):
    pass

logo = cv2.imread('opencv.jpg')

cv2.namedWindow('threshold')
# create trackbars for color change
cv2.createTrackbar('tMin','threshold',0,255,nothing)
cv2.createTrackbar('tMax','threshold',0,255,nothing)
cv2.setTrackbarPos('tMin','threshold',10)
cv2.setTrackbarPos('tMax','threshold',240)
cv2.imshow('threshold',logo)

cap = cv2.VideoCapture(1)
while(True):
    ret, frame = cap.read()
    # get current positions of four trackbars
    tMin = cv2.getTrackbarPos('tMin','threshold')
    tMax = cv2.getTrackbarPos('tMax','threshold')
    # I want to put logo on top-left corner, So I create a ROI
    #logo_resized = cv2.resize(logo, (frame.shape[1], frame.shape[0]))
    #rows,cols,channels = logo_resized.shape
    rows,cols,channels = logo.shape
    # Ensure logo fits within frame dimensions
    rows = min(rows, frame.shape[0])
    cols = min(cols, frame.shape[1])
    roi = frame[0:rows, 0:cols ]

    # Crop logo to match ROI size
    logo_cropped = logo[0:rows, 0:cols]

    # Now create a mask of logo and create its inverse mask also
    grijsLogo = cv2.cvtColor(logo_cropped,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(grijsLogo, tMin, tMax, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    frame_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    # Take only region of logo from logo image.
    logo_fg = cv2.bitwise_and(logo_cropped,logo_cropped,mask = mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(frame_bg,logo_fg)
    frame[0:rows, 0:cols ] = dst
    cv2.imshow('res',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()