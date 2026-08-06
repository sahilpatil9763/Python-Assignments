"""
9. Create a new column:

PerformanceIndex = (StudyHours * 2) + Attendance

Train the model including this new feature.
Does accuracy improve?
Ans : No. The accuracy does not improve. The model's accuracy remains the same after adding the PerformanceIndex feature.
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
# Function Name : TrainData
# Description   : Split Dataset
# ----------------------------------------------------------

def TrainData(X, Y, RandomState):

    X_train, X_test, Y_train, Y_test = train_test_split(

        X,
        Y,
        test_size=0.30,
        random_state=RandomState

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
# Function Name : AddPerformanceIndex
# Description   : Add PerformanceIndex Column
# ----------------------------------------------------------

def AddPerformanceIndex(df):

    NewDF = df.copy()

    NewDF["PerformanceIndex"] = (NewDF["StudyHours"] * 2) + NewDF["Attendance"]

    print("PerformanceIndex Column Added Successfully")

    return NewDF


# ----------------------------------------------------------
# Function Name : DecideVariablesWithPerformance
# Description   : Select Features with PerformanceIndex
# ----------------------------------------------------------

def DecideVariablesWithPerformance(df):

    FeatureColumns = [

        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours",
        "PerformanceIndex"

    ]

    X = df[FeatureColumns]

    Y = df["FinalResult"]

    return X, Y


# ----------------------------------------------------------
# Function Name : CompareAccuracy
# Description   : Compare Model Accuracy
# ----------------------------------------------------------

def CompareAccuracy(OldAccuracy, NewAccuracy):

    print("\n--------------------------------")
    print("Accuracy Comparison")
    print("--------------------------------")

    print(f"Original Accuracy  : {OldAccuracy * 100:.2f}%")
    print(f"New Accuracy       : {NewAccuracy * 100:.2f}%")

    if NewAccuracy > OldAccuracy:

        print("\nAccuracy Improved.")

    elif NewAccuracy == OldAccuracy:

        print("\nAccuracy Remained the Same.")

    else:

        print("\nAccuracy Decreased.")


# ----------------------------------------------------------
# Function Name : main
# Description   : Main Function
# ----------------------------------------------------------

def main():

    # ------------------------------------
    # Original Model
    # ------------------------------------

    df = Import_csv()

    X, Y = DecideVariables(df)

    X_train, X_test, Y_train, Y_test = TrainData(X, Y, 42)

    model = CreateModel()

    model = TrainModel(model, X_train, Y_train)

    Y_pred = PredictModel(model, X_test)

    OldAccuracy = Accuracy(Y_test, Y_pred)

    # ------------------------------------
    # Model with PerformanceIndex
    # ------------------------------------

    df = AddPerformanceIndex(df)

    X, Y = DecideVariablesWithPerformance(df)

    X_train, X_test, Y_train, Y_test = TrainData(X, Y, 42)

    model = CreateModel()

    model = TrainModel(model, X_train, Y_train)

    Y_pred = PredictModel(model, X_test)

    NewAccuracy = Accuracy(Y_test, Y_pred)

    # ------------------------------------
    # Compare Accuracy
    # ------------------------------------

    CompareAccuracy(OldAccuracy, NewAccuracy)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()