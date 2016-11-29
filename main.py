import cv2
import numpy as np

img = cv2.imread("test.png")
cap = cv2.VideoCapture('Lava.mp4')

cv2.namedWindow('Image Colour', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('Original Image', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('Colour Chart', cv2.WINDOW_KEEPRATIO)
cs = []
# print(cs[0])

# Output Init.
height = 4000
width = 3000
chart = np.zeros((height, width, 3), np.uint8)


# video processing
i = 0
while(cap.isOpened()):

    frameRead, img = cap.read()
    frameNum = int(i % 30)
    if frameRead and frameNum == 0:
        z = img.reshape((-1, 3))
        z = np.float32(z)

        crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        k = 1
        ret, label, center = cv2.kmeans(z, k, None, crit, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Now convert back into uint8, and make original image
        center = np.uint8(center)
        res = center[label.flatten()]

        res2 = res.reshape((img.shape))
        cs.append(res2[10, 10])

        cv2.imshow('Image Colour', res2)

        lineHeight = int(height / len(cs))
        currPos = 0
        chart = np.zeros((height, width, 3), np.uint8)
        for c in cs:
            chart[currPos:(currPos + lineHeight), :] = (c[0], c[1], c[2])
            currPos += lineHeight

        cv2.imshow("Colour Chart", chart)

    elif not frameRead:
        break


    cv2.imshow('Original Image', img)

    i += 1
    cv2.waitKey(1)

cap.release()


lineHeight = int(height / len(cs))
currPos = 0
chart = np.zeros((height, width, 3), np.uint8)

print(len(cs))

for c in cs:
    chart[currPos:(currPos + lineHeight), :] = (c[0], c[1], c[2])
    currPos += lineHeight

while(1):
    cv2.imshow("Colour Chart", chart)
    cv2.waitKey(5)

