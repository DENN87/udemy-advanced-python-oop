import numpy as np
from PIL import Image


class Canvas:
    """Object where all shapes are being drawn"""

    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make_image(self, image_path):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
