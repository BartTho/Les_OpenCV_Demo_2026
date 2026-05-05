import cv2

logo = cv2.imread('Afbeeldingen/logo.jpg')
logoKlein = cv2.resize(logo, (200, 200))

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()

    rows,cols,channels = logoKlein.shape

    frame[0:rows, 0:cols ] = logoKlein
    cv2.imshow('res',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()