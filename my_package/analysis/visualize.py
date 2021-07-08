#Imports
import colorsys
import logging
import math
import numpy as np
from enum import Enum, unique
#import cv2
import matplotlib as mpl
import matplotlib.colors as mplc
import matplotlib.figure as mplfigure
from matplotlib import pyplot as plt
#import pycocotools.mask as mask_util
import torch
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import Image, ImageDraw, ImageFont

#from detectron2.data import MetadataCatalog
#from detectron2.structures import BitMasks, Boxes, BoxMode, Keypoints, PolygonMasks, RotatedBoxes
#from detectron2.utils.file_io import PathManager

#from .colormap import random_color

def plot_boxes(imgArray,pred_box,pred_class,outputs,z ):
    # Write the required arguments

     imgArray = imgArray.transpose(1,2,0)
     print(imgArray.shape)
     #print(imgArray*255)
     #imag = np.asarray(imgArray,dtype=np.uint8)
     #imag = Image.fromarray(imag.astype('uint8'))
     #img = img.squeeze(axis=2)
     #imagArray = imgArray-18
     #print(imgArray)
     #data[256, 256] = [255, 0, 0]
     imag = Image.fromarray(np.uint8(imgArray*255))# 'RGB')
     print(imag)
     lentuple =len(pred_box)
     i=0
     for (x1,y1),(x2,y2) in pred_box[:5-lentuple]:
         shape = [(x1,y1),(x2,y2)]
         img1 = ImageDraw.Draw(imag)
         img1.rectangle(shape,outline="red")
         img1.text((x1+10,y1-10), pred_class[i], fill=(255, 0, 0))
         i = i+1
     imag.save(outputs + "[" + str(z) + "]"+ "bbedited.jpg")
     return imag
     #imag.show()

  # The function should plot the predicted boxes on the images and save them.
  # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
