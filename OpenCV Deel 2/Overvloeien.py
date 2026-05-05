import cv2

img = cv2.imread("Afbeeldingen/logo.png")

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()

    if not ret:
        print("Fout bij het openen van de camera.")
        break

    img_resized = cv2.resize(img, (frame.shape[1], frame.shape[0]))
    doelFrame = cv2.addWeighted(frame, 0.8, img_resized, 0.2, 0)
    cv2.imshow("Scherm", doelFrame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()