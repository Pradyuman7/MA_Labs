import cv2
import numpy as np
import matplotlib.pyplot as plt


def work_per_second(video_path):
    cap = cv2.VideoCapture(video_path)

    prev_frame = None
    CH = []

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
                diff = np.abs(prev_frame.astype('int16') -
                              frame.astype('int16'))
                CH.append(diff)

        prev_frame = frame
        count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return CH


def work_per_second_with_threshold(video_path, thresh):
    cap = cv2.VideoCapture(video_path)

    prev_frame = None
    CH = []

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
                diff = np.abs(prev_frame.astype('int16') -
                              frame.astype('int16'))

                currSum = np.sum(diff)

                if currSum <= thresh:
                    CH.append(0)
                else:
                    CH.append(1)

        prev_frame = frame
        count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return CH


ch = work_per_second('/Users/pd/PycharmProjects/MA_Labs/mma-lab/Videos/video_07.mp4')
sum = []

for c in ch:
    sum.append(np.sum(c))

print(sum)

plt.figure(figsize=(5, 5))
plt.stem(sum)
plt.show()

ch = work_per_second_with_threshold('/Users/pd/PycharmProjects/MA_Labs/mma-lab/Videos/video_07.mp4', 327676)
print(ch)

plt.figure(figsize=(5, 5))
plt.stem(ch)
plt.show()

print("second video")
ch = work_per_second_with_threshold('/Users/pd/PycharmProjects/MA_Labs/mma-lab/Videos/TUDelft_Ambulance_Drone.mp4', 3276760)
print(ch)

plt.figure(figsize=(5, 5))
plt.stem(ch)
plt.show()