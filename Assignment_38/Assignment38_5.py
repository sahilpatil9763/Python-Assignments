"""
5. Based on the dataset values, analyze whether:
• Higher StudyHours increase the chance of passing.
• Higher Attendance improves FinalResult.
  Write your observations in 4-5 lines.
"""

import pandas as pd

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    # Average StudyHours based on FinalResult
    AvgStudyHours = df.groupby("FinalResult")["StudyHours"].mean()

    # Average Attendance based on FinalResult
    AvgAttendance = df.groupby("FinalResult")["Attendance"].mean()

    print("Average StudyHours:")
    print(AvgStudyHours)

    print("\nAverage Attendance:")
    print(AvgAttendance)

if __name__ == "__main__":
    main()

"""
Based on the dataset:

Students who passed studied an average of 6.37 hours, while students who failed studied only 2.55 hours.
Students who passed had an average attendance of 86.61%, compared to 67.75% for students who failed.
This indicates that students with higher study hours are more likely to pass.
It also shows that higher attendance is associated with better academic performance and increases the likelihood of a Pass result.
Therefore, both StudyHours and Attendance have a positive relationship with the FinalResult.
"""