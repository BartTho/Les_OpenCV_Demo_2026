import cv2
import numpy as np

cap = cv2.VideoCapture(1)
while(True):
    ret, frame = cap.read()
    lijn = cv2.line(frame, (10, 10), (640, 480), (255, 0, 0), 5)
    cv2.imshow('video', lijn)

    cirkel = cv2.circle(frame, (320, 240), 200, (0, 255, 0), -1)
    cv2.imshow('video', cirkel)

    elips = cv2.ellipse(frame, (320, 240), (200, 100), 0, 0, 360, (0, 0, 255), -1)
    cv2.imshow('video', elips)

    veelhoek = cv2.polylines(frame, [np.array([[10, 10], [10, 500], [500, 500], [500, 10]])], True, (255, 255, 0), 10)
    cv2.imshow('video', veelhoek)

    tekst = cv2.putText(frame, 'Bart Thonissen', (10, 470), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)
    cv2.imshow('video', tekst)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()