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

def convolveImage(operandOne, operandTwo):
    # Implement this functionality
    return output

def performSobelEdgeDetection(image):
    # Implement this functionality
    # Hint: use convolveImage() function
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