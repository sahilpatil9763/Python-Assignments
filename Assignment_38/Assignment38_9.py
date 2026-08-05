"""
9. Create a plot showing relationship between AssignmentCompleted and FinalResult.
Explain your observation.
"""

import pandas as pd
import matplotlib.pyplot as plt

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    Result = pd.crosstab(df["AssignmentsCompleted"], df["FinalResult"])

    Result.plot(kind="bar")

    plt.title("AssignmentCompleted vs FinalResult")
    plt.xlabel("Assignment Completed")
    plt.ylabel("Number of Students")
    plt.legend(["Fail", "Pass"])

    plt.show()

if __name__ == "__main__":
    main()


"""
Observation : 
Students who completed their assignments have a higher number of Pass results.
Students who did not complete their assignments have a higher proportion of Fail results.
This indicates a positive relationship between assignment completion and academic performance.
Completing assignments appears to improve the likelihood of passing the course.
Therefore, AssignmentCompleted is an important factor influencing the FinalResult.
"""