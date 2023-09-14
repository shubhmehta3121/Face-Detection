import cv2
import numpy as np

# Initialize the face detection classifier using Haar-like features
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a video capture object for the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera feed
    success, frame = cap.read()

    if not success:
        break

    # Detect faces in the frame using the Haar cascade classifier
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Calculate the hypotenuse and radius for the detected face
        hypo = np.sqrt(w ** 2 + h ** 2)
        radius = int(hypo / 2)
        center = (x + w // 2, y + h // 2)

        # Draw a circle around the detected face
        cv2.circle(frame, center, radius, (0, 0, 255), 2)

        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw diagonal lines across the detected face
        cv2.line(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(frame, (x + w, y), (x, y + h), (255, 0, 0), 2)

    # Display the frame with face detection results
    cv2.imshow('Face Detection', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all open windows
cv2.destroyAllWindows()
