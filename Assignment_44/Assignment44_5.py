"""
Q5: Replace 'Pooja' with 'Puja' in the 'Name' column.

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
    # Function Name : ReplaceName
    # Description   : Replace Pooja with Puja
    # ------------------------------------------------------

    def ReplaceName(self):
        self.df['Name'] = self.df['Name'].replace('Pooja','Puja')

    # ------------------------------------------------------
    # Function Name : DisplayData
    # Description   : Dsiplay updated data
    # ------------------------------------------------------

    def DisplayData(self):

        border = "-" * 50

        print(border)
        print("\tUpdated Student DataFrame")
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

   # Replace Pooja with Puja
    obj.ReplaceName()

    # Display updated DataFrame
    obj.DisplayData()

# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()