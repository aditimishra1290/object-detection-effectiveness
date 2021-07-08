# object-detection-effectiveness
Object detection is a very well studied task of Deep Learning, having tremendous variety of applications. This is a python package for transforming images and analysing their effect on the predictions of an object detector.

A python package means that one can install the package in the python environment and can import the modules in any python script, irrespective of the location of the script. 

The details of each of the files/folders are as follows:

main.py: This is the main file which is to be called to execute the program. The main file calls the corresponding functions as needed while execution. The main file calls the appropriate function to prepare the dataset, then transform the images read, obtain the bounding boxes of the objects present in the image by calling the detector model, and then plot the obtained images by calling the appropriate functions from the package described below.

./pkg/model.py: This file contains the object-detection model definition. Consider it as a black-box model which takes an image (as numpy array) as input and provides the bounding box outputs.
 
./pkg/data/dataset.py: This file contains the class Dataset that reads the provided dataset from the annotation file and provides the numpy version of the images which are to be transformed and forwarded through the model. The annotation format is provided in data/README.md

./pkg/data/transforms: This folder contains 5 files. Each of these files is responsible for performing the corresponding transformation, as follows:

a) crop.py: This file takes an image (as numpy array) as input and crops it based on the provided arguments. Uses a class CropImage() for performing the operation.

b) flip.py: This file takes an image (as numpy array) as input and flips it based on the provided arguments. Uses a class FlipImage() for performing the operation.
 
c) rotate.py: This file takes an image (as numpy array) as input and rotates it based on the provided arguments. Uses a class RotateImage() for performing the operation.
 
d) rescale.py: This file takes an image (as numpy array) as input and rescales it based on the provided arguments. Uses a class RotateImage() for performing the operation.

e) blur.py: This file takes an image (as numpy array) as input and applies a gaussian blur to it based on the provided arguments. Uses a class GaussBlurImage() for performing the operation.

./pkg/analysis/visualize.py: This file defines a function that draws the image with the predicted bounding boxes (with the corresponding labels) on the image and saves them in the specified output folder.


Note: For handling images, e.g. reading images, etc. we have used PIL instead of OpenCV as OpenCV uses BGR format instead of RGB.

The various transformations in ./pkg/data/transforms. There are five files, as already mentioned. 

Then there is the Dataset class in ./pkg/data/dataset.py. This class will accept the path to the annotation file and the list of transformation classes. 

./pkg/analysis/visualize.py draws the image with the predicted bounding boxes (with the corresponding labels) on the images and saves them in the output folder. For simplicity, we have plotted only the 5 most confident bounding boxes predicted by the object detector. If the detector predicts less than 5 boxes, then it plots all of them.

Created a python package pkg.
