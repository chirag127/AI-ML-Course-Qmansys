from statistics import stdev
from statistics import mean


# Driver Program
arr = [15, 36, 53.67, 25.45, 67.8, 56, 78.09]


def coefficientOfVariation(arr):
    return stdev(arr) / mean(arr)


print("Coefficient of variation is:", coefficientOfVariation(arr))
