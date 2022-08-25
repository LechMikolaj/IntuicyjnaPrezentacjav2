import cv2
def slideCounter(slide,i,countOfSlides):
    cv2.putText(slide,f'{i}/{countOfSlides}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 100, 100), 2)