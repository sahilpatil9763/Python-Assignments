"""
6. Plot a histogram of StudyHours.
Explain what the distribution tells you.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    # Histogram
    plt.hist(df["StudyHours"], bins=6, edgecolor="black")
    plt.title("Histogram of StudyHours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    plt.show()

    
if __name__ == "__main__":
    main()

"""
From your dataset:

Minimum StudyHours = 1.0
Maximum StudyHours = 8.5
Average StudyHours = 4.84 hours

Observation (4 - 5 lines):

The histogram shows that most students study around 3 to 7 hours per day.
Very few students study less than 2 hours or more than 8 hours.
The data is concentrated near the average value of 4.84 hours, indicating moderate study habits for most students.
There are no major gaps or extreme outliers in the distribution.
Overall, the distribution suggests that most students spend a moderate amount of time studying, with only a few students at the lower and upper ends of the range.
"""