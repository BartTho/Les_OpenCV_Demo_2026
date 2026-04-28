import cv2

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Videos/output.avi', fourcc, 20.0, (640, 480))
while(True):
    ret, frame = cap.read()
    flip = cv2.flip(frame, 1)
    out.write(flip)
    cv2.imshow('video', flip)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()