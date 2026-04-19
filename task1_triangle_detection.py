import cv2
import numpy as np

# Open default webcam
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Webcam started successfully.")
print("Press 'q' to quit.")

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Resize frame for easier viewing
    frame = cv2.resize(frame, (960, 720))

    # Make a copy for drawing results
    output = frame.copy()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using Canny
    edges = cv2.Canny(blurred, 75, 200)

    # Detect lines using Probabilistic Hough Transform
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=80,
        minLineLength=100,
        maxLineGap=20
    )

    line_count = 0

    # Draw detected lines
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]

            # Calculate line length to remove tiny noisy lines
            length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            if length > 80:
                cv2.line(output, (x1, y1), (x2, y2), (0, 255, 0), 2)
                line_count += 1

    # Detect corners using Shi-Tomasi method
    corners = cv2.goodFeaturesToTrack(
        gray,
        maxCorners=10,
        qualityLevel=0.03,
        minDistance=25
    )

    corner_count = 0

    # Draw detected corners
    if corners is not None:
        corners = np.int32(corners)

        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(output, (x, y), 5, (0, 0, 255), -1)
            corner_count += 1

    # Show counts on screen
    cv2.putText(
        output,
        f"Lines Detected: {line_count}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        output,
        f"Corners Detected: {corner_count}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    # Display windows
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Edges", edges)
    cv2.imshow("Detected Lines and Corners", output)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close all windows
cap.release()
cv2.destroyAllWindows()
