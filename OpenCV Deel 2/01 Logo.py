import cv2

logo = cv2.imread("Afbeeldingen/Logo.png")
logoKlein = cv2.resize(logo, (200, 200))

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()

    rij,  kol, kanaal = logoKlein.shape
    frame[0:rij, 0:kol] = logoKlein

    cv2.imshow("Scherm", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()