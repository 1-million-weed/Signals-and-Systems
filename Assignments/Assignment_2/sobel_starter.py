"""
Authors: Matthijs Prinsen and Marinus v/d Ende
Date: 19/12/2024
Description:
    This script performs Sobel edge detection 
    on a grayscale image.
    The class is a subclass of the ThemisInterface class.
"""

import numpy as np
from PIL import Image

# Define a class to represent a grayscale image
class GrayImage:
    """Class to represent a grayscale image."""	
    def __init__(self, width, height):
        """Initialize the grayscale image."""
        self.width = width
        self.height = height
        self.data = np.zeros((height, width), dtype=int)

# Function to read a PGM image file and convert it to grayscale
def readPGM(filename: str) -> GrayImage:
    """Read a PGM image file and convert it to grayscale."""
    image = Image.open(filename)
    image = image.convert('L')  # convert image to grayscale
    width, height = image.size
    img = GrayImage(width, height)
    img.data = np.array(image)
    return img

# Function to write a grayscale image to a PGM file
def writePGM(filename: str, image: GrayImage):
    img = Image.fromarray(image.data.astype(np.uint8))
    img.save(filename)

def convolveImage(operandOne: np.ndarray, operandTwo: np.ndarray) -> int:
    """Perform convolution between two matrices and return the squared dot product."""
    dot_product = (operandOne * operandTwo).sum()
    return dot_product**2

def performSobelEdgeDetection(image: GrayImage) -> GrayImage:
    """Perform Sobel edge detection on a grayscale image."""
    # our kernels
    Hx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    Hy = np.array([[-1, -2, -1],
                   [ 0,  0,  0],
                   [ 1,  2,  1]])
    
    height, width = image.data.shape
    # Initialize the new image
    new_image = np.zeros((height-2, width-2), dtype=int)
    # Iterate over the gray scale image (ignoring the borders)
    for x in range(1, image.height-1):
        for y in range(1, image.width-1):
            # Get the sub matrix
            sub_matrix = image.data[x-1:x+2, y-1:y+2]
            # Convolve the sub matrix with the kernels
            Gx = convolveImage(sub_matrix, Hx)
            Gy = convolveImage(sub_matrix, Hy)
            # Set the new pixel value
            new_image[x-1, y-1] = int(np.sqrt(Gx + Gy))
    # Initialize the output image
    output = GrayImage(width-2, height-2)
    # Set the data of the output image and return it
    output.data = new_image
    return output

def main():
    filename = input().strip()

    # read input image
    image = readPGM(filename)

    # process image
    output = performSobelEdgeDetection(image)

    # generate output
    total = np.sum(output.data)
    print(total)
    writePGM("output.pgm", output)

if __name__ == "__main__":
    main()