"""
Q4: Plot a pie chart of subject marks for 'Sagar'.

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
"""

import pandas as pd
import matplotlib.pyplot as plt

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
    # Function Name : DisplayPieChart
    # Description   : Create pie chart of Sagar's marks
    #                 across all subjects
    # ------------------------------------------------------

    def DisplayPieChart(self):

        Sagar = self.df[self.df["Name"] == 'Sagar']

        Subjects = ['Math', 'Science', 'English']

        Marks = [
            Sagar['Math'].values[0],
            Sagar['Science'].values[0],
            Sagar['English'].values[0]
        ]

        plt.pie(Marks, labels=Subjects, autopct='%1.1f%%')

        plt.title("Sagar's Subject Marks")
        plt.legend()
        plt.show()


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
    obj.DisplayPieChart()


    # Display result
    obj.DisplayData()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()