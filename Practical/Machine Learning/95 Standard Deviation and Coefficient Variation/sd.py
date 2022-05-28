# -*- coding: utf-8 -*-
"""
Created on Tue May  5 07:58:40 2020

@author: Bijoy Pal
"""

# Python code to demonstrate stdev() 
# function on varioius range of datasets 

# importing the statistics module 
from statistics import stdev 

# importing frations as parameter values 
from fractions import Fraction as fr 

# creating a varying range of sample sets 
# numbers are spread apart but not very much 
sample1 = (1, 2, 5, 4, 8, 9, 12) 

# tuple of a set of negative integers 
sample2 = (-2, -4, -3, -1, -5, -6) 

# tuple of a set of positive and negative numbers 
# data-points are spread apart considerably 
sample3 = (-9, -1, -0, 2, 1, 3, 4, 19) 

# tuple of a set of floating point values 
sample4 = (1.23, 1.45, 2.1, 2.2, 1.9) 

# Print the standard deviation of 
# following sample sets of observations 
print("The Standard Deviation of Sample1 is % s"
							%(stdev(sample1))) 
								
print("The Standard Deviation of Sample2 is % s"
							%(stdev(sample2))) 
								
print("The Standard Deviation of Sample3 is % s"
							%(stdev(sample3))) 
								
								
print("The Standard Deviation of Sample4 is % s"
							%(stdev(sample4))) 
