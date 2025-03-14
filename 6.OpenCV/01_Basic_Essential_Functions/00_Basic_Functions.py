""" 5 Essential Basic Functions in OpenCV """

# Import opencv library in google colab
from google.colab.patches import cv2_imshow      #since I am using google colaboratory 
import cv2 as cv

# Load image
img = cv.imread("../../assets/Photos/park.jpg")
cv2_imshow("Park", img)

# 1. Converting the RGB image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv2_imshow("Grayscaled_park", gray)

# 2. Blur (Gaussian Blur)
# Reduces noise and smooth out details in the image
blur = cv.GaussianBlur(img, 
                       (3, 3),          # kernel_size needs to be odd number
                       cv.BORDER_DEFAULT)
cv2_imshow("Blurred_park", blur)

# 3. Edge Detection using Canny edge detector
# NOTE:
# The first threshold is the minimum gradient intensity for a pixel to be considered an edge.
# Pixels with gradients below this value are ignored.

# The second threshold is the maximum gradient intensity to be instantly accepted as an edge.
# Pixels with gradients above this value are immediately considered edges.
canny = cv.Canny(img, 125, 175)         # Applying Canny edge detection on the original image
blur_canny = cv.Canny(blur, 125, 175)   # Applying Canny edge detection on the blurred image
cv2_imshow("Canny_park", canny)
cv2_imshow("Canny_blur_park", blur_canny)

# 4. Dilating the edges to make them more prominent
dilated = cv.dilate(canny, (5,5), iterations=1)  # Dilating the edges with a 5x5 kernel, 1 iteration
cv2_imshow("Dilated_park", dilated)

# 5. Eroding the image to reduce noise and refine edges
erode = cv.erode(dilated, (5,5), iterations=3)  # Eroding the dilated image with a 5x5 kernel, 3 iterations
cv2_imshow("Eroded_park", erode)

cv.waitKey(0)
