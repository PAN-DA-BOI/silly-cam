import cv2
import RPi.GPIO as GPIO
import time

# Set up the button pin
button_pin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the camera
cap = cv2.VideoCapture(0)
cap.set(3, 480)  # Width
cap.set(4, 320)  # Height

# Create a window to display the camera feed
cv2.namedWindow("Camera", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Initialize variables
picture_count = 0

try:
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Display the frame in the window
        cv2.imshow("Camera", frame)

        # Check if the button is pressed
        if GPIO.input(button_pin) == GPIO.LOW:
            # Take a picture
            picture_name = f"picture_{picture_count}.jpg"
            cv2.imwrite(picture_name, frame)
            print(f"Picture {picture_name} taken")
            picture_count += 1

            # Wait for a short time to debounce the button
            time.sleep(0.3)

        # Check if the user pressed the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass

finally:
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
