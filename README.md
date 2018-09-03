# ALPR-Indonesian-plate
This code is for automatic license plate recognition in indonesian plate, which have black background and white number

for use in linux just
*Change file Destination of the writing image
*Main.py capture and save for waktu_kedatangan in sql
*Main2.py capture and save for waktu_kepergian in sql

Python Main.py -c directoryFileImage = calibrating the camera and threshold

Python Main.py  = use with cam

Python Main.py -i directoryFileImage = recognition an image

Python Main.py -v directoryFileVideo = recognition a video

# For using Database
1. Import alpr.sql with mysql engine

# To train the model 
1. Go to Training_Data
2. Replace testplat.tif or change code in GenData.py that open the image
3. Run GetData.py and click based on alpha or number that come.
4. Do it until complete.
