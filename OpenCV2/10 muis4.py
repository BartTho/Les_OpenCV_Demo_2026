import cv2
import numpy as np

# Global variables
selected_color = None
hsv_lower = None
hsv_upper = None

def select_color(event, x, y, flags, param):
    global selected_color, hsv_lower, hsv_upper
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the HSV value at the clicked point
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        selected_color = hsv_frame[y, x]
        # Define a range around the selected color
        hue = selected_color[0]
        sat = selected_color[1]
        val = selected_color[2]
        # Adjust the range as needed
        hsv_lower = np.array([max(0, hue - 10), max(0, sat - 50), max(0, val - 50)])
        hsv_upper = np.array([min(179, hue + 10), min(255, sat + 50), min(255, val + 50)])
        print(f"Selected HSV: {selected_color}, Range: {hsv_lower} - {hsv_upper}")

# Open webcam
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', select_color)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if selected_color is not None:
        # Convert to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Create mask
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
        # Morphological operations to clean the mask
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            # Find the largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest_contour) > 500:  # Minimum area threshold
                # Draw bounding box
                x, y, w, h = cv2.boundingRect(largest_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Draw center
                center_x = x + w // 2
                center_y = y + h // 2
                cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()