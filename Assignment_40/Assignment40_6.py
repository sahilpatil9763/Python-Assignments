"""
6. Identify students where:
y_test != y_pred
• Display those rows.
• How many students were misclassified?
• What common pattern do you observe?
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

    # Display Misclassified Students
    MisclassifiedStudents(X_test, Y_test, Y_pred)

# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()