import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# initialize the webcam
cap = cv2.VideoCapture(0)

# set the resolution of the webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# initialize the hand tracking model
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while True:
        # read a frame from the webcam
        ret, frame = cap.read()

        # flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # convert the frame to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # detect and track the hand in the frame
        results = hands.process(image)

        # draw the hand landmarks on the frame
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # display the frame
        cv2.imshow('Hand Tracking', frame)

        # check if the user pressed the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# release the webcam and close the window
cap.release()
cv2.destroyAllWindows()