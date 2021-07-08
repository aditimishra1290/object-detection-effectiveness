#Imports
from PIL import ImageFilter
from scipy.ndimage.filters import gaussian_filter

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius=5):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius = radius

        # Write your code here


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)
            Returns:
            image (numpy array or PIL Image)
        '''
        return image.filter(ImageFilter.GaussianBlur(radius=self.radius))

        # Write your code here
