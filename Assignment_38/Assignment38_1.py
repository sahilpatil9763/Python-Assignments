"""
1. Write a Python program to load the file student_performance_m1. csv using pandas.
Display:

• First 5 records
• Last 5 records
• Total number of rows and columns
• List of column names
• Data types of each column
"""

import pandas as pd

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    print("\nFirst 5 records : ")
    print(df.head(5))

    print("\nLast 5 records : ")
    print(df.tail(5))

    rows, columns = df.shape
    print(f"\nTotal number of rows are {rows} and columns are {columns}")

    print("\nList of columns names : ",list(df.columns))

    print("\nData types of each column : ")
    print(df.dtypes)


if __name__ == "__main__":
    main()