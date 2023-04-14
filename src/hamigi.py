import cv2
import threading
import mediapipe as mp
import win32api
import win32con
from vec import *

class Fings:
    def __init__(self):
        self.__handed=0 # 0 - No Hand, 1 - Left, 2 - Right
        self.thumb=vec2()
        self.index=vec2()
        self.mid=vec2()
        self.ring=vec2()
        self.pinky=vec2()
    
    def get_hand(self):
        return self.__handed

    def __set_hand(self):
        if(self.thumb.x - self.pinky.x > 0):
            self.__handed=1
        else:
            self.__handed=2

    def set_fing_pos(self, tmb=vec2(), ind=vec2(), mid=vec2(), rin=vec2(), pnk=vec2()):
        self.thumb=tmb
        self.index=ind
        self.mid=mid
        self.ring=rin
        self.pinky=pnk
        self.__set_hand()

    def reset(self):
        self.__handed=0
        self.thumb=vec2()
        self.index=vec2()
        self.mid=vec2()
        self.ring=vec2()
        self.pinky=vec2()

    # Thumb Click
    def gest1(self):
        if(self.__handed == 1):
            if(self.mid.x - self.thumb.x > 0):
                return True
            return False
        elif(self.__handed == 2):
            if(self.mid.x - self.thumb.x < 0):
                return True
            return False
    
    def gest2():
        return True

class Hamigi(threading.Thread):
    def __init__(self, screenCentre=vec2(300, 300)):
        threading.Thread.__init__(self)
        self.mp_drawing=mp.solutions.drawing_utils
        self.mp_hands=mp.solutions.hands
        self.cap = cv2.VideoCapture(0)  # Open default camera
        
        self.delta_cur_mov=vec2()
        self.__hands=self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.7)
        self.__fingData = Fings()
        self.__def_mouse_pos=screenCentre
        self.__prev_cur_pos=vec2()
        self.__curr_cur_pos=vec2()
        self.mouse_pos=self.__def_mouse_pos
        self.image=cv2.Mat

    def run(self):
        #with self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.7) as hands:
        smooth=1
        while self.cap.isOpened():
            success, self.image = self.cap.read()
            if not success:
                continue

            self.image = cv2.cvtColor(cv2.flip(self.image, 1), cv2.COLOR_BGR2RGB)

            image_height, image_width, _ = self.image.shape
            self.image.flags.writeable = False
            results = self.__hands.process(self.image)

            self.image.flags.writeable = True
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    t_x = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x * image_width)
                    t_y = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y * image_height)

                    i_x = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
                    i_y = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)

                    m_x = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width)
                    m_y = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height)

                    r_x = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width)
                    r_y = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height)
                    
                    p_x = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].x * image_width)
                    p_y = int(hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y * image_height)

                    self.__fingData.set_fing_pos(vec2(t_x, t_y), vec2(i_x, i_y), vec2(m_x, m_y), vec2(r_x, r_y), vec2(p_x, p_y))
                    
                    self.__curr_cur_pos = vec2(m_x, m_y)
                    self.__delta_cur_mov = self.__curr_cur_pos - self.__prev_cur_pos
                    self.mouse_pos += self.__delta_cur_mov * smooth
                    #print(self.__delta_cur_mov)
                    #for t in [x / 10.0 for x in range(1, 10, 1)]:
                        #l=0
                        #self.delta_cur_pos = self.self.__curr_cur_pos.lerp(self.__prev_cur_pos, t)
                    win32api.SetCursorPos(self.mouse_pos.getIntTup())

                    if(self.__fingData.gest1()):
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, m_x, m_y, 0, 0)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, m_x, m_y, 0, 0)

                    self.mp_drawing.draw_landmarks(self.image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            else:
                self.mouse_pos=self.__def_mouse_pos
                self.__fingData.reset()
                #print("no arm: ", i)
            
            self.__prev_cur_pos = self.__curr_cur_pos
            
            handedness = "No Hand"
            if self.__fingData.get_hand() == 1:
                handedness = "Left Handed"
            elif self.__fingData.get_hand() == 2:
                handedness = "Right Handed"

            print(handedness)
            #self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            cv2.imshow("Hand Tracking", self.image)

            if cv2.waitKey(123) & 0xFF == 27:  # Press Escape key to exit
                break

        self.cap.release()

    def get_image(self):
        return self.image

hand = Hamigi()
hand.start()

#from window import Window
#from PIL import Image, ImageTk
#import tkinter as tk


#win=Window(800, 600)
#tkk=win.get_window()
#img=Image.fromarray(hand.get_image())
#img = ImageTk.PhotoImage(img)
#label=tk.Label(tkk, image=img)
#tkk.mainloop()