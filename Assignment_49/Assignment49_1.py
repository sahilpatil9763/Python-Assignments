"""
1. Write a Python program that calculates the mean of a dataset using NumPy for the following values:
[6, 7, 8, 9, 10, 11, 12]
"""

import numpy as np

class CalculateMean:
    def __init__(self):
        self.Data = np.array([6, 7, 8, 9, 10, 11, 12])

    def Mean(self):
        # Mean is 9.0

        Mean = np.mean(self.Data)
        print("Dataset :", self.Data)
        print("Mean of dataset :", Mean)

def main():
    obj = CalculateMean()

    obj.Mean()

if __name__ == "__main__":
    main()