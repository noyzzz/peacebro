import cv2
import mediapipe as mp

# 🧠 Replace this with your actual IP Webcam video URL
IP_CAM_URL = "http://192.168.1.79:8080/video"

# Initialize video stream from IP Webcam
cap = cv2.VideoCapture(IP_CAM_URL, cv2.CAP_FFMPEG)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Drawing utility
mp_drawing = mp.solutions.drawing_utils

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame.")
        break

    # Flip horizontally for selfie-view and convert BGR → RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process with MediaPipe
    results = hands.process(rgb_frame)

    # Draw landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # Show the frame
    cv2.imshow("MediaPipe Hands", frame)
    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
