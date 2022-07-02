

# make a program that predicts the probability of a 
import math


def predict(x, mean, std):
    """
    x: the value to predict
    mean: the mean of the distribution
    std: the standard deviation of the distribution
    """
    return (1 / (std * (2 * math.pi) ** 0.5)) * math.exp(-0.5 * ((x - mean) / std) ** 2)



