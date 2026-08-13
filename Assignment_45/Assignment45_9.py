"""
Q9: Rename 'Math' column to 'Mathematics'.

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
# Description: Create DataFrame and rename a column
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
    # Function Name : RenameColumn
    # Description   : Rename Math column to Mathematics
    # ------------------------------------------------------

    def RenameColumn(self):

        self.df.rename(
            columns={'Math': 'Mathematics'},
            inplace=True
        )

    # ------------------------------------------------------
    # Function Name : DisplayData
    # Description   : Display updated DataFrame
    # ------------------------------------------------------

    def DisplayData(self):

        border = "-" * 50

        print(border)
        print("DataFrame After Renaming Column")
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

    # Rename Math column
    obj.RenameColumn()

    # Display updated DataFrame
    obj.DisplayData()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()