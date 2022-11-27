import cv2
slides =[]
countOfSlides=8
for i in range(1,countOfSlides+1):
    slides.append(cv2.imread(f"slajd{i}.png"))