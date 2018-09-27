# Genauto.py

import sys
from skimage.io import imread
import numpy as np
import cv2
import os


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
            img_details = imread(training_dataset_dir+'/'+each_letter+'/'+each_letter+'_'+str(each)+'.png', as_grey=True)
            imgROIResized = cv2.resize(img_details, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))

            print("%s %s" %(each_letter,each))

            intLetter= ord(each_letter)
            intClassifications.append(intLetter)
            npaFlattenedImage = imgROIResized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))  # flatten image to 1d numpy array so we can write to file later
            npaFlattenedImages = np.append(npaFlattenedImages, npaFlattenedImage, 0)

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
