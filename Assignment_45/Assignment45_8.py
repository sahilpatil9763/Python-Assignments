"""
Q8: Plot a histogram of Math marks.

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
# Description: Create DataFrame and plot histogram
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
    # Function Name : DisplayHistogram
    # Description   : Plot histogram of Math marks
    # ------------------------------------------------------

    def DisplayHistogram(self):

        plt.hist(self.df['Math'], label="Math Marks")

        plt.xlabel("Math Marks")
        plt.ylabel("Frequency")
        plt.title("Distribution of Math Marks")

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

    # Display histogram
    obj.DisplayHistogram()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()