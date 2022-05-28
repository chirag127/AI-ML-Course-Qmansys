# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:44:48 2020

@author: Bijoy Pal
"""

import matplotlib.pyplot as plt
sizes = [25, 20, 45, 10]
labels = ["Cats", "Dogs", "Tigers", "Goats"]

plt.pie(sizes, labels = labels, autopct = "%.2f")
plt.axes().set_aspect("equal")
plt.show()