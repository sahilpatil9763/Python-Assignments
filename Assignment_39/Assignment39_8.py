"""
8. Write a single structured Python program that performs:
    1. Dataset loading
    2. Data analysis
    3. Visualization
    4. Train-test split
    5. Model training
    6. Prediction
    7. Accuracy calculation
    8. Confusion matrix generation
    9. Final conclusion
Your code should include proper comments explaining each step.
"""


# ----------------------------------------------------------
# Import Required Libraries
# ----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay


# ----------------------------------------------------------
# Function Name : Import_csv
# Description   : Load Dataset
# ----------------------------------------------------------

def Import_csv():

    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    print("Dataset Loaded Successfully")

    return df


# ----------------------------------------------------------
# Function Name : DataAnalysis
# Description   : Display dataset information
# ----------------------------------------------------------

def DataAnalysis(df):

    print("\n------------------------------")
    print("Dataset Analysis")
    print("------------------------------")

    print("\nTotal Students :", len(df))

    print(f"Average StudyHours : {df['StudyHours'].mean():.2f}")
    print(f"Average Attendance : {df['Attendance'].mean():.2f}")
    print("Maximum PreviousScore :", df["PreviousScore"].max())
    print("Minimum SleepHours :", df["SleepHours"].min())

    print("\nFinal Result Distribution")

    print(df["FinalResult"].value_counts())

    Percentage = df["FinalResult"].value_counts(normalize=True) * 100

    print("\nPass Percentage : {:.2f}%".format(Percentage[1]))
    print("Fail Percentage : {:.2f}%".format(Percentage[0]))


# ----------------------------------------------------------
# Function Name : Visualization
# Description   : Plot Histogram
# ----------------------------------------------------------

def Visualization(df):

    plt.hist(df["StudyHours"],
             bins=6,
             edgecolor="black")

    plt.title("Histogram of StudyHours")
    plt.xlabel("StudyHours")
    plt.ylabel("Number of Students")

    plt.show()


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

    print("\nDataset Split Successfully")

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

    print("Model Created")

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

    print("Prediction Completed")

    return Y_pred


# ----------------------------------------------------------
# Function Name : DisplayPrediction
# Description   : Display Actual and Predicted Values
# ----------------------------------------------------------

def DisplayPrediction(Y_test, Y_pred):

    print("\n----------------------------------------")
    print("Actual\t\tPredicted")
    print("----------------------------------------")

    for actual, predicted in zip(Y_test, Y_pred):

        print(actual, "\t\t", predicted)


# ----------------------------------------------------------
# Function Name : Accuracy
# Description   : Calculate Model Accuracy
# ----------------------------------------------------------

def Accuracy(Y_test, Y_pred):

    AccuracyValue = accuracy_score(Y_test, Y_pred)

    print(f"\nModel Accuracy : {AccuracyValue * 100:.2f}%")

    return AccuracyValue


# ----------------------------------------------------------
# Function Name : DisplayConfusionMatrix
# Description   : Generate Confusion Matrix
# ----------------------------------------------------------

def DisplayConfusionMatrix(Y_test, Y_pred):

    CM = confusion_matrix(Y_test, Y_pred)

    print("\nConfusion Matrix")
    print(CM)

    Display = ConfusionMatrixDisplay(

        confusion_matrix=CM,
        display_labels=["Fail", "Pass"]

    )

    Display.plot(cmap="Blues")

    plt.title("Confusion Matrix")

    plt.show()


# ----------------------------------------------------------
# Function Name : PredictStudent
# Description   : Predict Result for New Student
# ----------------------------------------------------------

def PredictStudent(model):

    StudentData = pd.DataFrame({

        "StudyHours": [6],
        "Attendance": [85],
        "PreviousScore": [66],
        "AssignmentsCompleted": [7],
        "SleepHours": [7]

    })

    Prediction = model.predict(StudentData)

    print("\n--------------------------------")
    print("Prediction For New Student")
    print("--------------------------------")

    if Prediction[0] == 1:

        print("Result : PASS")

    else:

        print("Result : FAIL")


# ----------------------------------------------------------
# Function Name : Conclusion
# Description   : Display Final Conclusion
# ----------------------------------------------------------

def Conclusion(AccuracyValue):

    print("\n--------------------------------")
    print("Final Conclusion")
    print("--------------------------------")

    print(f"Model Accuracy : {AccuracyValue * 100:.2f}%")

    if AccuracyValue >= 0.90:

        print("Excellent Decision Tree Model.")

    elif AccuracyValue >= 0.80:

        print("Good Decision Tree Model.")

    elif AccuracyValue >= 0.70:

        print("Average Decision Tree Model.")

    else:

        print("Model needs improvement.")


# ----------------------------------------------------------
# Function Name : main
# Description   : Main Function
# ----------------------------------------------------------

def main():

    print("-------------------------------------------")
    print("Student Performance Prediction using")
    print("Decision Tree Classification")
    print("-------------------------------------------")

    # Step 1 : Load Dataset
    df = Import_csv()

    # Step 2 : Data Analysis
    DataAnalysis(df)

    # Step 3 : Visualization
    Visualization(df)

    # Step 4 : Independent & Dependent Variables
    X, Y = DecideVariables(df)

    # Step 5 : Split Dataset
    X_train, X_test, Y_train, Y_test = TrainData(X, Y)

    # Step 6 : Create Model
    model = CreateModel()

    # Step 7 : Train Model
    model = TrainModel(model, X_train, Y_train)

    # Step 8 : Prediction
    Y_pred = PredictModel(model, X_test)

    # Step 9 : Display Prediction
    DisplayPrediction(Y_test, Y_pred)

    # Step 10 : Accuracy
    AccuracyValue = Accuracy(Y_test, Y_pred)

    # Step 11 : Confusion Matrix
    DisplayConfusionMatrix(Y_test, Y_pred)

    # Step 12 : Predict New Student
    PredictStudent(model)

    # Step 13 : Final Conclusion
    Conclusion(AccuracyValue)


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()