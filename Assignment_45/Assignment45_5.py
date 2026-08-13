"""
Q5: Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail".

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
    # Function Name : AddStatus
    # Description   : Add Status column based on Total marks
    #                 Total >= 250 -> Pass
    #                 Total < 250  -> Fail
    # ------------------------------------------------------

    def AddStatus(self):
        self.df['Status'] = self.df['Total'].apply(
            lambda x: 'Pass' if x >= 250 else 'Fail'
        ) 

    # ------------------------------------------------------
    # Function Name : DisplayData
    # Description   : Display updated DataFrame
    # ------------------------------------------------------

    def DisplayData(self):

        border = "-" * 50

        print(border)
        print("Student Result")
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

    # Calculate Total marks
    obj.CalculateTotal()

    # Add Status column
    obj.AddStatus()

    # Display updated DataFrame
    obj.DisplayData()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()