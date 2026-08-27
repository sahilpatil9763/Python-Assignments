"""
Consider the dataset:
4,6,8,10,12

Perform the following steps:
• Calculate the mean
• Find the deviation of each value from the mean
• Calculate the square of each deviation
• Calculate the variance of the dataset.
"""

class Variance:
    def __init__(self):
        self.Data = [4,6,8,10,12]

    def CalculateMean(self):
        Sum = 0

        for i in range(len(self.Data)):
            Sum = Sum + self.Data[i]

        Mean = Sum / len(self.Data)
        return Mean

    def CalculateVariance(self,Mean):
        Sum = 0

        for i in range(len(self.Data)):
            Deviation = self.Data[i] - Mean

            SquaredDeviation = Deviation ** 2

            print("Value : ",self.Data[i])
            print("Deviation : ",Deviation)
            print("SquaredDeviation : ",SquaredDeviation)
            print()

            Sum = Sum + SquaredDeviation

        Variance = Sum / len(self.Data)

        return Variance

def main():
    obj = Variance()

    Mean = obj.CalculateMean()

    print("Mean : ",Mean)
    print()

    VarianceValue = obj.CalculateVariance(Mean)
    print("Variance : ",VarianceValue)

if __name__ == "__main__":
    main()