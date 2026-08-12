"""
Q1: Create a DataFrame for student marks and print basic information like shape, columns, and data types.

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
# Description: Create DataFrame and display basic information
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
    # Description   : Display basic DataFrame information
    # ------------------------------------------------------

    def DisplayInfo(self):
        border = "-" * 50

        print(border)
        print("DataFrame : ")
        print(self.df)
        print(border)

        print(border)
        print("Shape : ",self.df.shape)
        print(border)

        print(border)
        print("Columns : ",self.df.columns)
        print(border)

        print(border)
        print("Data types : ")
        print(self.df.dtypes)
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