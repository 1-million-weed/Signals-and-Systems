import numpy as np
from PIL import Image

# Define a class to represent a grayscale image
class GrayImage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = np.zeros((height, width), dtype=int)

# Function to read a PGM image file and convert it to grayscale
def readPGM(filename):
    image = Image.open(filename)
    image = image.convert('L')  # convert image to grayscale
    width, height = image.size
    img = GrayImage(width, height)
    img.data = np.array(image)
    return img

# Function to write a grayscale image to a PGM file
def writePGM(filename, image):
    img = Image.fromarray(image.data.astype(np.uint8))
    img.save(filename)

def convolveImage(operandOne: np.ndarray, operandTwo: np.ndarray) -> int:
    """
    Perform convolution between two matrices and return the squared dot product.

    Args:
        operandOne (np.ndarray): The first operand matrix.
        operandTwo (np.ndarray): The second operand matrix.

    Returns:
        int: The squared dot product of the convolution.
    """
    dot_product = (operandOne * operandTwo).sum()
    return dot_product**2

def performSobelEdgeDetection(image: GrayImage) -> GrayImage:
    """
    Perform Sobel edge detection on a grayscale image.

    Args:
        image (GrayImage): The input grayscale image.

    Returns:
        GrayImage: The output image after applying Sobel edge detection.
    """
    Hx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    
    Hy = np.array([[-1, -2, -1],
                   [ 0,  0,  0],
                   [ 1,  2,  1]])
    height, width = image.data.shape
    new_image = np.zeros((height-2, width-2), dtype=int)
    for x in range(1, image.height-1):
        for y in range(1, image.width-1):
            sub_matrix = image.data[x-1:x+2, y-1:y+2]
            Hx_sub_matrix = convolveImage(Hx, sub_matrix)
            Hy_sub_matrix = convolveImage(Hy, sub_matrix)
            new_image[x-1, y-1] = int(np.sqrt(Hx_sub_matrix + Hy_sub_matrix))
    output = GrayImage(height=height-2, width=width-2)
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