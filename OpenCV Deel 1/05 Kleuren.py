import cv2

cap = cv2.VideoCapture(1)
while(True):
    ret, frame = cap.read()
    grijs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('video', frame)
    cv2.imshow('grijs', grijs)
    cv2.imshow('hsv', hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()