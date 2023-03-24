import cv2
import time
import mediapipe as mp
import win32api, win32con
from PIL import Image, ImageTk
from vec import *

class Hamigi:
    def __init__(self):
        self.mp_drawing=mp.solutions.drawing_utils
        self.mp_hands=mp.solutions.hands
        self.cap = cv2.VideoCapture(0)  # Open default camera
        
        self.delta_cur_mov=vec2()
        self.__hands=self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.7)
        self.__prev_cur_pos=vec2()
        self.__curr_cur_pos=vec2()

    def run(self):
        #with self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.7) as hands:
        smooth=1.25
        self.mouse_pos = vec2(300, 300)
        while self.cap.isOpened():
            success, self.image = self.cap.read()
            if not success:
                continue

            curr_frame_time=time.time()

            self.image = cv2.cvtColor(cv2.flip(self.image, 1), cv2.COLOR_BGR2RGB)

            image_height, image_width, _ = self.image.shape
            self.image.flags.writeable = False
            results = self.__hands.process(self.image)

            self.image.flags.writeable = True
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    m_x = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
                    m_y = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
                    self.__curr_cur_pos = vec2(m_x, m_y)
                    self.__delta_cur_mov = self.__curr_cur_pos - self.__prev_cur_pos
                    self.mouse_pos += self.__delta_cur_mov * smooth
                    print(self.__delta_cur_mov)
                    #for t in [x / 10.0 for x in range(1, 10, 1)]:
                        #l=0
                        #self.delta_cur_pos = self.self.__curr_cur_pos.lerp(self.__prev_cur_pos, t)
                    win32api.SetCursorPos(self.mouse_pos.getIntTup())
                    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, m_x, m_y, 0, 0)
                    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, m_x, m_y, 0, 0)
                    self.mp_drawing.draw_landmarks(self.image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            else:
                self.mouse_pos = vec2(300, 300)
                #print("no arm: ", i)
            
            self.__prev_cur_pos = self.__curr_cur_pos
            #cv2.imshow("Hand Tracking", self.image)

            if cv2.waitKey(5) & 0xFF == 27:  # Press Escape key to exit
                break

        self.cap.release()

    def get_image(self):
        return self.image

hand = Hamigi()
hand.run()