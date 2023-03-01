import cv2
from poseDetection import poseDetection
if_flip=True
DEBUG = True

class TestClass:
    def test_change_on_next_slide(self):
        cap = cv2.VideoCapture("video-1647700348.mp4")
        while True:
            ret, img = cap.read()
            flipcode = 1
            if if_flip:
                img = cv2.flip(img, flipcode)  # image from camera flip horizontally
            # handsDetecion(img) # function detecting hands from image flipped
            ifChangeSlide = poseDetection(img, DEBUG)  # function detecting pose from image flipped
            print(ifChangeSlide)
            if ifChangeSlide==True:
                assert True
