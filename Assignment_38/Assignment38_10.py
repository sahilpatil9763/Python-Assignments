"""
10. Plot SleepHours against FinalResult.
Does sleeping more guatantee success? Explain.
"""

import pandas as pd
import matplotlib.pyplot as plt

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    for fr in df["FinalResult"].unique():
            temp = df[df["FinalResult"] == fr]
            plt.scatter(temp["SleepHours"], temp["FinalResult"], label = fr)

    plt.title("SleepHours vs FinalResult")

    plt.xlabel("Sleep Hours")
    plt.ylabel("FinalResult")

    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()

"""
Observation :
The scatter plot shows that both Pass and Fail students have a similar range of sleep hours.
Students with higher sleep hours are found in both the Pass and Fail groups.
This indicates that sleeping more does not guarantee success.
Academic performance depends on multiple factors such as StudyHours, Attendance, PreviousScore, and AssignmentsCompleted in addition to sleep.
Therefore, sleep is important, but it is not the only factor affecting the final result.
"""