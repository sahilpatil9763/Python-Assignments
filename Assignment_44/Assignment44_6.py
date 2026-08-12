"""
Q6: Sort the DataFrame by 'Total' marks in descending order.

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
    # Function Name : SortData
    # Description   : Sort DataFrame by Total marks in
    #                 descending order
    # ------------------------------------------------------

    def SortData(self):
        self.df = self.df.sort_values(by = 'Total', ascending = False)

    # ------------------------------------------------------
    # Function Name : DisplayData
    # Description   : Dsiplay updated data
    # ------------------------------------------------------

    def DisplayData(self):

        border = "-" * 50

        print(border)
        print("\tStudent DataFrame sorted by Total")
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

    # Sort DataFrame by Total in descending order
    obj.SortData()

    # Display sorted DataFrame
    obj.DisplayData()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()