import cv2
import numpy as np

class ColourProcessor:

    def __init__(self, height, width, freq, fileName, extension):
        """ Class constructor """
        self.cap = cv2.VideoCapture()
        self.chart = np.zeros((height, width, 3), np.uint8)
        self.height = height
        self.width = width
        self.freq = freq
        self.colours = []
        self.fileName = fileName
        self.extension = extension

    def openCap(self):
        """ Create a Video Capture object """
        self.cap = cv2.VideoCapture(self.fileName + self.extension)

    def readFrame(self):
        """ Read a frame from the capture device """
        return self.cap.read()

    def saveFrame(self, frame, fileName, frameID):
        """ Save the frame as an image in desired location """
        cv2.imwrite(fileName + '/' + fileName + str(frameID) + '.png', frame)

    def processFrame(self, frame):
        """ Get the colour from the given Frame"""

        # format the image for k-means
        mat = frame.reshape((-1, 3))
        mat = np.float32(mat)

        # Define k-means criteria
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        k = 1

        # carry out k-means
        comp, label, center = cv2.kmeans(mat, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # get the original image back (Just the colour really)
        center = np.uint8(center)
        result = center[label.flatten()]

        final = result.reshape((frame.shape))
        self.colours.append(final[10, 10])

        return final, final[10, 10]



