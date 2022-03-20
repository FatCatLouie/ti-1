import cv2
import mediapipe as mp

print ("hi")

camera = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
#mpDraw = mp.solutions.drawing_utils
#
# w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
# #video_writer = cv2.VideoWriter('d:\\vcap.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 25, (w, h))
# #video_writer = cv2.VideoWriter('d:\\vcap.mp4', cv2.VideoWriter_fourcc(*'XVID'), 25, (w, h))
#
while True:
    good, img = camera.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#    results = hands.process(imgRGB)
#     if results.multi_hand_landmarks:
#         for handLMS in results.multi_hand_landmarks:
#             mpDraw.draw_landmarks(img, handLMS, mpHands.HAND_CONNECTIONS)
    cv2.imshow("Image", img)
#     #video_writer.write(img)
    if cv2.waitKey(1) == ord('q'):
        break
print("bye")
