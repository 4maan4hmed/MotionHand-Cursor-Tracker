import cv2
import mediapipe as mp
import pyautogui as gui

vid = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

thumb_x = 0
thumb_y = 0
ind_x = 0
ind_y = 0
clicked = False

while True:
    ret, frame = vid.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    screen_width, screen_height = gui.size()

    col_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hands.process(col_frame)
    hands_landmarks = output.multi_hand_landmarks

    if hands_landmarks:
        for hand_landmarks in hands_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark

            for index, mark in enumerate(landmarks):
                if index == 8:
                    ind_x = int(mark.x * frame_width)
                    ind_y = int(mark.y * frame_height)
                    cv2.circle(frame, (ind_x, ind_y), 10, (255, 0, 0), -1)
                    x = int(mark.x * screen_width)
                    y = int(mark.y * screen_height)
                    gui.moveTo(x, y)

                if index == 4:
                    thumb_x = int(mark.x * frame_width)
                    thumb_y = int(mark.y * frame_height)
                    cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 0, 255), -1)

            thumb_pos = thumb_x + thumb_y
            index_pos = ind_x + ind_y

            if abs(thumb_pos - index_pos) < 50:
                if not clicked:
                    gui.click()
                    clicked = True
            else:
                clicked = False

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()