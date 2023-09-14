import cv2

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Set the screen dimensions
screen_width = 1200
screen_height = 800

# Create a resizable window for the webcam feed
cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam", screen_width, screen_height)

while True:
    # Read a frame from the camera feed
    success, frame = cap.read()

    if not success:
        break

    # Resize the frame to match the desired screen dimensions
    frame = cv2.resize(frame, (screen_width, screen_height))

    # Flip the frame horizontally for a mirrored effect (1 for horizontal flip)
    mirrored_frame = cv2.flip(frame, 1)

    # Display the mirrored frame in the "Webcam" window
    cv2.imshow("Webcam", mirrored_frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
