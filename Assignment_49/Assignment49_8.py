"""
8. Write a Python program that calculates TP, TN, FP, FN for the following arrays:

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

Display all four values.
"""

class ConfusionMatrix:

    def __init__(self):

        self.Actual = [1, 1, 1, 1, 0, 0, 0, 0]
        self.Predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    def Calculate(self):

        TP = 0
        TN = 0
        FP = 0
        FN = 0

        for i in range(len(self.Actual)):

            if self.Actual[i] == 1 and self.Predicted[i] == 1:
                TP = TP + 1

            elif self.Actual[i] == 0 and self.Predicted[i] == 0:
                TN = TN + 1

            elif self.Actual[i] == 0 and self.Predicted[i] == 1:
                FP = FP + 1

            elif self.Actual[i] == 1 and self.Predicted[i] == 0:
                FN = FN + 1

        print("True Positive (TP)  :", TP)
        print("True Negative (TN)  :", TN)
        print("False Positive (FP) :", FP)
        print("False Negative (FN) :", FN)

def main():

    obj = ConfusionMatrix()

    obj.Calculate()

if __name__ == "__main__":
    main()