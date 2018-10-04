import numpy as np
import cv2
from Treshold import *

face_cascade = cv2.CascadeClassifier('./DataSources/Haarcascade/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

treshold = Treshold(120, 2, 2)

img_counter = 0


def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)


make_480p()

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)

    # depending on the size the image we use we can change the parameters

    for(x, y, w, h) in faces:

        # my face is showing up in this frame
        # if i print x, y, w and h i will see the values changes as far as i am reconized by camera

        # roi means for region of interest wich is my face.

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        color = (255, 0, 0)
        stroke = 2
        width = x+w
        height = y+h

        if width > treshold.min_width & width < treshold.max_width & height > treshold.height:
            print('my condition is satisfied')

            # and the idea is to play with thoes treshold values, to pick same types of face images.

            cv2.rectangle(img, (x, y), (width, height), color, stroke)

        print(width, height)

    cv2.imshow('img', img)
    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, roi_color)
        print("{} written!".format(img_name))
        img_counter += 1

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()
