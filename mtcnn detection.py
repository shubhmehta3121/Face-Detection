import cv2
from mtcnn import MTCNN

# Create a VideoCapture object to capture video from the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

# Create the MTCNN detector
detector = MTCNN()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Detect faces in the frame
    faces = detector.detect_faces(frame)

    # Draw bounding boxes around detected faces
    for face in faces:
        x, y, width, height = face['box']
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    # Display the frame with bounding boxes
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
