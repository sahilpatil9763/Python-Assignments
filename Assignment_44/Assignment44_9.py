"""
Q9: Create a DataFrame with missing values and fill them
    with column mean.

data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}
"""

import pandas as pd
import numpy as np

# ==========================================================
# Class Name : StudentData
# Description: Create DataFrame and handle missing values
# ==========================================================

class StudentData:

    # ------------------------------------------------------
    # Function Name : __init__
    # Description   : Initialize student data
    # ------------------------------------------------------

    def __init__(self):

        self.data = {
            'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [np.nan, 76, 88],
            'Science': [91, np.nan, 85]
        }

    # ------------------------------------------------------
    # Function Name : CreateDataFrame
    # Description   : Create Pandas DataFrame
    # ------------------------------------------------------

    def CreateDataFrame(self):

        self.df = pd.DataFrame(self.data)

    # ------------------------------------------------------
    # Function Name : FillMissingValues
    # Description   : Fill missing values with column mean
    # ------------------------------------------------------

    def FillMissingValues(self):

        self.df['Math'] = self.df['Math'].fillna(
            self.df['Math'].mean()
        )

        self.df['Science'] = self.df['Science'].fillna(
            self.df['Science'].mean()
        )

    # ------------------------------------------------------
    # Function Name : DisplayData
    # Description   : Display updated DataFrame
    # ------------------------------------------------------

    def DisplayData(self):

        border = "-" * 50

        print(border)
        print("DataFrame After Filling Missing Values")
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

    # Fill missing values with column mean
    obj.FillMissingValues()

    # Display updated DataFrame
    obj.DisplayData()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()