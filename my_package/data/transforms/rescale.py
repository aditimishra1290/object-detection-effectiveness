#Imports
from PIL import Image
class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output = output_size

        # Write your code here

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        # Write your code here
        shape = self.output
        if isinstance(self.output, int):
            shape = image.size
            if shape[0] < shape[1]:
                ratio = self.output / shape[0]
                shape[1] = shape[1] * ratio
            else:
                ratio = self.output / shape[1]
                shape[0] = shape[0] * ratio
        return image.resize(shape, Image.ANTIALIAS)
