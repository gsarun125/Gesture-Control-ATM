import cv2
import mediapipe as mp
import win32api, win32con

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)  # Open default camera

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        image_height, image_width, _ = image.shape
        image.flags.writeable = False
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                m_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
                m_y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
                print(f'{m_x, m_y}')
                win32api.SetCursorPos((m_x, m_y))
                #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, m_x, m_y, 0, 0)
                #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, m_x, m_y, 0, 0)
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Tracking", image)

        if cv2.waitKey(5) & 0xFF == 27:  # Press Escape key to exit
            break

cap.release()
cv2.destroyAllWindows()