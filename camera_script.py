import cv2
import RPi.GPIO as GPIO
import time
import threading

# Set up the button pin
button_pin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the camera
cap = cv2.VideoCapture(0)
cap.set(3, 480)  # Width for display
cap.set(4, 320)  # Height for display

# Initialize variables
picture_count = 0

def display_feed():
    global cap
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

        # Check if the user pressed the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def take_picture():
    global cap, picture_count
    while True:
        # Check if the button is pressed
        if GPIO.input(button_pin) == GPIO.LOW:
            # Temporarily change the resolution to 1080p
            cap.set(3, 1920)  # Width for 1080p
            cap.set(4, 1080)  # Height for 1080p
            time.sleep(1)  # Wait for the camera to adjust

            # Read a frame from the camera
            ret, frame = cap.read()
            if ret:
                # Save the frame as a picture
                picture_name = f"/home/camera-pi/pictures/picture_{picture_count}.jpg"
                cv2.imwrite(picture_name, frame)  # Save in color
                print(f"Picture {picture_name} taken")
                picture_count += 1

            # Reset the resolution to 480x320
            cap.set(3, 480)  # Width for display
            cap.set(4, 320)  # Height for display
            time.sleep(0.3)  # Debounce the button

def cleanup():
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()

try:
    # Start the display feed thread
    display_thread = threading.Thread(target=display_feed)
    display_thread.start()

    # Start the take picture thread
    picture_thread = threading.Thread(target=take_picture)
    picture_thread.start()

    # Wait for both threads to complete
    display_thread.join()
    picture_thread.join()

except KeyboardInterrupt:
    pass

finally:
    cleanup()
