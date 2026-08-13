"""
Q10: Drop the 'English' column from original DataFrame.

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
"""

import pandas as pd
import numpy as np

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
    # Function Name : DropColumn
    # Description   : Drop English column from DataFrame
    # ------------------------------------------------------

    def DropColumn(self):

        self.df = self.df.drop('English', axis=1)

    # ------------------------------------------------------
    # Function Name : DisplayData
    # Description   : Display updated DataFrame
    # ------------------------------------------------------

    def DisplayData(self):

        border = "-" * 50

        print(border)
        print("DataFrame After Dropping English Column")
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

    # Drop English column
    obj.DropColumn()

    # Display updated DataFrame
    obj.DisplayData()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()