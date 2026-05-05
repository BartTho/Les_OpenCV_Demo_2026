import cv2
import numpy as np

background = cv2.imread('Afbeeldingen/eiland.jpg')

# Webcam openen
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Kan de webcam niet openen. Controleer of een camera beschikbaar is.")

# Haarcascade voor gezichtdetectie
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]
    background_resized = cv2.resize(background, (width, height), interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))

    mask = np.zeros((height, width), dtype=np.uint8)
    if len(faces) > 0:
        # Gebruik het grootste gedetecteerde gezicht
        x, y, w, h = sorted(faces, key=lambda r: r[2] * r[3], reverse=True)[0]
        x0 = max(x - w // 4, 0)
        y0 = max(y - h // 2, 0)
        x1 = min(x + w + w // 4, width)
        y1 = min(y + h + h // 2, height)

        center = ((x0 + x1) // 2, (y0 + y1) // 2)
        axes = ((x1 - x0) // 2, (y1 - y0) // 2)
        cv2.ellipse(mask, center, axes, angle=0, startAngle=0, endAngle=360, color=255, thickness=-1)
        mask = cv2.GaussianBlur(mask, (31, 31), 0)
    else:
        cv2.putText(
            background_resized,
            "Plaats je gezicht voor de camera",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

    mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    foreground = cv2.bitwise_and(frame, mask_3ch)
    background_part = cv2.bitwise_and(background_resized, cv2.bitwise_not(mask_3ch))
    output = cv2.add(background_part, foreground)

    cv2.imshow("Achtergrond met eiland", output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
