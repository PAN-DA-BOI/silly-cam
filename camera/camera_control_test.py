import cv2
import mediapipe as mp

# Mediapipe setup
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(
    model_selection=0,  # 0 for faster, 1 for more accurate
    min_detection_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

# Variables
use_usb_camera = False
recording = False
face_detection_active = False

def switch_camera():
    global use_usb_camera
    use_usb_camera = not use_usb_camera
    print("Switched to", "USB camera" if use_usb_camera else "built-in camera")

def take_picture(frame):
    cv2.imwrite('image.jpg', frame)
    print("Picture taken!")

def start_stop_video(out):
    global recording
    if recording:
        out.release()
        recording = False
        print("Video recording stopped.")
        return None
    else:
        out = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 60, (640, 480))
        recording = True
        print("Video recording started.")
        return out

def start_face_detection():
    global face_detection_active
    face_detection_active = not face_detection_active
    print("Face detection toggled.")

def main():
    global use_usb_camera, recording, face_detection_active

    cap = cv2.VideoCapture(1 if use_usb_camera else 0)
    out = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if face_detection_active:
            # Convert the BGR image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Process the image
            results = face_detection.process(image)
            # Convert the image back to BGR
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw the face detection annotations on the image
            if results.detections:
                for detection in results.detections:
                    # Get the bounding box coordinates
                    bounding_box = detection.location_data.relative_bounding_box
                    x, y = int(bounding_box.xmin * image.shape[1]), int(bounding_box.ymin * image.shape[0])
                    w, h = int(bounding_box.width * image.shape[1]), int(bounding_box.height * image.shape[0])

                    # Draw a black square over the face
                    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 0), -1)
                    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 0), 18)

            frame = image

        cv2.imshow('Camera', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('a'):
            switch_camera()
            cap.release()
            cap = cv2.VideoCapture(1 if use_usb_camera else 0)
        elif key == ord('s'):
            take_picture(frame)
        elif key == ord('d'):
            out = start_stop_video(out)
        elif key == ord('f'):
            start_face_detection()
        elif key == ord('q'):
            break

        if recording and out is not None:
            out.write(frame)

    cap.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
