import numpy as np
from PIL import Image

FORWARD = 1
REVERSE = -1
THRESHOLD = 0.9

class GrayImage:
    def __init__(self, width, height, data):
        # Initialize the GrayImage object with width, height, and data
        self.width = width
        self.height = height
        self.data = data

def readPGM(filename):
    # Open the image file
    image = Image.open(filename)
    # Convert the image to grayscale
    image = image.convert('L')
    # Get the size of the image
    width, height = image.size
    # Convert the image data to a numpy array
    data = np.array(image)
    # Create a GrayImage object with the image data
    img = GrayImage(width, height, data)
    return img

def writePGM(filename, img):
    # Create an image from the GrayImage data
    image = Image.fromarray(img.data)
    # Save the image to a file
    image.save(filename)

def mirror(image):
    # Convert the GrayImage data to a numpy array
    image = np.array(img.data)
    # Reflect each row of the image
    image = np.fliplr(image)
    # Reflect the rows of the image
    image = np.flipud(image)
    return image

def powerOfTwo(n):
    # Calculate the smallest power of two greater than or equal to n
    return 2**np.ceil(np.log2(n))

##############################################
'''
This function computes an in-place complex-to-complex FFT
x and y are the real and imaginary arrays of 2^m points.
dir =  FORWARD gives forward transform
dir =  REVERSE gives reverse transform
'''

def fft1D(direction, re, im):
    # Calculate the length of the input arrays and the number of bits needed to represent that length
    len_ = len(re)
    bits = int(np.log2(len_))

    # Perform the bit-reversal of the input arrays
    j = 0
    for i in range(len_-1):
        # Swap elements i and j if i is less than j
        if i < j:
            re[i], re[j] = re[j], re[i]
            im[i], im[j] = im[j], im[i]
        # Calculate the next value of j
        k = len_ >> 1
        while k <= j:
            j -= k
            k >>= 1
        j += k

    # Compute the FFT
    c1 = -1.0
    c2 = 0.0
    l2 = 1
    for _ in range(bits):
        l1 = l2
        l2 <<= 1
        u1 = 1.0
        u2 = 0.0
        # Perform the butterfly operations
        for j in range(l1):
            for i in range(j, len_, l2):
                i1 = i + l1
                # Calculate the twiddle factor
                t1 = u1 * re[i1] - u2 * im[i1]
                t2 = u1 * im[i1] + u2 * re[i1]
                # Perform the butterfly operation
                re[i1] = re[i] - t1
                im[i1] = im[i] - t2
                re[i] += t1
                im[i] += t2
            # Update the twiddle factor
            z = u1 * c1 - u2 * c2
            u2 = u1 * c2 + u2 * c1
            u1 = z
        # Update the cosine and sine values
        c2 = np.sqrt((1.0 - c1) / 2.0)
        if direction == FORWARD:
            c2 = -c2
        c1 = np.sqrt((1.0 + c1) / 2.0)

    # Scaling for reverse transform
    if direction == REVERSE:
        for i in range(len_):
            re[i] /= len_
            im[i] /= len_

    return re, im

##############################################
######### YOU HAVE TO IMPLEMENT THIS #########
##############################################
'''
Perform a 2D FFT inplace given a complex 2D array
The direction dir can be FORWARD or REVERSE.
'''

def fft2D(direction, re, im):
    '''YOU HAVE TO IMPLEMENT THE BODY OF THIS FUNCTION YOURSELF'''
    '''YOU CAN USE THE fft1D() FUNCTION ABOVE'''
    # 1) Get the shape of the real part of the image
    shape_real = re.shape
    # 2) Perform 1D FFT on each row of the real and imaginary parts of the image
    for row in range(shape_real[0]):
        re[row], im[row] = fft1D(direction=direction, re=re[row], im=im[row])
    # 3) Initialize arrays to hold the real and imaginary parts of the column transform
    real_column = np.zeros(shape=shape_real)
    im_column = np.zeros(shape=shape_real)
    # 4) Perform 1D FFT on each column of the real and imaginary parts of the image
    for column in range(shape_real[1]):
        real_column[:, column], im_column[:, column] = fft1D(direction=direction, re=re[:, column], im=im[:, column])
    return real_column, im_column
