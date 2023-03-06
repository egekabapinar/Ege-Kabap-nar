import cv2
import numpy as np

cap = cv2.VideoCapture('reddetection.mp4')

lower_red = np.array([95, 95, 35])
upper_red = np.array([10, 255, 255])
lower_red2 = np.array([105, 105, 45])
upper_red2 = np.array([180, 255, 255])

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = cv2.bitwise_or(mask1, mask2)

        res = cv2.bitwise_and(frame, frame, mask=mask)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            if radius > 2:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)

                uzaklik = (round(abs(320-x)),round(abs(176-y)))


                cv2.putText(frame,f"uzaklik:{uzaklik}",(5,30),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),3)

        cv2.line(frame, (int(x), int(y)), (320, 176), (255, 0, 0), 2)
        cv2.imshow('frame', frame)
        cv2.imshow("mask",res)
        cv2.resizeWindow("frame", 640, 352)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break


    else:
        break


cap.release()
cv2.destroyAllWindows()
