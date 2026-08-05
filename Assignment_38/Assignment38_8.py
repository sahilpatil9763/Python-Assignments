"""
8. Draw a boxplot for Attendance.
Identify if any outliers are present.
"""

import pandas as pd
import matplotlib.pyplot as plt

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    # Boxplot
    plt.boxplot(df["Attendance"])

    plt.title("Boxplot of Attendance")
    plt.ylabel("Attendance (%)")

    plt.show()

    Q1 = df["Attendance"].quantile(0.25)
    Q3 = df["Attendance"].quantile(0.75)

    IQR = Q3 - Q1

    LowerLimit = Q1 - 1.5 * IQR
    UpperLimit = Q3 + 1.5 * IQR

    Outliers = df[(df["Attendance"] < LowerLimit) | (df["Attendance"] > UpperLimit)]

    print("Outliers:")
    print(Outliers)
    
if __name__ == "__main__":
    main()