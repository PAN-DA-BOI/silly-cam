import cv2

# Initialize the camera
cap = cv2.VideoCapture(1)  # Use 0 for the default camera, change if needed
cap = cv2.VideoCapture(1)  # Use 0 for the default camera, change if needed
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Create a window to display the camera feed
cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Initialize variables
picture_count = 0

try:
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply the COLORMAP_HOT colormap to the grayscale frame
        colored_frame = cv2.applyColorMap(gray_frame, cv2.COLORMAP_HOT)

        # Display the colored frame in the window
        cv2.imshow("Camera", colored_frame)

        # Check if the space bar is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):
            # Take a picture
            picture_name = f"picture_{picture_count}.jpg"
            cv2.imwrite(picture_name, frame)  # Save in color
            print(f"Picture {picture_name} taken")
            picture_count += 1

        # Check if the user pressed the 'q' key to quit
        if key == ord('q'):
            break

except KeyboardInterrupt:
    pass

finally:
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
