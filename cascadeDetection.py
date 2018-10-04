import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('./DataSources/Haarcascade/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('./DataSources/Haarcascade/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

img_counter = 0


def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)


make_480p()

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # depending on the size the image we use we can change the parameters

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:int((y+h)*0.7), x:x+w]
        roi_color = img[y:int((y+h)*0.7), x:x+w]

        # considering eyes are always upper top face ^^

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, img)
        print("{} written!".format(img_name))
        img_counter += 1

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()
