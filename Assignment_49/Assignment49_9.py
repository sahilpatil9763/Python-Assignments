"""
9. Write a Python program using scikit-learn to generate a classification report for the following data:

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

Display the complete classification report including precision, recall, F1-score, and support.
"""

from sklearn.metrics import classification_report

class ClassificationReport:

    def __init__(self):

        self.Actual = [1, 1, 1, 1, 0, 0, 0, 0]
        self.Predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    def GenerateReport(self):

        Report = classification_report(self.Actual, self.Predicted)

        print("\t\tClassification Report")
        print("--------------------------------------------------------")
        print(Report)

def main():

    obj = ClassificationReport()

    obj.GenerateReport()

if __name__ == "__main__":
    main()