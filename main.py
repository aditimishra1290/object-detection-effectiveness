#Imports
import json
from my_package.model import ObjectDetectionModel
from my_package.data.dataset import Dataset
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from my_package.analysis.visualize import plot_boxes
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.crop import CropImage
from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.rescale import RescaleImage
from my_package.data.transforms.rotate import RotateImage
def experiment(annotation_file, detector, transforms, outputs):
    '''
        Function to perform the desired experiments
        Arguments:
        annotation_file: Path to annotation file
        detector: The object detector
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''

    #Create the instance of the dataset.
    rrr = Dataset(annotation_file, transforms)
    #z = dict{}
    for i in range(10):
        img, gt_bboxes = rrr.__getitem__(i)
        pred_boxes, pred_class, pred_score = detector(img)
        f = plot_boxes(img, pred_boxes, pred_class, outputs, i)
    #img, gt_bboxes = rrr.__getitem__(4)
    #pred_boxes, pred_class, pred_score = detector(img)
    #plot_boxes(img, pred_boxes, pred_class, outputs, 4)
    #print(img.shape)
    img, gt_bboxes = rrr.__getitem__(5)
    #Iterate over all data items.
    #for x in dat:
    #img = item["image"].transpose(1,2,0)
    pred_boxes, pred_class, pred_score = detector(img)
    f = plot_boxes(img, pred_boxes, pred_class, outputs, "ORIGINAL")
    zzz = Dataset(annotation_file, [FlipImage("horizontal")])
    img, gt_bboxes = zzz.__getitem__(5)
    pred_boxes, pred_class, pred_score = detector(img)
    f = plot_boxes(img, pred_boxes, pred_class, outputs, "FLIPPED")
    zzz = Dataset(annotation_file, [BlurImage(7)])
    img, gt_bboxes = zzz.__getitem__(5)
    pred_boxes, pred_class, pred_score = detector(img)
    f = plot_boxes(img, pred_boxes, pred_class, outputs, "BLURRED")
    zzz = Dataset(annotation_file, [RescaleImage((1576, 1042))])
    img, gt_bboxes = zzz.__getitem__(5)
    pred_boxes, pred_class, pred_score = detector(img)
    f = plot_boxes(img, pred_boxes, pred_class, outputs, "RESCALED2X")
    zzz = Dataset(annotation_file, [RescaleImage((394, 260))])
    img, gt_bboxes = zzz.__getitem__(5)
    pred_boxes, pred_class, pred_score = detector(img)
    f = plot_boxes(img, pred_boxes, pred_class, outputs, "RESCALED0.5X")
    zzz = Dataset(annotation_file, [RotateImage(270)])
    img, gt_bboxes = zzz.__getitem__(5)
    pred_boxes, pred_class, pred_score = detector(img)
    f = plot_boxes(img, pred_boxes, pred_class, outputs, "ROTATED90")
    zzz = Dataset(annotation_file, [RotateImage(45)])
    img, gt_bboxes = zzz.__getitem__(5)
    pred_boxes, pred_class, pred_score = detector(img)
    f = plot_boxes(img, pred_boxes, pred_class, outputs, "ROTATED45")
    #img = img.transpose(2,0,1).reshape(3,-1)
    #plt.subplot(1,2,1)
    #plt.plot(img)

    #Get the predictions from the detector.


    #Draw the boxes on the image and save them.


    #Do the required analysis experiments.



def main():
    detector = ObjectDetectionModel()
    experiment("python_se_assignment\\annotations.json", detector, [], "python_se_assignment\\op\\") # Sample arguments to call experiment()



if __name__ == '__main__':
    main()
