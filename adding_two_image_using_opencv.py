# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:53:28 2021

@author: aman
"""
import cv2

img = cv2.imread('C:\\Users\\g1ama\\Desktop\\messi.webp')
img2 = cv2.imread('C:\\Users\\g1ama\\Desktop\\429.jpeg')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))



img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

#dst = cv2.add(img,img2);
dst = cv2.addWeighted(img,.5, img2,.5,0);  #For Wighted Image
cv2.imshow('image',dst)


cv2.waitKey(0)
cv2.destroyAllWindows()

