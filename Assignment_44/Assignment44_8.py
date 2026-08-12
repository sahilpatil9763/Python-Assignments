"""
Q8: Plot a line chart of marks for 'Amit' across all subjects.a

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
    # Function Name : LinePlot
    # Description   : Create line plot of Amit's marks
    #                 across all subjects
    # ------------------------------------------------------

    def LinePlot(self):
        
        Amit = self.df[self.df['Name'] == 'Amit']

        Subjects = ['Math', 'Science', 'English']

        Marks = [
            Amit['Math'].values[0],
            Amit['Science'].values[0],
            Amit['English'].values[0]
        ]

        plt.plot(Subjects, Marks, marker = 'o')

        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.title("Amit's Marks")

        plt.grid()
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

    # Calculate Total marks
    obj.CalculateTotal()

    # Display Line Plot
    obj.LinePlot()


# ==========================================================
# Application Starter
# ==========================================================

if __name__ == "__main__":
    main()