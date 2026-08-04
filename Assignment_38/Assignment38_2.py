"""
2. Write a program to:

• Display total number of students in the dataset
• Count how many students Passed (FinalResult = 1)
• Count how many students Failed (FinaResult = 0)
"""

import pandas as pd

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    print("Total number of students in the dataset : ", len(df))

    print("Students Passed : ", (df["FinalResult"] == 1).sum())

    print("Students Failed : ", (df["FinalResult"] == 0).sum())

if __name__ == "__main__":
    main()