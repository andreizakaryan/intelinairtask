from cv2 import cv2
import numpy as np
import argparse

MAX_VAL = 256

parser = argparse.ArgumentParser()
parser.add_argument('--red', help='red channel', default='red.tif')
parser.add_argument('--green', help='green channel', default='green.tif')
parser.add_argument('--blue', help='blue channel', default='blue.tif')
parser.add_argument('--output', help='output file path', default='res.png')
args = parser.parse_args()

blue = cv2.imread(args.blue, -1)
green = cv2.imread(args.green, -1)
red = cv2.imread(args.red, -1)

img = np.dstack((blue, green, red))
img = img / MAX_VAL

# histogram equalization
img_hsv = cv2.cvtColor(img.astype('uint8'), cv2.COLOR_BGR2HSV)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img_hsv[:, :, 2] = clahe.apply(img_hsv[:, :, 2])

img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

# brightness correction
gamma = 0.6

lookUpTable = np.empty((MAX_VAL), np.uint8)
for i in range(MAX_VAL):
        lookUpTable[i] = np.clip(
            pow(i / (MAX_VAL - 1), gamma) * (MAX_VAL - 1), 0, MAX_VAL - 1)

img = lookUpTable[img]

cv2.imwrite(args.output, img)
