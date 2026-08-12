"""
Q4: Display students who scored more than 85 in Science.

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
    # Function Name : DisplayScienceStudent
    # Description   : Add Total column containing sum of
    #                 all subject marks
    # ------------------------------------------------------

    def DisplayScienceStudent(self):

        border = "-" * 50

        print(border)
        print("Students Scoring More Than 85 in Science")
        print(border)
        print(self.df[self.df['Science'] > 80] [['Name', 'Science']])                       # Only Prints Science Subject
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

    # Display students scoring more than 85 in Science
    obj.DisplayScienceStudent()

# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()