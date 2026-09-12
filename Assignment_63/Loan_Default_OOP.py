import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    ConfusionMatrixDisplay
)


# ============================================================
# Loan Default Prediction System
# ============================================================

class LoanDefaultSystem:

    # --------------------------------------------------------
    # Constructor
    # --------------------------------------------------------
    def __init__(self, filename):

        self.filename = filename

        self.df = None

        self.X = None
        self.y = None

        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

        self.scaler = StandardScaler()

        self.model = None


    # --------------------------------------------------------
    # 1. Load Dataset
    # --------------------------------------------------------
    def LoadData(self):

        self.df = pd.read_csv(self.filename)

        print("\n==========================================")
        print("DATASET LOADED")
        print("==========================================")

        print("Shape :", self.df.shape)

        print("\nColumns :")
        print(self.df.columns.tolist())

        print("\nFirst 5 Records :")
        print(self.df.head())


    # --------------------------------------------------------
    # 2. Exploratory Data Analysis
    # --------------------------------------------------------
    def ExploreData(self):

        print("\n==========================================")
        print("EXPLORATORY DATA ANALYSIS")
        print("==========================================")

        print("\nDataset Information :")
        print(self.df.info())

        print("\nStatistical Information :")
        print(self.df.describe())

        print("\nUnique Values :")

        for column in self.df.columns:

            print(
                column,
                ":",
                self.df[column].nunique()
            )


    # --------------------------------------------------------
    # 3. Check Missing Values
    # --------------------------------------------------------
    def CheckMissingValues(self):

        print("\n==========================================")
        print("MISSING VALUES")
        print("==========================================")

        missing = self.df.isnull().sum()

        print(missing)

        if missing.sum() == 0:

            print("\nNo missing values found.")

        else:

            print("\nMissing values are present.")


    # --------------------------------------------------------
    # 4. Check Target Class Balance
    # --------------------------------------------------------
    def CheckClassBalance(self):

        print("\n==========================================")
        print("TARGET CLASS BALANCE")
        print("==========================================")

        print(
            self.df["Default"].value_counts()
        )

        print("\nPercentage :")

        print(
            self.df["Default"]
            .value_counts(normalize=True) * 100
        )

        print("\nClass 0 = Low default risk")
        print("Class 1 = High default risk")

        print(
            "\nThe classes are not perfectly balanced, "
            "so stratified splitting should be used."
        )


    # --------------------------------------------------------
    # 5. Encode Categorical Variables
    # --------------------------------------------------------
    def EncodeData(self):

        print("\n==========================================")
        print("ENCODING CATEGORICAL VARIABLES")
        print("==========================================")

        # PreviousDefault
        self.df["PreviousDefault"] = self.df[
            "PreviousDefault"
        ].map({
            "No": 0,
            "Yes": 1
        })


        # HomeOwnership
        self.df = pd.get_dummies(
            self.df,
            columns=["HomeOwnership"],
            dtype=int
        )


        print("\nData after encoding :")

        print(self.df.head())


    # --------------------------------------------------------
    # 6. Separate X and y
    # --------------------------------------------------------
    def SeparateData(self):

        self.X = self.df.drop(
            "Default",
            axis=1
        )

        self.y = self.df["Default"]


        print("\n==========================================")
        print("X AND y")
        print("==========================================")

        print("\nIndependent Variables X :")

        print(self.X.head())

        print("\nDependent Variable y :")

        print(self.y.head())


    # --------------------------------------------------------
    # 7. Train Test Split
    # --------------------------------------------------------
    def SplitData(self):

        self.X_train, self.X_test, \
        self.y_train, self.y_test = train_test_split(

            self.X,
            self.y,

            test_size=0.2,

            random_state=42,

            # Important because target classes
            # are not perfectly balanced
            stratify=self.y
        )


        print("\n==========================================")
        print("TRAIN TEST SPLIT")
        print("==========================================")

        print(
            "Training Data :",
            self.X_train.shape
        )

        print(
            "Testing Data  :",
            self.X_test.shape
        )


        print("\nTraining Target Distribution :")

        print(
            self.y_train.value_counts()
        )

        print("\nTesting Target Distribution :")

        print(
            self.y_test.value_counts()
        )


    # --------------------------------------------------------
    # 8. Feature Scaling
    # --------------------------------------------------------
    def ScaleData(self):

        self.X_train = self.scaler.fit_transform(
            self.X_train
        )

        self.X_test = self.scaler.transform(
            self.X_test
        )


        print("\n==========================================")
        print("FEATURE SCALING")
        print("==========================================")

        print(
            "StandardScaler applied successfully."
        )


    # --------------------------------------------------------
    # 9. Create MLP Model
    # --------------------------------------------------------
    def CreateModel(self):

        self.model = MLPClassifier(

            hidden_layer_sizes=(32, 16),

            activation="relu",

            solver="adam",

            max_iter=1000,

            random_state=42
        )


        print("\n==========================================")
        print("MLP MODEL")
        print("==========================================")

        print(
            "Hidden Layers : (32, 16)"
        )

        print(
            "Activation : ReLU"
        )

        print(
            "Solver : Adam"
        )

        print(
            "Maximum Iterations : 1000"
        )


    # --------------------------------------------------------
    # 10. Train Model
    # --------------------------------------------------------
    def TrainModel(self):

        print("\n==========================================")
        print("MODEL TRAINING")
        print("==========================================")

        self.model.fit(
            self.X_train,
            self.y_train
        )

        print(
            "Model trained successfully."
        )

        print(
            "Iterations Required :",
            self.model.n_iter_
        )


    # --------------------------------------------------------
    # 11. Calculate Accuracy
    # --------------------------------------------------------
    def CalculateAccuracy(self):

        train_prediction = self.model.predict(
            self.X_train
        )

        test_prediction = self.model.predict(
            self.X_test
        )


        train_accuracy = accuracy_score(
            self.y_train,
            train_prediction
        )

        test_accuracy = accuracy_score(
            self.y_test,
            test_prediction
        )


        print("\n==========================================")
        print("ACCURACY")
        print("==========================================")

        print(
            "Training Accuracy :",
            train_accuracy * 100,
            "%"
        )

        print(
            "Testing Accuracy  :",
            test_accuracy * 100,
            "%"
        )

        return train_accuracy, test_accuracy


    # --------------------------------------------------------
    # 12. Confusion Matrix
    # --------------------------------------------------------
    def ConfusionMatrix(self):

        prediction = self.model.predict(
            self.X_test
        )

        cm = confusion_matrix(
            self.y_test,
            prediction
        )


        print("\n==========================================")
        print("CONFUSION MATRIX")
        print("==========================================")

        print(cm)


        display = ConfusionMatrixDisplay(

            confusion_matrix=cm,

            display_labels=[
                "Low Risk",
                "High Risk"
            ]
        )


        display.plot()

        plt.title(
            "Loan Default Confusion Matrix"
        )

        plt.show()


    # --------------------------------------------------------
    # 13. Classification Report
    # --------------------------------------------------------
    def ClassificationReport(self):

        prediction = self.model.predict(
            self.X_test
        )


        print("\n==========================================")
        print("CLASSIFICATION REPORT")
        print("==========================================")


        print(
            classification_report(
                self.y_test,
                prediction,
                target_names=[
                    "Low Risk",
                    "High Risk"
                ]
            )
        )


    # --------------------------------------------------------
    # 14. Precision Recall F1 Score
    # --------------------------------------------------------
    def CalculateMetrics(self):

        prediction = self.model.predict(
            self.X_test
        )


        precision = precision_score(
            self.y_test,
            prediction
        )

        recall = recall_score(
            self.y_test,
            prediction
        )

        f1 = f1_score(
            self.y_test,
            prediction
        )


        print("\n==========================================")
        print("PRECISION / RECALL / F1-SCORE")
        print("==========================================")

        print(
            "Precision :",
            precision
        )

        print(
            "Recall    :",
            recall
        )

        print(
            "F1-Score  :",
            f1
        )


    # --------------------------------------------------------
    # 15. Plot Training Loss
    # --------------------------------------------------------
    def PlotLoss(self):

        plt.plot(
            self.model.loss_curve_
        )

        plt.xlabel(
            "Iterations"
        )

        plt.ylabel(
            "Loss"
        )

        plt.title(
            "MLP Training Loss Curve"
        )

        plt.grid()

        plt.show()


    # --------------------------------------------------------
    # 16. Predict New Applicant
    # --------------------------------------------------------
    def PredictLoanDefault(
        self,
        applicant
    ):

        applicant_df = pd.DataFrame(
            [applicant]
        )


        # Encode PreviousDefault
        applicant_df[
            "PreviousDefault"
        ] = applicant_df[
            "PreviousDefault"
        ].map({
            "No": 0,
            "Yes": 1
        })


        # Encode HomeOwnership
        applicant_df = pd.get_dummies(

            applicant_df,

            columns=[
                "HomeOwnership"
            ],

            dtype=int
        )


        # Make sure the applicant has
        # exactly the same columns as X
        applicant_df = applicant_df.reindex(

            columns=self.X.columns,

            fill_value=0
        )


        # Scale
        applicant_scaled = self.scaler.transform(
            applicant_df
        )


        # Prediction
        prediction = self.model.predict(
            applicant_scaled
        )


        if prediction[0] == 0:

            return "Low default risk"

        else:

            return "High default risk"


    # --------------------------------------------------------
    # 17. Hyperparameter Experiment - Activation
    # --------------------------------------------------------
    def ActivationExperiment(self):

        print("\n==========================================")
        print("ACTIVATION FUNCTION EXPERIMENT")
        print("==========================================")


        activations = [
            "identity",
            "logistic",
            "tanh",
            "relu"
        ]


        for activation in activations:

            model = MLPClassifier(

                hidden_layer_sizes=(32, 16),

                activation=activation,

                solver="adam",

                max_iter=1000,

                random_state=42
            )


            model.fit(
                self.X_train,
                self.y_train
            )


            prediction = model.predict(
                self.X_test
            )


            accuracy = accuracy_score(
                self.y_test,
                prediction
            )


            print(
                activation,
                ":",
                accuracy * 100,
                "%"
            )


    # --------------------------------------------------------
    # 18. Hyperparameter Experiment - Hidden Layers
    # --------------------------------------------------------
    def HiddenLayerExperiment(self):

        print("\n==========================================")
        print("HIDDEN LAYER EXPERIMENT")
        print("==========================================")


        architectures = [

            (10,),

            (20, 10),

            (50, 25),

            (100, 50, 25)

        ]


        for architecture in architectures:

            model = MLPClassifier(

                hidden_layer_sizes=architecture,

                activation="relu",

                solver="adam",

                max_iter=1000,

                random_state=42
            )


            model.fit(
                self.X_train,
                self.y_train
            )


            prediction = model.predict(
                self.X_test
            )


            accuracy = accuracy_score(
                self.y_test,
                prediction
            )


            print(
                architecture,
                ":",
                accuracy * 100,
                "%"
            )


    # --------------------------------------------------------
    # 19. Learning Rate Experiment
    # --------------------------------------------------------
    def LearningRateExperiment(self):

        print("\n==========================================")
        print("LEARNING RATE EXPERIMENT")
        print("==========================================")


        learning_rates = [

            0.001,

            0.01,

            0.05,

            0.1

        ]


        for rate in learning_rates:

            model = MLPClassifier(

                hidden_layer_sizes=(32, 16),

                activation="relu",

                solver="adam",

                learning_rate_init=rate,

                max_iter=1000,

                random_state=42
            )


            model.fit(
                self.X_train,
                self.y_train
            )


            prediction = model.predict(
                self.X_test
            )


            accuracy = accuracy_score(
                self.y_test,
                prediction
            )


            print(
                "Learning Rate",
                rate,
                ":",
                accuracy * 100,
                "%"
            )


