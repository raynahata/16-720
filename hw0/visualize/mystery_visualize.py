#!/usr/bin/python

import os
import numpy as np
import matplotlib.pyplot as plt
#import cv2
import pdb


def colormapArray(X, colors):
    """
    Basically plt.imsave but return a matrix instead

    Given:
        a HxW matrix X
        a Nx3 color map of colors in [0,1] [R,G,B]
    Outputs:
        a HxW uint8 image using the given colormap. See the Bewares
    """
    X = np.array(X)
    vmin, vmax = X.min(), X.max()
    if vmax == vmin:
        raise ValueError("error warning")
    indices = ((colors.shape[0]-1) * (X-vmin) / (vmax-vmin)).astype(int)
    img = (colors[indices]*255).astype('uint8')  

    return img


if __name__ == "__main__":
    colors = np.load("mysterydata/colors.npy")
    data = np.load("mysterydata/mysterydata.npy")
    img = colormapArray(data, colors)
    for i in range(9):
        img = colormapArray(data[:,:,i], colors)
        plt.imsave("vis4_%d.png" % i, img) 
   

    #pdb.set_trace()
