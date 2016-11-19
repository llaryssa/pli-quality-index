import numpy as np
from scipy import misc
from scipy import ndimage
# from scipy.signal import convolve2d
import matplotlib.pyplot as plt


############## algorithm ##################

def quality_index(im1, im2, block_size = 8):
    if not im1.shape == im2.shape:
        print "ERROR: images not the same size"

    N = block_size * block_size
    sum_filter = np.ones((block_size, block_size))

    im1_sq = im1 * im1
    im2_sq = im2 * im2
    im12 = im1 * im2

    im1_sum = filter(im1, sum_filter)
    im2_sum = filter(im2, sum_filter)
    im12_sum = filter(im12, sum_filter)
    im1_sq_sum = filter(im1_sq, sum_filter)
    im2_sq_sum = filter(im2_sq, sum_filter)

    im12_sum_mul = im1_sum * im2_sum
    im12_sq_sum_mul = (im1_sum * im1_sum) + (im2_sum * im2_sum)

    num = 4 * (N * im12_sum - im12_sum_mul) * im12_sum_mul
    den1 = N*(im1_sq_sum + im2_sq_sum) - im12_sq_sum_mul
    den = den1 * im12_sq_sum_mul

    quality_map = np.ones(den.shape)
    index = (den1 == 0) & (im12_sq_sum_mul != 0)
    quality_map[index] = 2*im12_sum_mul[index]/im12_sq_sum_mul[index]
    index = den != 0
    quality_map[index] = num[index]/den[index]

    return quality_map.mean()

def filter(im, kernel):
    n = kernel.shape[0]
    nn = int((n/2.0) - 1)
    (a,b) = im.shape
    imm = ndimage.convolve(im,kernel)
    imm = imm[nn:a-nn-1, nn:b-nn-1]
    return imm

################### main ########################

original_image = misc.imread('images/lena.gif')
original_image = np.array(original_image, dtype='f')

filenames = ['lena-salt-pepper', 'lena-blurred','lena-mean-shift', 'lena-speckle', 'lena-gaussian'];

for f in filenames:
    test_image = misc.imread('images/' + f + '.gif')
    test_image = np.array(test_image, dtype='f')
    print quality_index(original_image, test_image)
