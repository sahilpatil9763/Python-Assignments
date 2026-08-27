"""
Suppose a dataset has the following values:
6,7,8,9,10, 11, 12

The mean is 9 and standard deviation is 2.
Calculate the scaled values for the following numbers using standard scaling:
• 6
• 9
• 12
"""

class StandardScaling:

    def __init__(self):
        self.Mean = 9
        self.StandardDeviation = 2
        self.Data = [6, 9, 12]

    def CalculateScaling(self):

        for i in range(len(self.Data)):

            ScaledValue = (self.Data[i] - self.Mean) / self.StandardDeviation

            print("Original Value :", self.Data[i])
            print("Scaled Value   :", ScaledValue)
            print()


def main():

    obj = StandardScaling()

    obj.CalculateScaling()


if __name__ == "__main__":
    main()