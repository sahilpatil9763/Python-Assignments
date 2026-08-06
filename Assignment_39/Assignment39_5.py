"""
5. Calculate:
• Training accuracy
• Testing accuracy
Compare both and comment whether the model is overfitting or underfitting.
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
# Function Name : CompareAccuracy
# Description   : Calculate Training and Testing Accuracy
# ----------------------------------------------------------
def CompareAccuracy(model, X_train, X_test, Y_train, Y_test):

    # Prediction on Training Data
    TrainPrediction = model.predict(X_train)

    # Prediction on Testing Data
    TestPrediction = model.predict(X_test)

    # Calculate Accuracy
    TrainAccuracy = accuracy_score(Y_train, TrainPrediction)
    TestAccuracy = accuracy_score(Y_test, TestPrediction)

    print(f"Training Accuracy : {TrainAccuracy * 100:.2f}%")
    print(f"Testing Accuracy  : {TestAccuracy * 100:.2f}%")

    # Compare Accuracy
    if TrainAccuracy > TestAccuracy:
        print("\nObservation : Model is Overfitting.")
    elif TrainAccuracy < TestAccuracy:
        print("\nObservation : Model is Underfitting.")
    else:
        print("\nObservation : Model is well fitted.")

    return TrainAccuracy, TestAccuracy

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

    # Step 7 : Display Actual and Predicted Values
    CompareAccuracy(model, X_train, X_test, Y_train, Y_test)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------
if __name__ == "__main__":
    main()