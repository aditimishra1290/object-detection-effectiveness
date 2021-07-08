#Imports
import numpy

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip_type = flip_type

        # Write your code here


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        if self.flip_type == 'horizontal':
            return numpy.flip(image, 0)
        else:
            return numpy.flip(image, 1)

        # Write your code here
