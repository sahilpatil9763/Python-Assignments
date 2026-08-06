"""
1. After training the Decision Tree model, use:
   model.feature_importances_
• Display importance score of each feature.
• Which feature contributes the most in predicting FinalResult?
• Which feature contributes the least?
"""


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# ----------------------------------------------------------
# Function Name : Import_csv
# Description   : Load Dataset
# ----------------------------------------------------------

def Import_csv():

    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    return df


# ----------------------------------------------------------
# Function Name : DecideVariables
# Description   : Separate Independent & Dependent Variables
# ----------------------------------------------------------

def DecideVariables(df):

    FeatureColumns = [

        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = df[FeatureColumns]

    Y = df["FinalResult"]

    return X, Y


# ----------------------------------------------------------
# Function Name : TrainData
# Description   : Split Dataset
# ----------------------------------------------------------

def TrainData(X, Y):

    X_train, X_test, Y_train, Y_test = train_test_split(

        X,
        Y,
        test_size=0.30,
        random_state=42

    )

    return X_train, X_test, Y_train, Y_test


# ----------------------------------------------------------
# Function Name : CreateModel
# Description   : Create Decision Tree Model
# ----------------------------------------------------------

def CreateModel():

    model = DecisionTreeClassifier(

        max_depth=3,
        random_state=42

    )

    return model

# ----------------------------------------------------------
# Function Name : FeatureImportance
# Description   : Display Feature Importance Scores
# ----------------------------------------------------------

def FeatureImportance(model, X):

    Importance = model.feature_importances_

    print("\n--------------------------------")
    print("Feature Importance")
    print("--------------------------------")

    for Feature, Score in zip(X.columns, Importance):
        print(f"{Feature:25} : {Score:.4f}")

    MaxIndex = Importance.argmax()
    MinIndex = Importance.argmin()

    print("\nMost Important Feature : ", X.columns[MaxIndex])
    print("Least Important Feature : ",X.columns[MinIndex])


# ----------------------------------------------------------
# Function Name : TrainModel
# Description   : Train Decision Tree
# ----------------------------------------------------------

def TrainModel(model, X_train, Y_train):

    model.fit(X_train, Y_train)

    print("Model Trained Successfully")

    return model



# ----------------------------------------------------------
# Function Name : main
# Description   : Main Function
# ----------------------------------------------------------

def main():

    df = Import_csv()

    X, Y = DecideVariables(df)

    X_train, X_test, Y_train, Y_test = TrainData(X, Y)

    model = CreateModel()

    model = TrainModel(model, X_train, Y_train)

    FeatureImportance(model, X)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()


"""
1. Which feature contributes the most in predicting FinalResult?
Answer:
Attendance contributes the most in predicting FinalResult because it has the highest feature importance score (1.0000).

2. Which feature contributes the least?
StudyHours, PreviousScore, AssignmentsCompleted, and SleepHours contribute the least because all have a feature importance score of 0.0000.
"""