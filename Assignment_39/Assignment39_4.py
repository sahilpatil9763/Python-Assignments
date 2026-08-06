"""
4. Generate confusion matrix using sklearn.
Display it using ConfusionMatrixDisplay.

Explain clearly:
• True Positive
• True Negative
• False Positive
• False Negative
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


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

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

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
# Function Name : PredictModel
# Description   : Predict the model using trained model
# ----------------------------------------------------------
def PredictModel(model, X_test):

    Y_pred = model.predict(X_test)

    return Y_pred


# ----------------------------------------------------------
# Function Name : CalculateAccuracy
# Description   : Calculate the accuracy of the model
# ----------------------------------------------------------

def CalculateAccuracy(Y_test, Y_pred):

    Accuracy = accuracy_score(Y_test, Y_pred)

    print(f"Model Accuracy : {Accuracy * 100}%")

    return Accuracy


# ----------------------------------------------------------
# Function Name : ConfusionMatrixDisplay
# Description   : Generate and Display Confusion Matrix
# ----------------------------------------------------------

def DisplayConfusionMatrix(Y_test, Y_pred):

    cm = confusion_matrix(Y_test, Y_pred)

    print("Confusion Matrix : ")
    print(cm)

    Display = ConfusionMatrixDisplay(confusion_matrix=cm,
                                     display_labels=["Fail", "Pass"])

    Display.plot(cmap="Blues")

    plt.title("Confusion Matrix")
    plt.show()


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

    # Step 4 : Create Model
    model = CreateModel()

    # Step 5 : Train Model
    model = TrainModel(model, X_train, Y_train)

    # Step 6 : Predict Results
    Y_pred = PredictModel(model, X_test)

    # Step 7 : Display Actual and Predicted Values
    #DisplayResult(Y_test, Y_pred)

    # Step 8 : Calculate Accuracy
    # CalculateAccuracy(Y_test, Y_pred)

    # Step 9 :
    DisplayConfusionMatrix(Y_test, Y_pred)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()


"""
Explanation :

1. True Positive (TP)
• The student actually passed.
• The model predicted Pass.

Example:
Actual : Pass
Predicted : Pass

In the above matrix:
TP = 8

2. True Negative (TN)
• The student actually failed.
• The model predicted Fail.

Example:
Actual : Fail
Predicted : Fail

In the above matrix:
TN = 5

3. False Positive (FP)
• The student actually failed.
• The model predicted Pass.

Example:
Actual : Fail
Predicted : Pass

This is called a False Positive because the model incorrectly predicted a positive (Pass).

In the matrix:
FP = 1

4. False Negative (FN)
• The student actually passed.
• The model predicted Fail.

Example:
Actual : Pass
Predicted : Fail

This is called a False Negative because the model missed a positive case.

In the matrix:
FN = 1
"""