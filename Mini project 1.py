#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def liveSketch():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow("Live Sketch", sketch(frame))
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


# In[3]:


def sketch(image):
    # Convert image to gray scale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image using Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Extract Edges
    canny_edges = cv2.Canny(img_gray_blur, 30, 70)

    # Do an invert binarize the image
    ret, mask = cv2.threshold(canny_edges, 120, 255, cv2.THRESH_BINARY_INV)

    return mask


# In[4]:


liveSketch()

