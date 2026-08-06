"""
2. Remove the column SleepHours from the dataset.
• Train the model again.
• Compare new accuracy with previous accuracy.
• Does removing this feature affect performance?
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
# Function Name : DecideVariablesWithoutSleepHours
# Description   : Separate Variables without SleepHours
# ----------------------------------------------------------

def DecideVariablesWithoutSleepHours(df):

    FeatureColumns = [

        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted"

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
# Function Name : RemoveFeature
# Description   : Remove SleepHours Column
# ----------------------------------------------------------

def RemoveFeature(df):

    NewDF = df.drop("SleepHours", axis=1)

    print("SleepHours Column Removed Successfully")

    return NewDF


# ----------------------------------------------------------
# Function Name : CompareAccuracy
# Description   : Compare Old and New Accuracy
# ----------------------------------------------------------
def CompareAccuracy(OldAccuracy, NewAccuracy):

    print("\n--------------------------------")
    print("Accuracy Comparison")
    print("--------------------------------")

    print(f"Previous Accuracy :{OldAccuracy * 100:.2f}%")
    print(f"New Accuracy      :{NewAccuracy * 100:.2f}%")

    print("--------------------------------")

    if OldAccuracy == NewAccuracy:
        print("\nRemoving SleepHours did not affect performance.\n")

    elif NewAccuracy > OldAccuracy:
        print("\nRemoving SleepHours improved performance.\n")

    else:
        print("\nRemoving SleepHours reduced performance.\n")


# ----------------------------------------------------------
# Function Name : main
# Description   : Main Function
# ----------------------------------------------------------

def main():

    # -----------------------------
    # Train model using all features
    # -----------------------------

    df = Import_csv()

    X, Y = DecideVariables(df)

    X_train, X_test, Y_train, Y_test = TrainData(X, Y)

    model = CreateModel()

    model = TrainModel(model, X_train, Y_train)

    Y_pred = PredictModel(model, X_test)

    OldAccuracy = Accuracy(Y_test, Y_pred)

    # -----------------------------
    # Remove SleepHours and train again
    # -----------------------------

    NewDF = RemoveFeature(df)

    X, Y = DecideVariablesWithoutSleepHours(NewDF)

    X_train, X_test, Y_train, Y_test = TrainData(X, Y)

    model = CreateModel()

    model = TrainModel(model, X_train, Y_train)

    Y_pred = PredictModel(model, X_test)

    NewAccuracy = Accuracy(Y_test, Y_pred)

    # -----------------------------
    # Compare Accuracy
    # -----------------------------

    CompareAccuracy(OldAccuracy, NewAccuracy)

# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()