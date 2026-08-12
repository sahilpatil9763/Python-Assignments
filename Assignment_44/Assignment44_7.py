"""
Q7: Create a bar plot of student names vs total marks.

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
# Description: Create DataFrame and descriptive statistics
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
    # Function Name : CalculateTotal
    # Description   : Calculate total marks of all subjects
    # ------------------------------------------------------

    def CalculateTotal(self):

        self.df['Total'] = (
            self.df['Math'] +
            self.df['Science'] +
            self.df['English']
        )

    # ------------------------------------------------------
    # Function Name : BarPlot
    # Description   : Create bar plot of student names
    #                 vs total marks
    # ------------------------------------------------------

    def BarPlot(self):
        plt.bar(self.df['Name'], self.df['Total'], width=.2, edgecolor='black')

        plt.xlabel("Student Names")
        plt.ylabel("Total Maarks")
        plt.title("Student Names vs Total Marks")

        plt.grid()
        plt.legend()
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

    # Calculate Total marks
    obj.CalculateTotal()

    # Display Bar Plot
    obj.BarPlot()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()