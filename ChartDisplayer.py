import cv2
import os, os.path

class ChartDisplayer:

    def __init__(self, dirName):
        """ Constructor """
        self.dir = dirName
        self.frameCount = self.getFrameCount()
        self.height = 4000
        self.width = 3000
        self.lineHeight = self.height // self.frameCount
        self.chart = self.getColourChart()
        self.currentFrame = cv2.imread(self.dir + '/' + self.dir +'0.png')

    def getColourChart(self):
        """ Opens the colour chart file present in the specified dir """
        return cv2.imread(self.dir + '/' + self.dir + 'Chart.png')

    def getFrameCount(self):
        """ Counts the number of Key Frame files in the dir """
        return len([f for f in os.listdir(os.getcwd() + '\\' + self.dir)]) - 1

    def updateScene(self, x, y):
        """ Updates the window containing the KeyFrames"""
        imgNum = y // self.lineHeight
        path = self.dir + '/' + self.dir + str(imgNum) + '.png'
        self.currentFrame = cv2.imread(path)

    def getMousePos(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            self.updateScene(x, y)

    def displayImages(self):
        """ Displays the colour chart and the current scene frame """
        cv2.namedWindow(self.dir + ' Colour Chart', cv2.WINDOW_KEEPRATIO)
        cv2.imshow(self.dir + ' Colour Chart', self.chart)

        cv2.namedWindow(self.dir + ' Key Frame', cv2.WINDOW_KEEPRATIO)
        cv2.imshow(self.dir + ' Key Frame', self.currentFrame)

        cv2.setMouseCallback(self.dir + " Colour Chart", self.getMousePos)

        cv2.waitKey(1)
