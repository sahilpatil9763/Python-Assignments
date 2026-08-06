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
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

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
# Function Name : MisclassifiedStudents
# Description   : Display Misclassified Students
# ----------------------------------------------------------

def MisclassifiedStudents(X_test, Y_test, Y_pred):

    print("\n--------------------------------")
    print("Misclassified Students")
    print("--------------------------------")

    Misclassified = X_test.copy()

    Misclassified["ActualResult"] = Y_test
    Misclassified["PredictedResult"] = Y_pred

    Misclassified = Misclassified[
        Misclassified["ActualResult"] != Misclassified["PredictedResult"]
    ]

    print(Misclassified)

    print("\nTotal Misclassified Students :", len(Misclassified))

    if len(Misclassified) == 0:

        print("\nPattern : No students were misclassified.")

    else:

        print("\nPattern : Misclassified students have similar feature values, making them difficult for the model to classify correctly.")


def CompareRandomState(df):

    RandomStates = [0, 10, 42]

    print("\n--------------------------------")
    print("Random State Comparison")
    print("--------------------------------")

    for State in RandomStates:

        X, Y = DecideVariables(df)

        X_train, X_test, Y_train, Y_test = TrainData(X, Y, State)

        model = CreateModel()

        model = TrainModel(model, X_train, Y_train)

        Y_pred = PredictModel(model, X_test)

        AccuracyValue = Accuracy(Y_test, Y_pred)

        print(f"Random State = {State} --> Accuracy = {AccuracyValue * 100:.2f}%")


# ----------------------------------------------------------
# Function Name : DisplayDecisionTree
# Description   : Visualize Decision Tree
# ----------------------------------------------------------

def DisplayDecisionTree(model, X):

    plt.figure(figsize=(12, 8))

    plot_tree(
        model,
        feature_names=X.columns,
        class_names=["Fail", "Pass"],
        filled=True,
        rounded=True,
        fontsize=10
    )

    plt.title("Decision Tree Visualization")

    plt.show()


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