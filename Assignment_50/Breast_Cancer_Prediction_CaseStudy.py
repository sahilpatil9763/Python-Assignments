"""
"Breast Cancer Prediction"

Objective :

1. Load and explore the dataset.
2. Perform data preprocessing steps:
    • Handle missing values (if any)
    • Normalize or scale features
3. Perform exploratory data analysis (EDA):
    • Summary statistics
    • Visualization of feature correlations
4. Split the dataset into training and testing sets.
5. Build a machine learning classification model to predict tumor type.
6. Evaluate the model using:
    • Accuracy
    ° Confusion Matrix
    • Precision, Recall, F1-Sc
7. Provide your observations and conclusions.

Expected Deliverables
Code File:
    • Data loading
    • Preprocessing
    • Model building
    • Evaluation
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)


# ----------------------------------------------------------
# Step 1: Load Dataset
# ----------------------------------------------------------

def LoadData():

    DataPath = "breast-cancer-wisconsin.csv"

    df = pd.read_csv(DataPath)

    print("Dataset Loaded Successfully")
    print("Shape of Dataset:", df.shape)

    return df


# ----------------------------------------------------------
# Step 2: Data Preprocessing
# ----------------------------------------------------------

def PreprocessData(df):

    print("\nMissing Values Before Preprocessing:")
    print(df.isnull().sum())

    # Replace '?' with NaN
    df["BareNuclei"] = df["BareNuclei"].replace("?", pd.NA)

    # Convert BareNuclei into numeric format
    df["BareNuclei"] = pd.to_numeric(
        df["BareNuclei"],
        errors="coerce"
    )

    # Fill missing values with median
    df["BareNuclei"] = df["BareNuclei"].fillna(
        df["BareNuclei"].median()
    )

    print("\nMissing Values After Preprocessing:")
    print(df.isnull().sum())

    return df


# ----------------------------------------------------------
# Step 3: Exploratory Data Analysis
# ----------------------------------------------------------

def AnalyzeData(df):

    print("\nFirst 5 Records:")
    print(df.head())

    print("\nDataset Information:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())

    print("\nCancer Type Distribution:")
    print(df["CancerType"].value_counts())

    # Correlation Matrix
    plt.figure(figsize=(12, 8))

    sns.heatmap(
        df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Feature Correlation Matrix")
    plt.tight_layout()
    plt.show()

    # Cancer Type Distribution
    plt.figure(figsize=(6, 4))

    sns.countplot(
        x="CancerType",
        data=df
    )

    plt.title("Cancer Type Distribution")
    plt.xlabel("Cancer Type")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.show()


# ----------------------------------------------------------
# Step 4: Prepare Features and Target
# ----------------------------------------------------------

def PrepareData(df):

    # CodeNumber is an ID, so it is not used as a feature
    X = df.drop(
        ["CodeNumber", "CancerType"],
        axis=1
    )

    y = df["CancerType"]

    # Convert target:
    # 2 -> 0 (Benign)
    # 4 -> 1 (Malignant)
    y = y.map({
        2: 0,
        4: 1
    })

    return X, y


# ----------------------------------------------------------
# Step 5: Train-Test Split
# ----------------------------------------------------------

def SplitData(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("\nTraining Records:", X_train.shape[0])
    print("Testing Records:", X_test.shape[0])

    return X_train, X_test, y_train, y_test


# ----------------------------------------------------------
# Step 6: Feature Scaling
# ----------------------------------------------------------

def ScaleData(X_train, X_test):

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test


# ----------------------------------------------------------
# Step 7: Model Building
# ----------------------------------------------------------

def TrainModel(X_train, y_train):

    model = LogisticRegression(
        random_state=42,
        max_iter=1000
    )

    model.fit(
        X_train,
        y_train
    )

    print("\nModel Trained Successfully")

    return model


# ----------------------------------------------------------
# Step 8: Model Evaluation
# ----------------------------------------------------------

def EvaluateModel(model, X_test, y_test):

    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    # Precision
    precision = precision_score(
        y_test,
        y_pred
    )

    # Recall
    recall = recall_score(
        y_test,
        y_pred
    )

    # F1 Score
    f1 = f1_score(
        y_test,
        y_pred
    )

    # Confusion Matrix
    cm = confusion_matrix(
        y_test,
        y_pred
    )

    print("\n-----------------------------")
    print("Model Evaluation")
    print("-----------------------------")

    print("Accuracy :", accuracy * 100, "%")
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1-Score :", f1)

    print("\nConfusion Matrix:")
    print(cm)

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=[
                "Benign",
                "Malignant"
            ]
        )
    )

    # Display Confusion Matrix
    plt.figure(figsize=(6, 5))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=[
            "Benign",
            "Malignant"
        ],
        yticklabels=[
            "Benign",
            "Malignant"
        ]
    )

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()


# ----------------------------------------------------------
# Main Function
# ----------------------------------------------------------

def main():

    # Load dataset
    df = LoadData()

    # Preprocess dataset
    df = PreprocessData(df)

    # Exploratory Data Analysis
    AnalyzeData(df)

    # Prepare features and target
    X, y = PrepareData(df)

    # Train-test split
    X_train, X_test, y_train, y_test = SplitData(
        X,
        y
    )

    # Feature scaling
    X_train, X_test = ScaleData(
        X_train,
        X_test
    )

    # Train model
    model = TrainModel(
        X_train,
        y_train
    )

    # Evaluate model
    EvaluateModel(
        model,
        X_test,
        y_test
    )


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":
    main()