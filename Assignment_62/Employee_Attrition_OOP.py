"""
Tasks :

1. Load the dataset using Pandas.
2. Display the shape, columns and first five records.
3. Check for missing values.
4. Identify numerical and categorical features.
5. Convert categorical features such as OverTime into numerical representation.
6. Convert the target Attrition into 0 and 1.
7. Separate independent and dependent variables.
8. Divide the dataset into training and testing data.
9. Apply appropriate feature scaling.
10. Design an MLP with at least two hidden layers.
11. Train the network.
12. Display the number of iterations required for training.
13. Calculate training accuracy.
14. Calculate testing accuracy.
15. Generate a confusion matrix.
16. Plot the loss curve.
17. Create a function: Predict Attrition(employee_data)
18. Test the system using at least five new employee records.
19. Explain whether the model is suffering from overfitting or underfitting 
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay



# ============================================================
# Employee Attrition Prediction System
# ============================================================

class EmployeeAttritionSystem:

    #----------------------------------------------------
    # Constructor
    #----------------------------------------------------
    def __init__(self, filename):

        self.filname = filename

        self.df = None
        self.X = None
        self.Y = None

        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None

        self.model = None

    #----------------------------------------------------
    # Step 1. Load the dataset using Pandas.
    #----------------------------------------------------

    def LoadData(self):
        self.df = pd.read_csv(self.filname)
        
        print("\n==========================================")
        print("Dataset Loaded Successfully")
        print("==========================================")

        
    #------------------------------------------------------------
    # Step 2. Display the shape, columns and first five records.
    #------------------------------------------------------------

    def ShapeofData(self):

        print("\n==================================================")
        print("Display the shape, columns and first five records")
        print("====================================================")

        print("Shape : ",self.df.shape)

        print("\nColumns : ")
        print(self.df.columns)

        print("\nFirst 5 Records : ")
        print(self.df[:5])

    #------------------------------------------------------------
    # Step 3. Check for missing values.
    #------------------------------------------------------------

    def CheckMissingValues(self):
        print("\n==========================================")
        print("Check the missing values")
        print("==========================================")

        print(self.df.isnull().sum())

    #--------------------------------------------------------
    # Step 4. Identify numerical and categorical features.
    #--------------------------------------------------------

    def IdentiifyFeatures(self):

        print("\n==========================================")
        print("Identify Features")
        print("==========================================")

        numerical_features = [
            "Age",
            "MonthlyIncome",
            "YearsAtCompany",
            "TotalWorkingYears",
            "DistanceFromHome",
            "JobSatisfaction",
            "WorkLifeBalance",
            "NumCompaniesWorked",
            "TrainingTimesLastYear"
        ]

        print("\nNeumerical Features : ")
        print(numerical_features)

        categorical_features = ["OverTime"]

        print("\nCategorical Features : ")
        print(categorical_features)

    #----------------------------------------------------
    # Step 5. Data Preprocessing
    #----------------------------------------------------

    def PreprocessData(self):

        # Convert OverTime into numerical values
        self.df["OverTime"] = self.df["OverTime"].map({"Yes" : 1, "No" : 0})

        # Convert Attrition into numerical values
        self.df["Attrition"] = self.df["Attrition"].map({"Yes" : 1, "No" : 0})

        print("\n==========================================")
        print("Data After Encoding")
        print("==========================================")

        print(self.df.head())

    #----------------------------------------------------
    # Step 6. Seperate Indepndent ad Dependent Variables
    #----------------------------------------------------

    def SplitFeatures(self):

        self.X = self.df.drop("Attrition", axis=1)
        self.Y = self.df["Attrition"]

        print("\n==========================================")
        print("Independent Variables X :")
        print("==========================================")

        print(self.X.head())

        print("\n==========================================")
        print("Dependent Variables Y :")
        print("==========================================")

        print(self.Y.head())

    #----------------------------------------------------
    # Step 7. Train Test Split
    #----------------------------------------------------

    def SplitData(self):

        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.X,
            self.Y,
            test_size=0.2,
            random_state=42,
            stratify=self.Y
        )
        
        print("\n==========================================")
        print("Training and Testing Dataset :")
        print("==========================================")

        print("\nTraining Data : ",self.X_train.head())
        print("\nTesting Data : ",self.X_test.head())

    #----------------------------------------------------
    # Step 8. Feature Scaling
    #----------------------------------------------------

    def ScaleData(self):

        self.scaler = StandardScaler()

        self.scaled_X_train = self.scaler.fit_transform(self.X_train)
        self.scaled_X_test = self.scaler.fit_transform(self.X_test)

        print("\n==========================================")
        print("Feature Scaling Done")
        print("==========================================")

    #----------------------------------------------------
    # Step 9. MLP Model Creation
    #----------------------------------------------------

    def CreateModel(self):
        self.model = MLPClassifier(
            hidden_layer_sizes=(16,8),
            random_state=42,
            activation='relu',
            solver="adam",
            max_iter=1000
        )

        print("\n==========================================")
        print("MLP Model Created")
        print("==========================================")

        print("Hidden Layer 1 : 16 neurons")
        print("Hidden Layer 2 : 8 neurons")
        print("Activation     : ReLU")
        print("Solver         : Adam")

    #----------------------------------------------------
    # Step 10. Train the Model
    #----------------------------------------------------

    def Traimodel(self):

        self.model.fit(self.scaled_X_train, self.Y_train)

        print("\n==========================================")
        print("Model Training Completed")
        print("==========================================")

        print("Number of Iterations :", self.model.n_iter_)

    #----------------------------------------------------
    # Step 11. Training accuracy
    #----------------------------------------------------

    def TrainingAccuracy(self):
        Y_pred_train = self.model.predict(self.scaled_X_train)

        AccuracyTrain = accuracy_score(self.Y_train, Y_pred_train)

        print("\n==========================================")
        print("Training Accuracy")
        print("==========================================")

        print("Training Accuracy :", AccuracyTrain * 100, "%")

        return AccuracyTrain

    #----------------------------------------------------
    # Step 12. Testing accuracy
    #----------------------------------------------------

    def TestingAccuracy(self):
        Y_pred_test = self.model.predict(self.scaled_X_test)

        AccuracyTest = accuracy_score(self.Y_test, Y_pred_test)

        print("\n==========================================")
        print("Testing Accuracy")
        print("==========================================")

        print("Training Accuracy :", AccuracyTest * 100, "%")

        return AccuracyTest

    # --------------------------------------------------------
    # Step 13 : Confusion Matrix
    # --------------------------------------------------------
    
    def ConfusionMatrix(self):

        Y_pred_test = self.model.predict(self.scaled_X_test)

        cm = confusion_matrix(
            self.Y_test,
            Y_pred_test
        )

        print("\n==========================================")
        print("Confusion Matrix")
        print("==========================================")

        print(cm)

        display = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=["Stay", "Leave"]
        )

        display.plot()

        plt.title("Employee Attrition - Confusion Matrix")

        plt.show()

    # --------------------------------------------------------
    # Step 14 : Plot Loss Curve
    # --------------------------------------------------------
    
    def LossCurve(self):

        plt.plot(self.model.loss_curve_)

        plt.title("MLP Training Loss Curve")
        plt.xlabel("Iterations")
        plt.ylabel("Loss")
        plt.grid(True)
        plt.show()

    # --------------------------------------------------------
    # Step 14 : Predict Attrition
    # --------------------------------------------------------
    
    def PredictAttrition(self, employee_data):

        # Convert input in dataframe
        employee_df = pd.DataFrame(
            [employee_data],
            columns=self.X.columns
        )

        # Scale input data
        employee_scaled = self.scaler.transform(
            employee_df
        )

        # Make prediction
        prediction = self.model.predict(
            employee_scaled
        )

        if prediction[0] == 0:

            return "Employee is likely to stay"

        else:

            return "Employee is likely to leave"

# ============================================================
# Main Program
# ============================================================

def main():
    # Create object
    obj = EmployeeAttritionSystem(
        "Employee_Attrition.csv"
    )

    # Step 1:
    obj.LoadData()

    # Step 2:
    obj.ShapeofData()

    # Step 3:
    obj.CheckMissingValues()

    # Step 4:
    obj.IdentiifyFeatures()

    # Step 5:
    obj.PreprocessData()

    # Step 6:
    obj.SplitFeatures()

    # Step 7:
    obj.SplitData()

    # Step 8:
    obj.ScaleData()

    # Step 9:
    obj.CreateModel()

    # Step 10:
    obj.Traimodel()

    # Step 11:
    train_accuracy = obj.TrainingAccuracy()

    # Step 12:
    test_accuracy = obj.TestingAccuracy()

    # Step 13:
    obj.ConfusionMatrix()

    # Step 14:
    obj.LossCurve()

    # ========================================================
    # Step 14 : Test with 5 New Employees
    # ========================================================

    print("\n==========================================")
    print("Testing 5 New Employees")
    print("==========================================")

    employees = [

        {
            "Age": 25,
            "MonthlyIncome": 30000,
            "YearsAtCompany": 1,
            "TotalWorkingYears": 2,
            "DistanceFromHome": 20,
            "JobSatisfaction": 2,
            "WorkLifeBalance": 2,
            "OverTime": 1,
            "NumCompaniesWorked": 2,
            "TrainingTimesLastYear": 2
        },

        {
            "Age": 45,
            "MonthlyIncome": 100000,
            "YearsAtCompany": 10,
            "TotalWorkingYears": 20,
            "DistanceFromHome": 5,
            "JobSatisfaction": 4,
            "WorkLifeBalance": 4,
            "OverTime": 0,
            "NumCompaniesWorked": 2,
            "TrainingTimesLastYear": 4
        },

        {
            "Age": 30,
            "MonthlyIncome": 45000,
            "YearsAtCompany": 2,
            "TotalWorkingYears": 5,
            "DistanceFromHome": 25,
            "JobSatisfaction": 2,
            "WorkLifeBalance": 2,
            "OverTime": 1,
            "NumCompaniesWorked": 4,
            "TrainingTimesLastYear": 1
        },

        {
            "Age": 38,
            "MonthlyIncome": 75000,
            "YearsAtCompany": 8,
            "TotalWorkingYears": 12,
            "DistanceFromHome": 8,
            "JobSatisfaction": 4,
            "WorkLifeBalance": 3,
            "OverTime": 0,
            "NumCompaniesWorked": 2,
            "TrainingTimesLastYear": 3
        },

        {
            "Age": 28,
            "MonthlyIncome": 35000,
            "YearsAtCompany": 1,
            "TotalWorkingYears": 4,
            "DistanceFromHome": 30,
            "JobSatisfaction": 1,
            "WorkLifeBalance": 1,
            "OverTime": 1,
            "NumCompaniesWorked": 5,
            "TrainingTimesLastYear": 1
        }
    ]


    # Predict each employee
    for i, employee in enumerate(employees, start=1):

        result = obj.PredictAttrition(
            employee
        )

        print(
            "Employee", i, ":", result
        )


    # ========================================================
    # Step 15 : Overfitting / Underfitting
    # ========================================================

    print("\n==========================================")
    print("Overfitting / Underfitting Analysis")
    print("==========================================")

    difference = abs(
        train_accuracy - test_accuracy
    )

    if difference < 0.05:

        print(
            "The training and testing accuracy are close."
        )

        print(
            "The model does not show significant overfitting."
        )

    elif train_accuracy > test_accuracy:

        print(
            "Training accuracy is significantly higher "
            "than testing accuracy."
        )

        print(
            "The model may be suffering from overfitting."
        )

    else:

        print(
            "Testing accuracy is higher than training accuracy."
        )

        print(
            "The model may be suffering from underfitting "
            "or the dataset split may have caused this difference."
        )

if __name__ == "__main__":
    main()