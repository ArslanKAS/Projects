
# import the necessary packages
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import imutils
import time
import dlib
import cv2
import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate

root = tk.Tk()
root.withdraw()
click = 'YES'


def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear

# for asking user to open Shape-file
shape_predictor = filedialog.askopenfilename()

# for asking user to open video-file
video = filedialog.askopenfilename()

# Three modes for blinking
USER_INPUT = input("Please select a mode: \n 1 = Fast Mode , 2 = Medium Mode, 3 = Slow Mode:\n ")


EYE_AR_THRESH = 0.3
COUNTER = 0
TOTAL = 0
D_TOTAL = 0
T_TOTAL = 0
SPEED_BLINK_COUNTER = 0
S_blink = []
blinks = 0
S_blink_show = 0
D_blink_show = 0
T_blink_show = 0
D_blinks = 0
D_blink = []
T_blink = []
T_blinks = 0

# initialize dlib's face detector (HOG-based) and then create
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()

# the facial landmark predictor
predictor = dlib.shape_predictor(shape_predictor)

# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# start the video stream thread
print("[INFO] starting video stream thread...")
vs = FileVideoStream(video).start()


# If wanna use the Webcam then uncomment the following lines and comment the others.
# vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
fileStream = True
time.sleep(1.0)

# loop over frames from the video stream
while True:

    # Grab the frames from the video
    frame = vs.read()
    # if the frames are over then program will break and end.
    if np.shape(frame) == ():
        break

    # Resize the frames to our needs
    frame = imutils.resize(frame, width=450)

    # Convert the frames into grayscale since image processing will be performed on it.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    rects = detector(gray, 0)

    # loop over the face detections
    for rect in rects:
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # extract the left and right eye coordinates, then use the
        # coordinates to compute the eye aspect ratio for both eyes
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # average the eye aspect ratio together for both eyes
        ear = (leftEAR + rightEAR) / 2.0

        # compute the convex hull for the left and right eye, then
        # visualize each of the eyes
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # check to see if the eye aspect ratio is below the blink
        # threshold, and if so, increment the blink frame counter
        # Jb tk Ankh bnd hy to ye Counter increase hta jay ga kuink for loop lga hy
        if ear < EYE_AR_THRESH:
            COUNTER += 1
            blinks = 1
            D_blinks = 0
            T_blinks = 0
        # otherwise, the eye aspect ratio is not below the blink
        # threshold
        # Jese e Ankh khulay gi aur counter 3 frames ya is sy zyada hjay ga to Total mai increment ajaye ga
        else:
            # if the eyes were closed for a sufficient number of
            # then increment the total number of blinks
            if COUNTER >= 2:
                TOTAL += 1
                S_blink.append(TOTAL)
                S_blink_show = sum(S_blink)
                if S_blink_show % 2 == 0 and blinks == 1:
                    D_TOTAL += 1
                    D_blink.append(D_TOTAL)
                    D_blink_show = sum(D_blink)
                    D_blinks = 1
                if S_blink_show % 3 == 0 and blinks == 1:
                    T_TOTAL += 1
                    T_blink.append(T_TOTAL)
                    T_blink_show = sum(T_blink)
                    T_blinks = 1

            # reset the eye frame counter
            COUNTER = 0
            S_blink = []
            D_TOTAL = 0
            T_TOTAL = 0
            blinks = 0

        # draw the total number of blinks on the frame along with
        # the computed eye aspect ratio for the frame
        MODE_text = "Blink Mode"
        MODE1_text = "Fast Mode"
        MODE2_text = "Medium Mode"
        MODE3_text = "Slow Mode"

        if USER_INPUT == "1":
            SPEED_BLINK_COUNTER = S_blink_show
            MODE_text = MODE1_text
            if blinks == 1:
                click = "YES"
            else:
                click = ""

        if USER_INPUT == "2":
            SPEED_BLINK_COUNTER = D_blink_show
            MODE_text = MODE2_text
            if D_blinks == 1:
                click = "YES"
            else:
                click = ""

        if USER_INPUT == "3":
            SPEED_BLINK_COUNTER = T_blink_show
            MODE_text = MODE3_text
            if T_blinks == 1:
                click = "YES"
            else:
                click = ""

        cv2.putText(frame, "Blinks: {}".format(SPEED_BLINK_COUNTER), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.rectangle(frame, (0, 250), (450, 350), (104, 104, 104), thickness=-1, lineType=8, shift=0)
        cv2.putText(frame, "User Clicked: {}".format(click), (220, 270),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(frame, MODE_text, (10, 270),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # show the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(2) & 0xFF
    if key == ord("q"):
        break
print(tabulate([[video, S_blink_show, D_blink_show, T_blink_show]],
               headers=['Video Name', 'Fast Blinks', 'Medium Blinks', 'Slow Blinks']))

vs.stop()

input("Press Enter to Exit the Program")