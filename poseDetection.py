import cv2
from pose import Pose
handAtEnd=False
handAtBeginning=False

def poseDetection(img,DEBUG):
    global handAtEnd
    global handAtBeginning
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mpPose=Pose.pose
    mpDraw = Pose.mwDraw
    results=mpPose.process(imgRGB)
    h,w,c=img.shape
    id_leftWrist=15
    id_hip=23
    leftWrist_positionx=0
    hip_positionx = 0
    if results.pose_landmarks:
        if DEBUG:
            mpDraw.draw_landmarks(img,results.pose_landmarks,Pose.mpPose.POSE_CONNECTIONS)
        for id,landmark in enumerate(results.pose_landmarks.landmark):
            if id==id_leftWrist:
                leftWrist_positionx =landmark.x
            if id==id_hip:
                hip_positionx =landmark.x
        if leftWrist_positionx*h < hip_positionx*h:
            handAtEnd=True
        if leftWrist_positionx*h > hip_positionx*h :
            handAtBeginning=True
        if handAtEnd==True and handAtBeginning==True:
            handAtEnd=False
            handAtBeginning=False
            if leftWrist_positionx * h < hip_positionx * h:
                return True
            else:
                return False
            # print("leftWrist_positionx:",leftWrist_positionx*h)
            # print("hip_positionx:",hip_positionx*h)
        #dopisac rozpoznawanie odpowiedniej pozycji reki na podstawie results.pose_landmarks
        #pozycja reki jak do przesuwania w prawo slajdu
        #dopisac ostrzeżenie o zbyt malej odleglosci