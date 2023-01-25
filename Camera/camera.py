import cv2
import time
import datetime
import pyttsx3

#tekst-naar-spraak-engine
engine = pyttsx3.init()

# Open de webcam en sla de eerste frame op
webcam = cv2.VideoCapture(0)
_, frame1 = webcam.read()

while True:
    # Lees het volgende frame van de webcam
    _, frame2 = webcam.read()

    # Bereken het verschil tussen de twee frames
    diff = cv2.absdiff(frame1, frame2)

    # Converteer het verschil naar zwart-wit en bepaal de drempelwaarde
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(mask, 25, 255, cv2.THRESH_BINARY)[1]

    # Zoek naar contouren in het zwart-wit verschil
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop door de contouren
    for c in contours:
        # Als de contour groter is dan een bepaalde drempelwaarde, wordt beweging gedetecteerd
        if cv2.contourArea(c) > 1000:
            print("Beweging gedetecteerd!")
            time.sleep(7)
            engine.say("prepare to")
            engine.say("take a photo")
            time.sleep(5)
            now = datetime.datetime.now()
            timer = 0
            while timer < 5:
                engine.say(f"{5 - timer}")
                engine.runAndWait()
                # Wacht 1 seconde
                time.sleep(1)
                # Tel 1 seconde op bij de timer
                timer += 1
                # Geef de timer hardop weer
                print(f"Timer: {timer} sec")
            engine.say("the photo is taken")
            engine.runAndWait()
            _, frame = webcam.read()
             # Maak een bestandnaam met  datum en tijd
            filename = f"{now:%Y%m%d-%H%M%S}.jpg"
            cv2.imwrite(filename, frame)
            cv2.imshow("Foto", frame)
            cv2.waitKey()