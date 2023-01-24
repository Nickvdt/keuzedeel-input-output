import cv2
for i in range(10):
    webcam = cv2.VideoCapture(i)
    if webcam.isOpened():
        print(f"Webcam met apparaat-ID {i} is beschikbaar")
    else:
        print(f"Webcam met apparaat-ID {i} is niet beschikbaar")

        