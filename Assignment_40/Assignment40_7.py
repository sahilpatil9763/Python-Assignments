"""
7. Train model using:
• random_state = 0
• random_state = 10
• random_state = 42
Compare testing accuracy.
Does the result change?
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
# Function Name : main
# Description   : Main Function
# ----------------------------------------------------------

def main():

    df = Import_csv()

    CompareRandomState(df)

# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()