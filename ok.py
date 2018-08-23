
import imutils
import argparse
import cv2
import numpy as np
import Preprocess as pp
import os
import time
import math
import Calibration as cal
import collections
import DetectChars
import DetectPlates
import PossiblePlate

nums = "DEKASI"
plateDic = {'B':'Jakarta', 'D':'Bandung', 'L':'Surabaya'}
for i, j in plateDic.items():
    if (nums[0] == i):
        plateRegion = j

                
