"""Uploading image
Görsel boyutunu degistirmek (800,800)ok
Image dondurmek (mouse sol tuşu ile sola sağ tuş ile sağa) ok
Dikdörtgen çizdirmek ve dikdörtgenin içindeki görsel kırpıp kaydetme (öngörü saglanmali) (ctrl ve sol ile) ok
Text yazdırmak ( Adinizi o pixeldeki rgb renginde yazacaksınız) alt ve sol ok
Çember çizdirmek (öngörü saglanmali) ctrl ve sag ok
Görseldeki son degisiklikleri kaydetmek alt ve sag """
import cv2
top_left_corner=[]
bottom_right_corner=[]
drawing=False
circle = False
firstx=0
firsty=0
lastx=0
lasty=0
a=[]
b=[]
def copyimg(img):
    img1=img.copy
    return img1
def click_event(event,x,y,flags,param):
    global top_left_corner
    global bottom_right_corner
    global drawing,circle
    global firstx
    global firsty
    global lastx
    global lasty
    global a,b
    global my_radius
    if event == cv2.EVENT_LBUTTONDOWN and not(flags & cv2.EVENT_FLAG_CTRLKEY) and not(flags & cv2.EVENT_FLAG_ALTKEY):
        rotated_left = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow('rotated_left', rotated_left)
    if event == cv2.EVENT_RBUTTONDOWN and not(flags & cv2.EVENT_FLAG_CTRLKEY) and not(flags & cv2.EVENT_FLAG_ALTKEY):
        rotated_right = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('rotated_right', rotated_right)
    if event == cv2.EVENT_LBUTTONDOWN and flags == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON:
        drawing = True

        top_left_corner = [(x, y)]

    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            bottom_right_corner = [(x, y)]
            a = img.copy()

            cv2.rectangle(a, top_left_corner[0], bottom_right_corner[0], (0, 255, 0), 2, 8)

            cv2.imshow("image", a)

    if event == cv2.EVENT_LBUTTONUP and flags == cv2.EVENT_FLAG_CTRLKEY :
        drawing = False

        bottom_right_corner = [(x, y)]

        cv2.rectangle(a, top_left_corner[0], bottom_right_corner[0], (0, 255, 0), 2, 8)
        cv2.imshow("image", img)

        cropped = imgcopy[min(top_left_corner[0][1],bottom_right_corner[0][1]):max(bottom_right_corner[0][1],top_left_corner[0][1]),
                  min(top_left_corner[0][0],bottom_right_corner[0][0]):max(bottom_right_corner[0][0],top_left_corner[0][0])]
        cv2.imshow('cropped', cropped)
    if event == cv2.EVENT_LBUTTONDOWN and     flags == cv2.EVENT_FLAG_ALTKEY + cv2.EVENT_FLAG_LBUTTON:
        blue = int(img[y, x, 0])
        green = int(img[y, x, 1])
        red= int(img[y, x, 2])
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, "Dilara", (x, y), font, 0.5, (blue,green,red), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN and flags == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_RBUTTON:
        circle = True
        firstx = x
        firsty = y
    elif     event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_RBUTTON:
        if circle == True:
            lastx=x
            lasty=y
            my_radius = int(((lastx - firstx) ** 2 + (lasty - firsty) ** 2) ** (1 / 2))
            b= img.copy()
            cv2.circle(b, (firstx,firsty), my_radius, (255, 0, 0), -1)
            cv2.imshow("image", b)

    if event == cv2.EVENT_RBUTTONUP and flags == cv2.EVENT_FLAG_CTRLKEY :
        circle = False
        lastx = x
        lasty = y
        cv2.circle(img, (firstx, firsty), my_radius, (255, 0, 0), -1)

        cv2.imshow("image", img)

    if event == cv2.EVENT_RBUTTONDOWN and     flags == cv2.EVENT_FLAG_ALTKEY + cv2.EVENT_FLAG_RBUTTON:
        cv2.imwrite("savedodtu.jpg", img)

img = cv2.imread('odtu.jpg')
img = cv2.resize(img, (800, 800))
cv2.imshow('image', img)
imgcopy=img.copy()

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

