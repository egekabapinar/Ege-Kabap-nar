"""
Opencv ilk odev : Fotoğraf editleme uygulamasi H3
Uploading image
X Görsel boyutunu degistirmek (800,800)
X Image dondurmek (mouse sol tuşu ile sola sağ tuş ile sağa)
X Dikdörtgen çizdirmek ve dikdörtgenin içindeki görsel kırpıp kaydetme (öngörü saglanmali) (ctrl ve sol ile)
X Text yazdırmak ( Adinizi o pixeldeki rgb renginde yazacaksınız) alt ve sol
X Çember çizdirmek (öngörü saglanmali) ctrl ve sag
Görseldeki son degisiklikleri kaydetmek alt ve sag
"""

import cv2
import numpy as np

img = cv2.imread("odtu.jpg")
cv2.resize(img,(800,800))

def mouse_event(event, x,y,flags,param):
    global ilk_mouse
    global cizim
    global son_mouse
    global mouse1
    global circle
    global img
    if event == cv2.EVENT_LBUTTONDOWN and not(flags & cv2.EVENT_FLAG_CTRLKEY) and not(flags & cv2.EVENT_FLAG_ALTKEY):
        sag_90 = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow("saga 90 dondurme",sag_90)

    if event == cv2.EVENT_RBUTTONDOWN and not(flags & cv2.EVENT_FLAG_CTRLKEY) and not(flags & cv2.EVENT_FLAG_ALTKEY):
        sol_90 = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imshow("sola 90 dondurme",sol_90)

    if event == cv2.EVENT_LBUTTONDOWN and flags == cv2.EVENT_FLAG_ALTKEY + cv2.EVENT_FLAG_LBUTTON:
        b = int(img[y,x,0])
        g = int(img[y,x,1])
        r = int(img[y,x,2])
        cv2.putText(img,"Ege",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(b,g,r),2)
        cv2.imshow("image",img)

    if event == cv2.EVENT_LBUTTONDOWN and flags == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON:
        cizim = True
        ilk_mouse = (x,y)

    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_LBUTTON:
        if cizim == True:
            son_mouse = (x,y)
            a =img.copy()
            cv2.rectangle(a,ilk_mouse,son_mouse,(0,0,255),2)
            cv2.imshow("image",a)

    if event == cv2.EVENT_LBUTTONUP and flags == cv2.EVENT_FLAG_CTRLKEY:
        cizim = False
        kirp = img[min(son_mouse[1],ilk_mouse[1]):max(son_mouse[1],ilk_mouse[1]),
               min(ilk_mouse[0],son_mouse[0]):max(ilk_mouse[0],son_mouse[0])]
        cv2.imshow("kirpma",kirp)
        cv2.resizeWindow("kirpma",abs(ilk_mouse[0]-son_mouse[0]),abs(ilk_mouse[1]-son_mouse[1]))

    if event == cv2.EVENT_RBUTTONDOWN and flags == cv2.EVENT_RBUTTONDOWN + cv2.EVENT_FLAG_CTRLKEY:
        circle = True
        mouse1 = (x,y)
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_CTRLKEY + cv2.EVENT_FLAG_RBUTTON:
        if circle == True:
            mouse2 = (x,y)
            cv2.circle(img,mouse1,max(mouse2[1],mouse1[1]) - min(mouse2[1],mouse1[1]),(0,0,255),-1)
            cv2.imshow("image",img)

    if event == cv2.EVENT_RBUTTONDOWN and flags == cv2.EVENT_FLAG_ALTKEY + cv2.EVENT_FLAG_RBUTTON:
        cv2.imwrite("saved_img.jpg",img)

    if event == 10 and flags>0:

        img = cv2.resize(img,None,fx=1.1,fy=1.1, interpolation=cv2.INTER_CUBIC)
        cv2.imshow("image",img)
    elif event == 10 and flags <= 0:
        img = cv2.resize(img, None, fx=0.9, fy=0.9, interpolation=cv2.INTER_AREA)
        cv2.imshow("image", img)


cv2.imshow("image",img)
cv2.setMouseCallback("image",mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
