import numpy as np


def add(arr1, arr2):
    """Add two numpy arrays element-wise."""
    return np.add(arr1, arr2)


def subtract(arr1, arr2):
    """Subtract one numpy array from another element-wise."""
    return np.subtract(arr1, arr2)


def multiply(arr1, arr2):
    """Multiply two numpy arrays element-wise."""
    return np.multiply(arr1, arr2)


def divide(arr1, arr2):
    """Divide one numpy array by another element-wise."""
    return np.divide(arr1, arr2)


class Arithmetic:
    def __init__(self):
        pass

    def add(self, arr1, arr2):
        return add(arr1, arr2)

    def subtract(self, arr1, arr2):
        return subtract(arr1, arr2)

    def multiply(self, arr1, arr2):
        return multiply(arr1, arr2)

    def divide(self, arr1, arr2):
        return divide(arr1, arr2)
