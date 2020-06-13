#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:32:33 2019

@author: luiz
"""

import numpy as np
from scipy.signal import fftconvolve
from scipy.io.wavfile import read as wvrd
from scipy.io.wavfile import write as wvwr

def stereoConvolution(wv1, wv2):
    #srate = wv1[0]
    
    wv1_left = wv1[1][:,0]
    wv1_right = wv1[1][:,1]
    
    wv2_left = wv2[1][:,0]
    wv2_right = wv2[1][:,1]
    
    wv_conv_left = fftconvolve(wv1_left, wv2_left)
    wv_conv_right = fftconvolve(wv1_right, wv2_right)
    
    wv_conv_left = wv_conv_left/np.max(wv_conv_left)
    wv_conv_right = wv_conv_right/np.max(wv_conv_right)
    
    wv_conv = np.vstack((wv_conv_left, wv_conv_right)).T
    
    return wv_conv