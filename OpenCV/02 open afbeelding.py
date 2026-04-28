import cv2

logo = cv2.imread('Afbeeldingen/logo.png')
cv2.imshow('Logo', logo)
cv2.imwrite('Afbeeldingen/logo.jpg', logo)
cv2.waitKey(0)
cv2.destroyAllWindows()