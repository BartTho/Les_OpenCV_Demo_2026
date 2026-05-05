# Oefening 2: Detectiebox simuleren
# Teken een cirkel rond de bal op de foto van messi.jpg
# zet er de tekst bij BAL

import cv2

image = cv2.imread("Afbeeldingen/messi.jpg")

if image is None:
    print("Kan de afbeelding niet laden: Afbeeldingen/messi.jpg")
    exit(1)

# Functie voor muisgebeurtenissen
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coördinaten: ({x}, {y})")

# Venster maken en callback instellen
cv2.namedWindow("Messi")
cv2.setMouseCallback("Messi", mouse_callback)
print( image.shape )
# Afbeelding tonen
cv2.circle(image,(57,184),20,(255,0,0),-1)
cv2.putText(image, "BAL", (30, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow("Messi", image)

print("Klik met de linkermuisknop op de afbeelding om coördinaten te zien. Druk op 'q' om af te sluiten.")

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()