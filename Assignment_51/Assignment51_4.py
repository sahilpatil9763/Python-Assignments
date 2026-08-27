"""
Consider the dataset:
5,7,9,11,13

Perform the following calculations step by step:
• Calculate the mean
• Calculate the variance
• Calculate the standard deviation.
"""

class Statistics:

    def __init__(self):
        self.Data = [5, 7, 9, 11, 13]

    def CalculateMean(self):

        Sum = 0

        for i in range(len(self.Data)):
            Sum = Sum + self.Data[i]

        Mean = Sum / len(self.Data)

        return Mean

    def CalculateVariance(self, Mean):

        Sum = 0

        for i in range(len(self.Data)):

            Deviation = self.Data[i] - Mean
            SquaredDeviation = Deviation ** 2

            print("Value :", self.Data[i])
            print("Deviation :", Deviation)
            print("Squared Deviation :", SquaredDeviation)
            print()

            Sum = Sum + SquaredDeviation

        Variance = Sum / len(self.Data)

        return Variance

    def CalculateStandardDeviation(self, Variance):

        StandardDeviation = Variance ** 0.5

        return StandardDeviation


def main():

    obj = Statistics()

    # Calculate Mean
    Mean = obj.CalculateMean()

    print("Mean :", Mean)
    print()

    # Calculate Variance
    Variance = obj.CalculateVariance(Mean)

    print("Variance :", Variance)
    print()

    # Calculate Standard Deviation
    StandardDeviation = obj.CalculateStandardDeviation(Variance)

    print("Standard Deviation :", StandardDeviation)


if __name__ == "__main__":
    main()