"""
Q2: Use the DataFrame from Q1 and print descriptive statistics using describe().

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
"""

import pandas as pd

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
    # Function Name : DisplayInformation
    # Description   : Display Descriptive Statistics
    # ------------------------------------------------------

    def DisplayInfo(self):
        border = "-" * 50

        print(border)
        print("Descriptive Statistics : ")
        print(self.df.describe())
        print(border)


# ==========================================================
# Function Name : main
# Description   : Create object and call class methods
# ==========================================================

def main():
    obj = StudentData()

    obj.CreateDataFrame()
    obj.DisplayInfo()

if __name__ == "__main__":
    main()