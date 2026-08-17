"""
2. Write a Python program that calculates the variance and standard deviation of the dataset:
[6,7,8,9,10, 11,12]
Display both results
"""

class Dataset:
    def __init__(self):
        self.Data = [6, 7, 8, 9, 10, 11, 12]

    def CalculateMean(self):
        Sum = 0

        for i in range(len(self.Data)):
            Sum = Sum + self.Data[i]

        Mean = Sum / len(self.Data)
        return Mean

    def CalculateVariance(self):
        Mean = self.CalculateMean()

        Sum = 0

        for i in range(len(self.Data)):
            Sum = Sum + ((self.Data[i] - Mean) ** 2)

        Variance = Sum / len(self.Data)
        return Variance

    def CalculateStandardDeviation(self):

        Variance = self.CalculateVariance()

        StandardDeviation = Variance ** 00.5

        return StandardDeviation

def main():
    obj = Dataset()

    obj.CalculateMean()

    Variamce = obj.CalculateVariance()
    StandardDeviation = obj.CalculateStandardDeviation()

    print("Variance : ",Variamce)
    print("Standard Deviation : ",StandardDeviation)

if __name__ == "__main__":
    main()