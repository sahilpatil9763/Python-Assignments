"""
7. Use the trained model to predict result for a student with:
• StudyHours = 6
• Atendance = 85
• PreviousScore = 66
• AssignmentsCompleted =7
• SleepHours = 7
Will the student Pass or Fail?
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ----------------------------------------------------------
# Function Name : Import_csv
# Description   : Load the CSV dataset into a DataFrame
# ----------------------------------------------------------
def Import_csv():
    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    return df


# ----------------------------------------------------------
# Function Name : DecideVariables
# Description   : Separate Independent(X) and Dependent(Y)
#                 variables from the dataset
# ----------------------------------------------------------
def DecideVariables(df):

    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    # Independent Variables
    X = df[feature_cols]

    # Dependent Variable
    Y = df["FinalResult"]

    return X, Y


# ----------------------------------------------------------
# Function Name : TrainData
# Description   : Split the dataset into training and
#                 testing data
# ----------------------------------------------------------
def TrainData(X, Y):

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    return X_train, X_test, Y_train, Y_test


# ----------------------------------------------------------
# Function Name : CreateModel
# Description   : Create the Decision Tree model
# ----------------------------------------------------------
def CreateModel():

    model = DecisionTreeClassifier(max_depth=5)

    return model


# ----------------------------------------------------------
# Function Name : TrainModel
# Description   : Train the model using training data
# ----------------------------------------------------------
def TrainModel(model, X_train, Y_train):

    model.fit(X_train, Y_train)

    return model


# ----------------------------------------------------------
# Function Name : main
# Description   : Entry point of the program
# ----------------------------------------------------------
def main():

    print("\n-------------------------------")
    print("Decision Tree Classification")
    print("-------------------------------")

    # Step 1 : Load Dataset
    df = Import_csv()

    # Step 2 : Decide Independent and Dependent Variables
    X, Y = DecideVariables(df)

    # Step 3 : Split Dataset
    X_train, X_test, Y_train, Y_test = TrainData(X, Y)

    # Step 4 : Create Model
    model = CreateModel()

    # Step 5 : Train the Model
    model = TrainModel(model, X_train, Y_train)

    # Step 6 : New Student Data
    StudentData = pd.DataFrame({
        "StudyHours": [6],
        "Attendance": [85],
        "PreviousScore": [66],
        "AssignmentsCompleted": [7],
        "SleepHours": [7]
    })

    # Step 7 : Predict Result
    Prediction = model.predict(StudentData)

    # Step 8 : Display Result
    if Prediction[0] == 1:
        print("Prediction :", Prediction[0])
        print("The student will Pass.\n")
    else:
        print("Prediction :", Prediction[0])
        print("The student will Fail.\n")


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()