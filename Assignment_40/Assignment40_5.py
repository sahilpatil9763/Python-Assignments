"""
5. Without using accuracy_score, manually calculate accuracy:
Verify whether it matches sklearn accuracy.
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
# Function Name : ManualAccuracy
# Description   : Calculate Accuracy Manually
# ----------------------------------------------------------

def ManualAccuracy(Y_test, Y_pred):

    Correct = 0
    Total = len(Y_test)

    for Actual, Predicted in zip(Y_test, Y_pred):

        if Actual == Predicted:

            Correct = Correct + 1

    Accuracy = Correct / Total

    print(f"\nManual Accuracy : {Accuracy * 100:.2f}%")

    return Accuracy


# ----------------------------------------------------------
# Function Name : VerifyAccuracy
# Description   : Compare Manual and Sklearn Accuracy
# ----------------------------------------------------------

def VerifyAccuracy(SklearnAccuracy, ManualAccuracy):

    print(f"Sklearn Accuracy : {SklearnAccuracy * 100:.2f}%")

    if SklearnAccuracy == ManualAccuracy:

        print("\nBoth accuracies are the same.")

    else:

        print("\nAccuracies do not match.")


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

    # Predict Test Data
    Y_pred = PredictModel(model, X_test)

    # Accuracy using sklearn
    SklearnAccuracy = Accuracy(Y_test, Y_pred)

    # Manual Accuracy
    ManualAcc = ManualAccuracy(Y_test, Y_pred)

    # Compare Both
    VerifyAccuracy(SklearnAccuracy, ManualAcc)

# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()