##############################################
##############################################
##############################################

def fftCorrelator(image, mask, corrWidth, corrHeight):
    # Calculate the width and height for the FFT, which should be a power of two
    width = int(powerOfTwo(image.width + mask.width - 1))
    height = int(powerOfTwo(image.height + mask.height - 1))

    # Allocate arrays for the real and imaginary parts of the image and mask
    imreal = np.zeros((height, width))
    imimag = np.zeros((height, width))
    maskreal = np.zeros((height, width))
    maskimag = np.zeros((height, width))

    # Copy the image data into the real part of the image array
    imreal[:image.height, :image.width] = image.data

    # Copy the mirror of the mask data into the real part of the mask array
    maskreal[:mask.height, :mask.width] = mask.data[::-1, ::-1]

    # Perform FFT on the image and mask
    fft2D(FORWARD, imreal, imimag)
    fft2D(FORWARD, maskreal, maskimag)

    # Perform pairwise complex multiplication of the image and mask
    realPart = imreal * maskreal - imimag * maskimag
    imagPart = imreal * maskimag + imimag * maskreal
    imreal, imimag = realPart, imagPart

    # Perform inverse FFT on the result
    fft2D(REVERSE, imreal, imimag)

    # Copy the result into the correlation array
    corr = imreal[:corrHeight, :corrWidth]

    return corr

##############################################

def prefSum(width, height, im):
    # Initialize a zero matrix of the same size as the image
    ps = np.zeros((height, width), dtype=int)
    
    # Compute the prefix sum for the first row
    ps[0, 0] = im[0, 0]
    for c in range(1, width):
        ps[0, c] = im[0, c] + ps[0, c-1]
    
    # Compute the prefix sum for the remaining rows
    for r in range(1, height):
        # Compute the prefix sum for the first column
        ps[r, 0] = im[r, 0] + ps[r-1, 0]
        # Compute the prefix sum for the remaining columns
        for c in range(1, width):
            ps[r, c] = ps[r-1, c] + ps[r, c-1] - ps[r-1, c-1] + im[r, c]
    return ps

def prefSquaredSum(width, height, im):
    # Initialize a zero matrix of the same size as the image
    ps = np.zeros((height, width), dtype=int)
    
    # Compute the prefix sum of squares for the first row
    ps[0, 0] = im[0, 0]**2
    for c in range(1, width):
        ps[0, c] = im[0, c]**2 + ps[0, c-1]
    
    # Compute the prefix sum of squares for the remaining rows
    for r in range(1, height):
        # Compute the prefix sum of squares for the first column
        ps[r, 0] = im[r, 0]**2 + ps[r-1, 0]
        # Compute the prefix sum of squares for the remaining columns
        for c in range(1, width):
            ps[r, c] = ps[r-1, c] + ps[r, c-1] - ps[r-1, c-1] + im[r, c]**2
    return ps

def sum(row0, col0, row1, col1, prefsum):
    # Initialize the sum
    s = 0
    # Adjust the row and column indices
    row0 -= 1
    col0 -= 1
    row1 -= 1
    col1 -= 1

    # Add and subtract elements from the prefix sum to compute the sum of the submatrix
    if 0 <= row1:
        if 0 <= col1: s += prefsum[row1, col1]
        if 0 <= col0: s -= prefsum[row1, col0]
    if 0 <= row0:
        if 0 <= col1: s -= prefsum[row0, col1]
        if 0 <= col0: s += prefsum[row0, col0]

    return s

def sum0(row0, col0, row1, col1, im):
    # Initialize the sum
    s = 0
    # Compute the sum of the submatrix
    for r in range(row0, row1):
        for c in range(col0, col1):
            s += im[r, c]
    return s

def sqsum(row0, col0, row1, col1, im):
    # Initialize the sum
    s = 0
    # Compute the sum of squares of the submatrix
    for r in range(row0, row1):
        for c in range(col0, col1):
            s += im[r, c]**2
    return s

##############################################

