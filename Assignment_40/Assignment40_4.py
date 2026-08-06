"""
4. Create a new DataFrame with details of 5 new students.
Use the trained model to predict their results.
Display predictions clearly.
"""


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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
# Function Name : PredictNewStudents
# Description   : Predict Result of 5 New Students
# ----------------------------------------------------------

def PredictNewStudents(model):

    StudentData = pd.DataFrame({

        "StudyHours": [6, 2, 8, 5, 4],
        "Attendance": [85, 60, 95, 75, 65],
        "PreviousScore": [70, 45, 88, 60, 55],
        "AssignmentsCompleted": [8, 3, 10, 6, 5],
        "SleepHours": [7, 6, 8, 7, 5]

    })

    Prediction = model.predict(StudentData)

    StudentData["PredictedResult"] = Prediction

    StudentData["PredictedResult"] = StudentData["PredictedResult"].map({

        1: "PASS",
        0: "FAIL"

    })

    print("\n--------------------------------")
    print("Prediction For 5 New Students")
    print("--------------------------------")

    print(StudentData)


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
# Function Name : TrainModel
# Description   : Train Decision Tree
# ----------------------------------------------------------

def TrainModel(model, X_train, Y_train):

    model.fit(X_train, Y_train)

    print("Model Trained Successfully")

    return model


# ----------------------------------------------------------
# Function Name : PredictModel
# Description   : Predict Test Dataset
# ----------------------------------------------------------

def PredictModel(model, X_test):

    Y_pred = model.predict(X_test)

    return Y_pred

# ----------------------------------------------------------
# Function Name : Accuracy
# Description   : Calculate Accuracy
# ----------------------------------------------------------
def Accuracy(Y_test, Y_pred):
    AccuracyValue = accuracy_score(Y_test, Y_pred)

    return AccuracyValue


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

    Y_pred = PredictModel(model, X_test)

    FullAccuracy = Accuracy(Y_test, Y_pred)

    PredictNewStudents(model)

# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()