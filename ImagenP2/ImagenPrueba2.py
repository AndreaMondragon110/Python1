# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:48:10 2020

@author: Andrea Mondragón
"""


import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def listarImagen(lista):
   l=misc.figure()
   misc.imsave('figure.png', l)
   plt.imshow()
   plt.show()
   figure=misc.imread('figure.png')
   type (figure)
   figure.shape, figure.dtype
   l.tofile('figure.raw')
   
   figure_from_raw = np.fromfile('figure.raw', dtype=np.int64)
   figure_from_raw.shape
   (262144,)
   figure_from_raw.shape = (512, 512)
   import os
   os.remove('figure.raw')
   #figure_memmap = np.memmap('figure.raw', dtype=np.int64, shape=(512, 512))
  
   plt.imshow(l, cmap=plt.cm.gray)

