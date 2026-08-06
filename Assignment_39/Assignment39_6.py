"""
6. Train three Decision Tree models with:
• max_depth = 1
• max_depth = 3
• max_depth = None
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
# Function Name : CompareModels
# Description   : Train Decision Tree models with different
#                 max_depth values and compare accuracy
# ----------------------------------------------------------
def CompareModels(X_train, X_test, Y_train, Y_test):

    Depth = [1, 3, None]

    for value in Depth:

        # Create Model
        model = DecisionTreeClassifier(max_depth=value, random_state=42)

        # Train Model
        model.fit(X_train, Y_train)

        # Prediction
        Y_pred = model.predict(X_test)

        # Accuracy
        Accuracy = accuracy_score(Y_test, Y_pred)

        print("----------------------------------")
        print("Max Depth :", value)
        print(f"Accuracy  : {Accuracy * 100:.2f}%")
        print("----------------------------------")


# ----------------------------------------------------------
# Function Name : main
# Description   : Entry point of the program
# ----------------------------------------------------------
def main():

    print("-------------------------------")
    print("Decision Tree Classification")
    print("-------------------------------")

    # Step 1 : Load Dataset
    df = Import_csv()

    # Step 2 : Decide Independent and Dependent Variables
    X, Y = DecideVariables(df)

    # Step 3 : Split Dataset
    X_train, X_test, Y_train, Y_test = TrainData(X, Y)

    # Step 4 : Train Model
    CompareModels(X_train, X_test, Y_train, Y_test)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()