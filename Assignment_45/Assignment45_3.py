"""
Q3: Group students by gender and calculate average marks.

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
# Description: Create DataFrame and calculate average marks
#              based on gender
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
    # Function Name : CalculateAverage
    # Description   : Group students by gender and calculate
    #                 average marks
    # ------------------------------------------------------

    def CalculateAverage(self):

        self.result = self.df.groupby('Gender')[
            ['Math', 'Science', 'English']
        ].mean()

    # ------------------------------------------------------
    # Function Name : DisplayData
    # Description   : Display average marks by gender
    # ------------------------------------------------------

    def DisplayData(self):

        border = "-" * 50

        print(border)
        print("\tAverage Marks By Gender")
        print(border)

        print(self.result)

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

    # Add Gender column
    obj.AddGender()

    # Calculate average marks
    obj.CalculateAverage()

    # Display result
    obj.DisplayData()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()