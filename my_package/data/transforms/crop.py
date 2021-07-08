#Imports
import numpy
import random
from PIL import Image

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
        image = Image.open('demo_image.jpg')
box = (200, 300, 700, 600)
cropped_image = image.crop(box)
cropped_image.save('cropped_image.jpg')

# Print size of cropped image
print(cropped_image.size) # Output: (500, 300)
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        img = self
        #self.old_shape = img.size
        self.new_shape = shape
        self.crop_type = crop_type

        # Write your code here

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        print(image.size)
        old_shape = image.size
        if self.crop_type == 'center':
            return image.crop(((old_shape[0] /2) -(self.new_shape[0] /2) , (old_shape[1] /2) -(self.new_shape[1] /2) , (old_shape[0] /2) +(self.new_shape[0] /2), (old_shape[1] /2) +(self.new_shape[1] /2)))
        else:
            y = int((old_shape[0] - self.new_shape[0]) * random.random())
            x = int((old_shape[1] - self.new_shape[1]) * random.random())
            return image.crop((y, x,  y + self.new_shape[0], x + self.new_shape[1]))


        # Write your code here
