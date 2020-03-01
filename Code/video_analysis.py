import numpy as np
import cv2
import matplotlib.pyplot as plt
import Code.video_tools as video_tools
import Code.feature_extraction as ft
from Code.mfcc_talkbox import mfcc
import scipy.io.wavfile as wav
import math


def do_work_per_second(video_path):
    cap = cv2.VideoCapture(video_path)

    # store previous frame
    prev_frame = None
    CH = []
    # set video capture object to specific point in time
    cap.set(cv2.CAP_PROP_POS_MSEC, S * 1000)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("Frames per second {0}".format(fps))
    count = 0

    while cap.isOpened():
        retVal, frame = cap.read()

        if not retVal:
            break

        # == Do your processing here ==#
        if count % fps == 0:
            if prev_frame is not None:
                CH.append(colorhist_diff(frame, prev_frame))

        prev_frame = frame
        count += 1

        #
        # cv2.imshow('Video', frame)
        # cv2.waitKey()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print(CH)

    plot_difference_sum(CH)


def colorhist_diff(frame, prev_frame):
    diff = 0
    hist = ft.colorhist(frame)
    prev_hist = ft.colorhist(prev_frame)

    for i in range(hist.shape[1]):
        diff = diff + np.sum(np.abs(prev_hist[:, i] - hist[:, i]))
    return diff


def plot_difference_sum(ch):
    sum = []

    if len(ch) <= 1:
        print("insufficient values for plot")
        return

    for i in range(0, len(ch) - 1):
        curr = ch[i] + ch[i + 1]
        sum.append(curr)

    plt.stem(sum)
    plt.show()
    return sum


def work_for_audio_per_second(path):
    video_path = path + '.avi'
    cap = cv2.VideoCapture(video_path)

    audio_path = path + '.wav'
    samplerate, samples = wav.read(audio_path)
    # print(samplerate) 8000

    plt.plot(samples)
    plt.show()

    # prev_frame = None
    CH = []
    # set video capture object to specific point in time

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("Frames per second {0}".format(fps))
    count = 0

    while cap.isOpened():
        retVal, frame = cap.read()

        if not retVal:
            break

        # == Do your processing here ==#
        # if count % fps == 0:



        # prev_frame = frame
        count += 1

        #
        # cv2.imshow('Video', frame)
        # cv2.waitKey()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Path to video file to analyse
video1 = '/Users/pd/PycharmProjects/MA_Labs/mma-lab/Videos/video_07.mp4'
video2 = '/Users/pd/PycharmProjects/MA_Labs/mma-lab/Videos/TUDelft_Ambulance_Drone.mp4'

# starting point
S = 0  # seconds
# stop at
E = 1  # seconds

# Retrieve frame count. We need to add one to the frame count because cv2 somehow 
# has one extra frame compared to the number returned by ffprobe.
frame_count = video_tools.get_frame_count(video1) + 1
frame_rate = video_tools.get_frame_rate(video1)

# do_work_per_second(video1)
# do_work_per_second(video2)

work_for_audio_per_second('/Users/pd/PycharmProjects/MA_Labs/mma-lab/Videos/BlackKnight')


