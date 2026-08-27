import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)


# ----------------------------------------------------------
# Step 1 : Load the Dataset
# ----------------------------------------------------------

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

print("Shape of Dataset :", df.shape)

print("\nDataset :")
print(df)


# ----------------------------------------------------------
# Step 2 : Check Missing Values
# ----------------------------------------------------------

print("\nMissing Values :")
print(df.isnull().sum())


# ----------------------------------------------------------
# Step 3 : Separate Input and Output Variables
# ----------------------------------------------------------

X = df.drop("Fraud", axis=1)
Y = df["Fraud"]

print("\nX Shape :")
print(X.head())

print("\nY Shape :")
print(Y.head())


# ----------------------------------------------------------
# Step 4 : Split Training and Testing Data
# ----------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("\nTraining Data :", X_train.shape)
print("Testing Data  :", X_test.shape)


# ----------------------------------------------------------
# Step 5 : Decision Tree Classifier
# ----------------------------------------------------------

model_dt = DecisionTreeClassifier(
    random_state=42
)

model_dt.fit(X_train, Y_train)

Y_pred_dt = model_dt.predict(X_test)


# ----------------------------------------------------------
# Step 6 : Bagging Classifier
# ----------------------------------------------------------

model_bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=10,
    random_state=42
)

model_bagging.fit(X_train, Y_train)

Y_pred_bagging = model_bagging.predict(X_test)


# ----------------------------------------------------------
# Step 7 : Random Forest Classifier
# ----------------------------------------------------------

model_rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model_rf.fit(X_train, Y_train)

Y_pred_rf = model_rf.predict(X_test)


# ----------------------------------------------------------
# Step 8 : AdaBoost Classifier
# ----------------------------------------------------------

model_adaboost = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

model_adaboost.fit(X_train, Y_train)

Y_pred_adaboost = model_adaboost.predict(X_test)


# ----------------------------------------------------------
# Step 9 : Voting Classifier
# ----------------------------------------------------------

model_voting = VotingClassifier(
    estimators=[
        (
            "dt",
            DecisionTreeClassifier(random_state=42)
        ),

        (
            "rf",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )
        ),

        (
            "ada",
            AdaBoostClassifier(
                n_estimators=50,
                random_state=42
            )
        )
    ],
    voting="hard"
)

model_voting.fit(X_train, Y_train)

Y_pred_voting = model_voting.predict(X_test)


# ----------------------------------------------------------
# Step 10 : Function to Calculate Metrics
# ----------------------------------------------------------

def DisplayMetrics(ModelName, Y_test, Y_pred):

    accuracy = accuracy_score(Y_test, Y_pred)

    precision = precision_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    recall = recall_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    f1 = f1_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    cm = confusion_matrix(
        Y_test,
        Y_pred
    )

    print("\n======================================")
    print(ModelName)
    print("======================================")

    print("Accuracy  :", accuracy * 100, "%")
    print("Precision :", precision * 100, "%")
    print("Recall    :", recall * 100, "%")
    print("F1 Score  :", f1 * 100, "%")

    print("\nConfusion Matrix :")
    print(cm)

    return accuracy, precision, recall, f1


# ----------------------------------------------------------
# Step 11 : Evaluate All Models
# ----------------------------------------------------------

dt_metrics = DisplayMetrics(
    "Decision Tree",
    Y_test,
    Y_pred_dt
)

bagging_metrics = DisplayMetrics(
    "Bagging",
    Y_test,
    Y_pred_bagging
)

rf_metrics = DisplayMetrics(
    "Random Forest",
    Y_test,
    Y_pred_rf
)

adaboost_metrics = DisplayMetrics(
    "AdaBoost",
    Y_test,
    Y_pred_adaboost
)

voting_metrics = DisplayMetrics(
    "Voting Classifier",
    Y_test,
    Y_pred_voting
)


# ----------------------------------------------------------
# Step 12 : Final Comparison
# ----------------------------------------------------------

comparison = pd.DataFrame({

    "Algorithm": [
        "Decision Tree",
        "Bagging",
        "Random Forest",
        "AdaBoost",
        "Voting"
    ],

    "Accuracy": [
        dt_metrics[0] * 100,
        bagging_metrics[0] * 100,
        rf_metrics[0] * 100,
        adaboost_metrics[0] * 100,
        voting_metrics[0] * 100
    ],

    "Precision": [
        dt_metrics[1] * 100,
        bagging_metrics[1] * 100,
        rf_metrics[1] * 100,
        adaboost_metrics[1] * 100,
        voting_metrics[1] * 100
    ],

    "Recall": [
        dt_metrics[2] * 100,
        bagging_metrics[2] * 100,
        rf_metrics[2] * 100,
        adaboost_metrics[2] * 100,
        voting_metrics[2] * 100
    ],

    "F1": [
        dt_metrics[3] * 100,
        bagging_metrics[3] * 100,
        rf_metrics[3] * 100,
        adaboost_metrics[3] * 100,
        voting_metrics[3] * 100
    ]
})


# ----------------------------------------------------------
# Step 13 : Display Final Comparison
# ----------------------------------------------------------

print("\n\n==============================================")
print("          FINAL MODEL COMPARISON")
print("==============================================")

print(
    comparison.to_string(
        index=False,
        formatters={
            "Accuracy": "{:.2f}%".format,
            "Precision": "{:.2f}%".format,
            "Recall": "{:.2f}%".format,
            "F1": "{:.2f}%".format
        }
    )
)


# ----------------------------------------------------------
# Step 14 : Find Best Model
# ----------------------------------------------------------

best_model = comparison.loc[
    comparison["F1"].idxmax()
]

print("\n======================================")
print("           BEST MODEL")
print("======================================")

print("Algorithm :", best_model["Algorithm"])
print("F1 Score  :", round(best_model["F1"], 2), "%")