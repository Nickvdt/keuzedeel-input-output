import cv2
import time
import datetime
import pyttsx3

#Tekst naar spraak engine roep ik hier aan.
engine = pyttsx3.init()

# Opent de webcam en je kan de nummer veranderen om een andere camera/webcam te gebruiken
webcam = cv2.VideoCapture(0)


while True:
    _, frame1 = webcam.read() #Leest de eerste frame van de camera en slaat het op in de variabele: frame 1, de underscore wordt overgeslagen
    _, frame2 = webcam.read() #Leest de eerste frame van de camera en slaat het op in de variabele: frame 2, de underscore wordt overgeslagen

    # Bereken het verschil tussen de twee frames en sla het op in diff
    diff = cv2.absdiff(frame1, frame2)

    # Converteer het verschil naar grijs en zoek daar het verschil in (in plaats van een waarde voor rood, groen en blauw).
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # cv2.threshold() functie, die een afbeelding in twee delen verdeelt.
    # Hier wordt de drempelwaarde ingesteld op 25, en alles boven de 25 wordt wit, alles eronder wordt zwart.
    # De [1] achter de functie geeft aan dat alleen het tweede element van de teruggegeven tuple wordt gebruikt, dat is de afbeelding met de drempelwaarde.
    threshold = cv2.threshold(mask, 25, 255, cv2.THRESH_BINARY)[1]

    # Deze regel code zoekt naar contouren in de afbeelding met de drempelwaarde.
    # Contouren zijn de randen van objecten in een afbeelding.
    # Hier wordt de cv2.findContours() functie gebruikt om contouren te vinden in de afbeelding met de drempelwaarde. 
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop door de contouren
    for c in contours:
        # . Als de grootte van de contour groter is dan 1000 pixels, wordt de string "Beweging gedetecteerd!" naar de console geprint.
        if cv2.contourArea(c) > 1000:
            print("Beweging gedetecteerd!")
            time.sleep(7)
            engine.say("prepare to")
            engine.say("take a photo")
            time.sleep(5)
            now = datetime.datetime.now() # Haalt de huidige tijd op
            timer = 0 # Zet de timer op 0
            while timer < 5:
                engine.say(f"{5 - timer}")
                engine.runAndWait()
                # Wacht 1 seconde
                time.sleep(1)
                # Tel 1 seconde op bij de timer
                timer += 1
                # Geef de timer hardop weer
                print(f"Timer: {timer} sec")
            _, frame = webcam.read()
            engine.say("the photo is taken")
            engine.runAndWait()
            filename = f"{now:%Y%m%d-%H%M%S}.jpg" # Maak een bestandnaam met  datum en tijd
            cv2.imwrite(filename, frame) # De afbeelding zal worden opgeslagen in dezelfde map waar camera.py zit.
            cv2.imshow("Foto", frame) # geeft de afbeelding op het scherm
            cv2.waitKey() # Wacht tot dat de gebruiker een toets indrukt zodat de afbeelding weg gaat.