def pearsonCorrelator(image, mask, corrWidth, corrHeight):
    # Get the image and mask data
    im = image.data
    ms = mask.data

    # Compute standard correlation (no pearson yet!)
    corr = fftCorrelator(image, mask, corrWidth, corrHeight)

    # Compute prefix sum of image (a.k.a. summed area table)
    imprefsum = prefSum(image.width, image.height, im)
    msprefsum = prefSum(mask.width, mask.height, ms)
    imprefsqsum = prefSquaredSum(image.width, image.height, im)
    msprefsqsum = prefSquaredSum(mask.width, mask.height, ms)

    # Iterate over the correlation height
    for r in range(corrHeight):
        dr = r - mask.height + 1
        # Iterate over the correlation width
        for c in range(corrWidth):
            dc = c - mask.width + 1

            # Compute bounding box of overlap in image
            ir0 = max(dr, 0)
            ic0 = max(dc, 0)
            ir1 = min(image.height, dr+mask.height)
            ic1 = min(image.width, dc+mask.width)

            # Compute bounding box of overlap in mask
            mr0 = max(-dr, 0)
            mc0 = max(-dc, 0)
            mr1 = min(mask.height, image.height-dr)
            mc1 = min(mask.width, image.width-dc)

            # Compute number of points in overlap
            npoints = (ir1-ir0)*(ic1-ic0)

            # Compute pearson coefficient for delay (dr,dc)
            sx = sum(ir0, ic0, ir1, ic1, imprefsum)
            sx2 = sum(ir0, ic0, ir1, ic1, imprefsqsum)

            sy = sum(mr0, mc0, mr1, mc1, msprefsum)
            sy2 = sum(mr0, mc0, mr1, mc1, msprefsqsum)

            mx = sx/npoints
            my = sy/npoints

            # If the squared sum equals the product of the mean and the sum, set pc to 0
            if (sx2 == mx*sx) or (sy2 == my*sy):
                pc = 0
            else:
                # Compute the denominator and the Pearson correlation coefficient
                denom = np.sqrt((sx2-mx*sx)*(sy2-my*sy))
                pc = corr[r, c] - (sx/npoints)*sy
                pc /= denom

            # Update the correlation matrix
            corr[r, c] = pc

    # Return the correlation matrix
    return corr

##############################################

def drawbox(y0, x0, y1, x1, im):
    # Initialize newbox as 1
    newbox = 1

    # Iterate over the range from x0 to x1
    for x in range(x0, x1):
        # If the pixel at (y0, x) or (y1, x) is white (255), set newbox to 0
        if im[y0][x] == 255 or im[y1][x] == 255:
            newbox = 0
        # Set the pixel at (y0, x) and (y1, x) to white (255)
        im[y0][x] = im[y1][x] = 255

    # Iterate over the range from y0+1 to y1-1
    for y in range(y0+1, y1-1):
        # If the pixel at (y, x0) or (y, x1) is white (255), set newbox to 0
        if im[y][x0] == 255 or im[y][x1] == 255:
            newbox = 0
        # Set the pixel at (y, x0) and (y, x1) to white (255)
        im[y][x0] = im[y][x1] = 255

    # Return newbox
    return newbox

def match(p, mw, mh, pcorr, image):
    # Get the image data
    im = image.data

    # Initialize count as 0
    cnt = 0

    # Iterate over the range from mh to image height
    for r in range(mh, image.height):
        # Iterate over the range from mw to image width
        for c in range(mw, image.width):
            # If the correlation at (r, c) is greater than or equal to the threshold
            if pcorr[r][c] >= THRESHOLD:
                # Increase count by the result of drawbox function
                cnt += drawbox(r-mh, c-mw, r, c, im)

    # Return count
    return cnt

##############################################

def main():
    # Read the input image and mask
    image = readPGM("smb_w11.pgm")
    mask = readPGM("box.pgm")

    # Calculate the dimensions of the correlation result
    corrWidth = image.width + mask.width - 1
    corrHeight = image.height + mask.height - 1

    # Perform correlation using Pearson correlator
    corr = pearsonCorrelator(image, mask, corrWidth, corrHeight)

    # Match the template in the image and count the number of matches
    cnt = match(THRESHOLD, mask.width, mask.height, corr, image)

    # Print the count of matches
    print(cnt)

    # Write the resulting image with matched boxes
    writePGM("match.pgm", image)

if __name__ == "__main__":
    main()