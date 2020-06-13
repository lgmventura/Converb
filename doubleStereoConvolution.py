#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:33:43 2019

@author: luiz
"""

import numpy as np
from scipy.signal import fftconvolve
from scipy.io.wavfile import read as wvrd
from scipy.io.wavfile import write as wvwr

def doubleStereoConvolution(wv1, wv2, wv3, pad0s = False):
    # This matricial approach is more realistic, since you can give a stereo impulse for the left side and another
    # stereo impulse for the right side. On the left side, the left channel of the impulse should be dryer than wet
    # and the right channel impulse should be wetter than dry.
    # Both stereo impulses must be the same length. If not, there is an option to pad zeros (if pad0s == True) or trim
    # (if pad0s == False).
    
    #srate = wv1[0]
    
    wv1_left = wv1[1][:,0]
    wv1_right = wv1[1][:,1]
    
    wv2_left = wv2[1][:,0]
    wv2_right = wv2[1][:,1]
    
    wv3_left = wv3[1][:,0]
    wv3_right = wv3[1][:,1]
    
    if pad0s == False:
        imp_len = min(np.shape(wv2_left)[0], np.shape(wv3_left)[0])
        wv2_left = wv2_left[:imp_len]
        wv2_right = wv2_right[:imp_len]
        wv3_left = wv3_left[:imp_len]
        wv3_right = wv3_right[:imp_len]
    else: # True
        imp_len = np.max(len(wv2_left), len(wv3_left))
        wv2_left = wv2_left + np.zeros(imp_len - np.shape(wv2_left)[0])
        wv2_right = wv2_right + np.zeros(imp_len - np.shape(wv2_right)[0])
        wv3_left = wv3_left + np.zeros(imp_len - np.shape(wv3_left)[0])
        wv3_right = wv3_right + np.zeros(imp_len - np.shape(wv3_right)[0])
        
    
    wv_conv_left = fftconvolve(wv1_left, wv2_left) + fftconvolve(wv1_right, wv2_right)
    wv_conv_right = fftconvolve(wv1_right, wv3_right) + fftconvolve(wv1_left, wv3_left)
    
    wv_conv_left = wv_conv_left/np.max(wv_conv_left)
    wv_conv_right = wv_conv_right/np.max(wv_conv_right)
    
    wv_conv = np.vstack((wv_conv_left, wv_conv_right)).T
    
    return wv_conv