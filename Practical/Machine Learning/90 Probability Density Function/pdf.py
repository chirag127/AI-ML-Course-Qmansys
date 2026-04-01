# -*- coding: utf-8 -*-
"""
Created on Tue May  5 07:55:02 2020

@author: Bijoy Pal
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

x = np.arange(-4, 4, 0.001)
plt.plot(x, norm.pdf(x))

plt.show()
