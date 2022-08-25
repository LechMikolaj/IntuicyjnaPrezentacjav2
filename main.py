import cv2
from fps import fps
from changingSlides import slides,countOfSlides
from slidesCounter import slideCounter
from poseDetection import poseDetection

import mediapipe as mp





handAtEnd=False
handAtBeginning=False






            # print("leftWrist_positionx:",leftWrist_positionx*h)
            # print("hip_positionx:",hip_positionx*h)
        #dopisac rozpoznawanie odpowiedniej pozycji reki na podstawie results.pose_landmarks
        #pozycja reki jak do przesuwania w prawo slajdu
        #dopisac ostrzeżenie o zbyt malej odleglosci



import time
pTime=0.0
import cv2
#function showing fps on image


slides =[]
countOfSlides=5
for i in range(1,countOfSlides+1):
    slides.append(cv2.imread(f"slajd{i}.png"))



DEBUG = True
if_flip=False
print_Hands=True
i=1
print(f"DEBUG:{DEBUG}")
# fps dziala

slideCounter(slides[0], i, countOfSlides) #first position of countOfSlides
cv2.imshow("Slide",slides[0])#first slide

cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture("video-1646058581.mp4")

while True:
    ret, img=cap.read()

    flipcode=1

    if if_flip:
        img=cv2.flip(img, flipcode)    #image from camera flip horizontally


    #handsDetecion(img) # function detecting hands from image flipped
    ifChangeSlide=poseDetection(img,DEBUG) # function detecting pose from image flipped
    if ifChangeSlide:

        i=i%(countOfSlides)
        slideCounter(slides[i], i+1, countOfSlides)
        cv2.imshow("Slide",slides[i])
        i=i+1

        if DEBUG:
            print(i)


    if DEBUG==True:
        fps(img) # function showing fps on image
    cv2.imshow("Image", img) #showing image
    cv2.waitKey(1)