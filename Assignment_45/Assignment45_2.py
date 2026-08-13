"""
Q2: Create a gender column and perform one-hot encoding.

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# ==========================================================
# Class Name : StudentData
# Description: Create DataFrame and drop a column
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
    # Function Name : AddGender
    # Description   : Add Gender column to DataFrame
    # ------------------------------------------------------

    def AddGender(self):
        self.df['Gender'] = ['Male', 'Male', 'Female']

    # ------------------------------------------------------
    # Function Name : OneHotEncoding
    # Description   : Perform one-hot encoding on Gender
    #                 column
    # ------------------------------------------------------

    def OneHotEncoding(self):

        self.df = pd.get_dummies(self.df, columns=['Gender'], dtype=int)

    # ------------------------------------------------------
    # Function Name : DisplayData
    # Description   : Display updated DataFrame
    # ------------------------------------------------------

    def DisplayData(self):

        border = "-" * 60

        print(border)
        print("\tDataFrame After One-Hot Encoding")
        print(border)

        print(self.df)

        print(border)


# ==========================================================
# Function Name : main
# Description   : Create object and call class methods
# ==========================================================

def main():

    # Create object of StudentData class
    obj = StudentData()

    # Create DataFrame
    obj.CreateDataFrame()

    # Add Gender Column
    obj.AddGender()

    # Perform One-Hot Encoding
    obj.OneHotEncoding()

    # Display updated DataFrame
    obj.DisplayData()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()