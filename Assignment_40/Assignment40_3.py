"""
3. Train the model using only:

• StudyHours
• Attendance

Compare the accuracy with the full-feature model
Is the model still performing well?
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
# Function Name : SelectFeatures
# Description   : Select StudyHours and Attendance
# ----------------------------------------------------------

def SelectFeatures(df):

    FeatureColumns = [

        "StudyHours",
        "Attendance"

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
# Function Name : CompareAccuracy
# Description   : Compare Full Model and Two-Feature Model
# ----------------------------------------------------------

def CompareAccuracy(OldAccuracy, NewAccuracy):

    print("\n--------------------------------")
    print("Accuracy Comparison")
    print("--------------------------------")

    print(f"Full Feature Model Accuracy : {OldAccuracy * 100:.2f}%")
    print(f"Two Feature Model Accuracy  : {NewAccuracy * 100:.2f}%")

    if OldAccuracy == NewAccuracy:

        print("\nThe model is still performing equally well.")

    elif NewAccuracy >= OldAccuracy - 0.05:

        print("\nThe model is still performing well.")

    else:

        print("\nThe model performance has decreased.")


# ----------------------------------------------------------
# Function Name : main
# Description   : Main Function
# ----------------------------------------------------------

def main():

    # ----------------------------------------
    # Full Feature Model
    # ----------------------------------------

    df = Import_csv()

    X, Y = DecideVariables(df)

    X_train, X_test, Y_train, Y_test = TrainData(X, Y)

    model = CreateModel()

    model = TrainModel(model, X_train, Y_train)

    Y_pred = PredictModel(model, X_test)

    FullAccuracy = Accuracy(Y_test, Y_pred)

    # ----------------------------------------
    # Model using only StudyHours & Attendance
    # ----------------------------------------

    X, Y = SelectFeatures(df)

    X_train, X_test, Y_train, Y_test = TrainData(X, Y)

    model = CreateModel()

    model = TrainModel(model, X_train, Y_train)

    Y_pred = PredictModel(model, X_test)

    TwoFeatureAccuracy = Accuracy(Y_test, Y_pred)

    # ----------------------------------------
    # Compare Accuracy
    # ----------------------------------------

    CompareAccuracy(FullAccuracy, TwoFeatureAccuracy)

# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()


"""
1. Compare the accuracy with the full-feature model.
The accuracy of the model trained using only StudyHours and Attendance is the same as the full-feature model.

2. Is the model still performing well?
Yes. The model is still performing well because its accuracy remains unchanged even after using only two features. This indicates that these features, especially Attendance, contain sufficient information to predict FinalResult for this dataset.
"""