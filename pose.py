import mediapipe as mp

class Pose():
    mpPose=mp.solutions.pose
    pose=mpPose.Pose()
    mwDraw = mp.solutions.drawing_utils