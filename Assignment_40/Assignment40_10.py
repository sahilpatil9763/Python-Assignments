"""
10. Train model with:
• max_depth = None
Calculate:
• Training accuracy
• Testing accuracy
If training accuracy is 100% but testing accuracy is lower, explain why this happens.
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

        max_depth=None,
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
# Function Name : TrainingAccuracy
# Description   : Calculate Training Accuracy
# ----------------------------------------------------------

def TrainingAccuracy(model, X_train, Y_train):

    Y_train_pred = model.predict(X_train)

    TrainAccuracy = accuracy_score(Y_train, Y_train_pred)

    print(f"\nTraining Accuracy : {TrainAccuracy * 100:.2f}%")

    return TrainAccuracy



# ----------------------------------------------------------
# Function Name : main
# Description   : Main Function
# ----------------------------------------------------------

def main():

    df = Import_csv()

    X, Y = DecideVariables(df)

    X_train, X_test, Y_train, Y_test = TrainData(X, Y, 42)

    model = CreateModel()

    model = TrainModel(model, X_train, Y_train)

    TrainAccuracy = TrainingAccuracy(model, X_train, Y_train)

    Y_pred = PredictModel(model, X_test)

    TestAccuracy = Accuracy(Y_test, Y_pred)

    print(f"Testing Accuracy : {TestAccuracy * 100:.2f}%")

    if TrainAccuracy == 1.0 and TestAccuracy < TrainAccuracy:

        print("The model is overfitting.")
        print("It has memorized the training data but does not generalize well to unseen data.")

    else:

        print("The model is performing well without significant overfitting.")
        

# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()