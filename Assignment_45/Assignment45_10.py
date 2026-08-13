"""
Q10: Plot a boxplot for English marks to check
     distribution and outliers.

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# Class Name : StudentData
# Description: Create DataFrame and plot boxplot
# ==========================================================

class StudentData:

    # ------------------------------------------------------
    # Function Name : __init__
    # Description   : Initialize student data
    # ------------------------------------------------------

    def __init__(self):

        self.data = {
            'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]
        }

    # ------------------------------------------------------
    # Function Name : CreateDataFrame
    # Description   : Create Pandas DataFrame
    # ------------------------------------------------------

    def CreateDataFrame(self):

        self.df = pd.DataFrame(self.data)

    # ------------------------------------------------------
    # Function Name : DisplayBoxPlot
    # Description   : Plot boxplot for English marks
    #                 to check distribution and outliers
    # ------------------------------------------------------

    def DisplayBoxPlot(self):

        plt.boxplot(self.df['English'])

        plt.ylabel("English Marks")
        plt.title("Boxplot of English Marks")

        plt.show()


# ==========================================================
# Function Name : main
# Description   : Create object and call class methods
# ==========================================================

def main():

    # Create object of StudentData class
    obj = StudentData()

    # Create DataFrame
    obj.CreateDataFrame()

    # Display boxplot
    obj.DisplayBoxPlot()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()