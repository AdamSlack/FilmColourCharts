import cv2
import numpy as np
import os

def create_fp_string(folder_id, file_name):
    return 'film/' + folder_id + '/video/' + file_name

def create_path_string(folder_id, folder):
    return 'film/' + folder_id + '/'+ folder +'/'

def get_file_name(folder_id):
    dir_path = create_path_string(folder_id, 'video')
    available_files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return available_files[0]


folder_id = '00002' # id will come from cmd line arg.

file_name = get_file_name(folder_id)
dir_path = create_path_string(folder_id, 'video')
output_path = create_path_string(folder_id, 'colour_chart')
frame_path = create_path_string(folder_id, 'images')
file_path = create_fp_string(folder_id, file_name)

cap = cv2.VideoCapture(file_path)
cs = []
# print(cs[0])

# Output Init.
height = 16000
width = 12000
chart = np.zeros((height, width, 3), np.uint8)

# vieo processing
i = 0
n = 0
while cap.isOpened():

    frameRead, img = cap.read()
    frameNum = int(i % 75)
    if frameRead and frameNum == 0:
        print(i)
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

        lineHeight = int(height / len(cs))
        currPos = 0
        chart = np.zeros((height, width, 3), np.uint8)
        for c in cs:
            chart[currPos:(currPos + lineHeight), :] = (c[0], c[1], c[2])
            currPos += lineHeight

        cv2.imwrite(frame_path + file_name + str(n) + '.png', img)
        n += 1
    elif not frameRead:
        break
    i += 1

cap.release()


lineHeight = int(height / len(cs))
currPos = 0
chart = np.zeros((height, width, 3), np.uint8)

print(len(cs))

for c in cs:
    chart[currPos:(currPos + lineHeight), :] = (c[0], c[1], c[2])
    currPos += lineHeight

cv2.imwrite(output_path + file_name + 'Chart.png', chart, )
