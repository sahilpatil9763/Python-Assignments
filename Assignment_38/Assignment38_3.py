"""
3. Using pandas functions, calculate and display:

• Average StudyHours
• Average Attendance
• Maximum PreviousScore
• Minimum SleepHours
"""

import pandas as pd

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    AverageStudyHours = df["StudyHours"].mean()
    AverageAttendance = df["Attendance"].mean()
    MaximumPreviousScore = df["PreviousScore"].max()
    MinimumSleepHours = df["SleepHours"].min()

    print(f"Average StudyHours : {AverageStudyHours:.2f}")
    print(f"Average Attendance : {AverageAttendance:.2f}")
    print(f"Maximum PreviousScore : {MaximumPreviousScore}")
    print(f"Minimum SleepHours : {MinimumSleepHours}")

if __name__ == "__main__":
    main()