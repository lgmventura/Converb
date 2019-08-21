#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:45:04 2019

@author: luiz
"""

# Audio convolution

from tkinter import *
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


def on_convolve_button_click(entries):
    e = []
    field = []
    for k, entry in enumerate(entries):
        field.append(entry[0])
        e.append(entry[1].get())
    path1 = e[0]
    path2 = e[1]
    path_out = e[2]
    
    wv1 = wvrd(path1)
    wv2 = wvrd(path2)
    srate = wv1[0]
    
    wv_conv = stereoConvolution(wv1, wv2)
    wvwr(path_out, srate, wv_conv.astype('float32'))
    

# APP
fields = 'Path to audio file 1', 'Path to audio file 2', 'Path to output file'
std_entries = '', '', '/home/luiz/StereoAudioConvolverOutput.wav'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 

def set_std(entries):
    for k, entry in enumerate(entries):
        entry[1].insert(0, std_entries[k])

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=20, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   set_std(ents)
   root.bind('<Return>', (lambda event, e=ents: on_convolve_button_click(e)))   
   b1 = Button(root, text='Convolve',
          command=(lambda e=ents: on_convolve_button_click(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.destroy)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()

