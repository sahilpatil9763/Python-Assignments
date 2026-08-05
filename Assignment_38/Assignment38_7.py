"""
7. Create a scatter plot of:
StudyHours vs PreviousScore

Use different colors for Pass and Fail students.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    # Scatter Plot
    plt.figure(figsize=(8,6))

    for fr in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == fr]
        plt.scatter(temp["StudyHours"], temp["PreviousScore"], label = fr)

    plt.title("Student Preformance Study")

    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")

    plt.legend()
    plt.grid()
    plt.show()

    
if __name__ == "__main__":
    main()