# Genauto.py

import sys
from skimage.io import imread
import numpy as np
import cv2
import os
import time


# module level variables ##########################################################################
MIN_CONTOUR_AREA = 100

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30

###################################################################################################
def main():
    current_dir=os.getcwd()
    training_dataset_dir = os.path.join(current_dir, 'dataset')

    letters = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

    npaFlattenedImages =  np.empty((0, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))

    intClassifications = []
    for each_letter in letters:
        x=0
        path = os.path.join(training_dataset_dir, each_letter)
        for files in os.listdir(path):
            if files.endswith('.png'):
                x+=1
        for each in range(x):
            #training_data[1] is for 10X20 training data images
            img_details = cv2.imread(training_dataset_dir+'/'+each_letter+'/'+each_letter+'_'+str(each)+'.png')
            imgROIResized = cv2.resize(img_details, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))
            imgGray = cv2.cvtColor(imgROIResized, cv2.COLOR_BGR2GRAY)          # get grayscale image
            imgBlurred = cv2.GaussianBlur(imgGray, (5,5), 0)                        # blur

                                                                # filter image from grayscale to black and white
            imgThresh = cv2.adaptiveThreshold(imgBlurred,                           # input image
                                              255,                                  # make pixels that pass the threshold full white
                                              cv2.ADAPTIVE_THRESH_GAUSSIAN_C,       # use gaussian rather than mean, seems to give better results
                                              cv2.THRESH_BINARY_INV,                # invert so foreground will be white, background will be black
                                              11,                                   # size of a pixel neighborhood used to calculate threshold value
                                              2)                                    # constant subtracted from the mean or weighted mean


            #cv2.imwrite('2_%s.png' %each,imgThresh)
            #cv2.imwrite('1_%s.png' %each,img_details)
            #cv2.imshow("imgROIResized", imgROIResized)

            print("%s %s" %(each_letter,each))

            intLetter= ord(each_letter)
            intClassifications.append(intLetter)
            npaFlattenedImage = imgThresh.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))  # flatten image to 1d numpy array so we can write to file later
            npaFlattenedImages = np.append(npaFlattenedImages, npaFlattenedImage, 0)
            time.sleep(1)

    fltClassifications = np.array(intClassifications, np.float32)                   # convert classifications list of ints to numpy array of floats

    npaClassifications = fltClassifications.reshape((fltClassifications.size, 1))   # flatten numpy array of floats to 1d so we can write to file later

    print ("\n\ntraining complete !!\n")

    np.savetxt("classifications.txt", npaClassifications)           # write flattened images to file
    np.savetxt("flattened_images.txt", npaFlattenedImages)          #

    cv2.destroyAllWindows()             # remove windows from memory

    return

###################################################################################################
if __name__ == "__main__":
    main()
# end if
