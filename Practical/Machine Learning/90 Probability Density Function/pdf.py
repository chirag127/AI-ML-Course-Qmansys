# -*- coding: utf-8 -*-
"""
Created on Tue May  5 07:55:02 2020

@author: Bijoy Pal
"""

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-4, 4, 0.001)
plt.plot(x, norm.pdf(x))

plt.show()
