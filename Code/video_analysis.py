import numpy as np
import cv2
import matplotlib.pyplot as plt
import Code.video_tools as video_tools
import Code.feature_extraction as ft
from Code.mfcc_talkbox import mfcc

# Path to video file to analyse 
video = '/Users/pd/PycharmProjects/MA_Labs/mma-lab/Videos/video_07.mp4'

# starting point
S = 0  # seconds
# stop at
E = 1  # seconds

# Retrieve frame count. We need to add one to the frame count because cv2 somehow 
# has one extra frame compared to the number returned by ffprobe.
frame_count = video_tools.get_frame_count(video) + 1
frame_rate = video_tools.get_frame_rate(video)

# create an cv2 capture object
cap = cv2.VideoCapture(video)

# store previous frame
prev_frame = None

# set video capture object to specific point in time
cap.set(cv2.CAP_PROP_POS_MSEC, S * 1000)

while cap.isOpened() and cap.get(cv2.CAP_PROP_POS_MSEC) < (E * 1000):

    # 
    retVal, frame = cap.read()
    # 
    if not retVal:
        break

    # == Do your processing here ==#

    #
    cv2.imshow('Video', frame)
    cv2.waitKey()

    #
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    prev_frame = frame

#
cap.release()
cv2.destroyAllWindows()
