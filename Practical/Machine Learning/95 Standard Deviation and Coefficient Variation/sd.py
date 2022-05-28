from statistics import stdev
from fractions import Fraction as fr
sample1 = (1, 2, 5, 4, 8, 9, 12)
sample2 = (-2, -4, -3, -1, -5, -6)
sample3 = (-9, -1, -0, 2, 1, 3, 4, 19)
sample4 = (1.23, 1.45, 2.1, 2.2, 1.9)
print("The Standard Deviation of Sample1 is :", stdev(sample1))
print("The Standard Deviation of Sample2 is :", stdev(sample2))
print("The Standard Deviation of Sample3 is :", stdev(sample3))
print("The Standard Deviation of Sample4 is :", stdev(sample4))