# ============================================================
# Main Function
# ============================================================

def main():

    # Create object
    obj = LoanDefaultSystem(
        "Loan_Default.csv"
    )


    # 1. Load data
    obj.LoadData()


    # 2. Exploratory analysis
    obj.ExploreData()


    # 3. Missing values
    obj.CheckMissingValues()


    # 4. Class balance
    obj.CheckClassBalance()


    # 5. Encoding
    obj.EncodeData()


    # 6. X and y
    obj.SeparateData()


    # 7. Train/Test split
    obj.SplitData()


    # 8. Scaling
    obj.ScaleData()


    # 9. Create MLP
    obj.CreateModel()


    # 10. Train
    obj.TrainModel()


    # 11. Accuracy
    obj.CalculateAccuracy()


    # 12. Confusion Matrix
    obj.ConfusionMatrix()


    # 13. Classification Report
    obj.ClassificationReport()


    # 14. Precision / Recall / F1
    obj.CalculateMetrics()


    # 15. Loss Curve
    obj.PlotLoss()


    # ========================================================
    # Test New Loan Applicants
    # ========================================================

    print("\n==========================================")
    print("NEW LOAN APPLICANTS")
    print("==========================================")


    applicants = [

        {
            "Age": 25,
            "Income": 400000,
            "LoanAmount": 200000,
            "CreditScore": 750,
            "EmploymentYears": 3,
            "ExistingLoans": 1,
            "MonthlyDebt": 10000,
            "LoanTerm": 24,
            "PreviousDefault": "No",
            "HomeOwnership": "Own"
        },

        {
            "Age": 45,
            "Income": 800000,
            "LoanAmount": 500000,
            "CreditScore": 720,
            "EmploymentYears": 15,
            "ExistingLoans": 2,
            "MonthlyDebt": 20000,
            "LoanTerm": 36,
            "PreviousDefault": "No",
            "HomeOwnership": "Mortgage"
        },

        {
            "Age": 30,
            "Income": 300000,
            "LoanAmount": 900000,
            "CreditScore": 580,
            "EmploymentYears": 4,
            "ExistingLoans": 4,
            "MonthlyDebt": 40000,
            "LoanTerm": 48,
            "PreviousDefault": "Yes",
            "HomeOwnership": "Rent"
        },

        {
            "Age": 50,
            "Income": 900000,
            "LoanAmount": 300000,
            "CreditScore": 780,
            "EmploymentYears": 20,
            "ExistingLoans": 1,
            "MonthlyDebt": 12000,
            "LoanTerm": 24,
            "PreviousDefault": "No",
            "HomeOwnership": "Own"
        },

        {
            "Age": 28,
            "Income": 350000,
            "LoanAmount": 700000,
            "CreditScore": 600,
            "EmploymentYears": 2,
            "ExistingLoans": 3,
            "MonthlyDebt": 35000,
            "LoanTerm": 60,
            "PreviousDefault": "Yes",
            "HomeOwnership": "Rent"
        }
    ]


    for i, applicant in enumerate(
        applicants,
        start=1
    ):

        result = obj.PredictLoanDefault(
            applicant
        )

        print(
            "Applicant",
            i,
            ":",
            result
        )


    # ========================================================
    # Hyperparameter Experiments
    # ========================================================

    obj.ActivationExperiment()

    obj.HiddenLayerExperiment()

    obj.LearningRateExperiment()


# ============================================================
# Program Execution
# ============================================================

if __name__ == "__main__":

    main()