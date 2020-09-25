# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:15:15 2020

@author: akash
"""


import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import seaborn as sns

x = np.linspace(0,5)
y = np.cumsum(np.random.randn(50))+6

length_track= len(x)
heatmap, xedges, yedges = np.histogram2d(x, y, bins=(np.linspace(0,length_track,length_track+1),1))
extent = [0, length_track+1, 0, 5]
plt.imshow(heatmap.T, extent=extent, origin='lower', cmap='jet',vmin=0,vmax=None)
plt.colorbar()
plt.show()

