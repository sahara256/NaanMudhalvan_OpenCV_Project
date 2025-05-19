import cv2
import numpy as np

# Load the video (or use 0 for webcam)
cap = cv2.VideoCapture("dronevideo.mp4")  # Change to 0 for webcam

# Create the background subtractor to detect motion areas
fgbg = cv2.createBackgroundSubtractorMOG2(history=200, varThreshold=50)

frame_number = 0
memory = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 360))
    original = frame.copy()

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Find contours in the foreground mask (moving areas)
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process each contour (potential moving object)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Filter small contours (noise)
        if w > 30 and h > 30:
            # Draw bounding box around detected moving object
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(frame, "Moving Object", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            memory.append(("Moving Object", frame_number, x, y, w, h))

    # Display the output
    cv2.imshow("Moving Object Detection (OpenCV Only)", frame)

    frame_number += 1

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()

# Optional: Print what was remembered (for debugging/logging)
print("DETECTED MOVING OBJECT MEMORY:")
for item in memory:
    print(item)