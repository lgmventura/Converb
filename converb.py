#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri 23 Aug 2019 19:31:38

@author: Luiz Guilherme de Medeiros Ventura

Usage:
    $python converb.py audioFile.wav stereoImpulseRespForBothChannels.wav output.wav
    
    or
    
    $python converb.py audioFile.wav stereoImpulseRespForLeftChannel.wav stereoImpulseRespForRightChannel.wav output.wav

"""

import sys
from scipy.io.wavfile import read as wvrd
from scipy.io.wavfile import write as wvwr
from stereoConvolution import stereoConvolution
from doubleStereoConvolution import doubleStereoConvolution

path1 = sys.argv[1]
path2 = sys.argv[2]

wv1 = wvrd(path1)
wv2 = wvrd(path2)

if len(sys.argv) == 4:
    path_out = sys.argv[3]
    wv_conv = stereoConvolution(wv1, wv2)
elif len(sys.argv) == 5:
    path3 = sys.argv[3]
    wv3 = wvrd(path3)
    path_out = sys.argv[4]
    wv_conv = doubleStereoConvolution(wv1, wv2, wv3)

srate = wv1[0]

wvwr(path_out, srate, wv_conv.astype('float32'))