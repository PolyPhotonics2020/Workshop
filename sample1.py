# -*- coding: utf-8 -*-
"""Sample1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hFqvokVy5ZBHvY_VK_-PZVXYgpbqbESm

```
Download image
```
"""

!git clone https://github.com/PolyPhotonics2020/Workshop.git

import imutils
import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread('Workshop/tetris_blocks.png')
print("Image color")
cv2_imshow(image)
# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Image gray")
cv2_imshow(gray)

edged = cv2.Canny(gray, 30, 150)
print("Image edged")
cv2_imshow(edged)

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
print("Image thresh")
cv2_imshow(thresh)

# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()
# loop over the contours
print("Contours")
for c in cnts:
	# draw each contour on the output image with a 3px thick red
	# outline, then display the output contours one at a time
	cv2.drawContours(output, [c], -1, (0, 0, 255), 3)
text = "Found {} objects!".format(len(cnts))
print(text)
cv2_imshow(output)