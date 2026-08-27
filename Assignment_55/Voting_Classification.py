import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier


# ----------------------------------------------------------
# Step 1 : Load the Dataset
# ----------------------------------------------------------

df = pd.read_csv("Customer_Loan_Approval.csv")

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

X = df.drop("LoanApproved", axis=1)
Y = df["LoanApproved"]

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
    random_state=42
)

print("\nTraining Data :", X_train.shape)
print("Testing Data  :", X_test.shape)


# ----------------------------------------------------------
# Step 5 : Feature Scaling
# ----------------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ----------------------------------------------------------
# Step 6 : Train Logistic Regression
# ----------------------------------------------------------

model_lr = LogisticRegression()

model_lr.fit(X_train_scaled, Y_train)

Y_pred_lr = model_lr.predict(X_test_scaled)

accuracy_lr = accuracy_score(Y_test, Y_pred_lr)

print("\nLogistic Regression Accuracy :",accuracy_lr * 100, "%")


# ----------------------------------------------------------
# Step 7 : Train Decision Tree
# ----------------------------------------------------------

model_dt = DecisionTreeClassifier(
    random_state=42
)

model_dt.fit(X_train, Y_train)

Y_pred_dt = model_dt.predict(X_test)

accuracy_dt = accuracy_score(Y_test, Y_pred_dt)

print("Decision Tree Accuracy       :",accuracy_dt * 100, "%")


# ----------------------------------------------------------
# Step 8 : Train KNN
# ----------------------------------------------------------

model_knn = KNeighborsClassifier(
    n_neighbors=5
)

model_knn.fit(X_train_scaled, Y_train)

Y_pred_knn = model_knn.predict(X_test_scaled)

accuracy_knn = accuracy_score(Y_test, Y_pred_knn)

print("KNN Accuracy                 :",accuracy_knn * 100, "%")


# ----------------------------------------------------------
# Step 9 : Create Hard Voting Classifier
# ----------------------------------------------------------

hard_voting = VotingClassifier(
    estimators=[
        ("logistic", LogisticRegression()),
        ("decision_tree", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ],
    voting="hard"
)

hard_voting.fit(X_train_scaled, Y_train)

Y_pred_hard = hard_voting.predict(X_test_scaled)

accuracy_hard = accuracy_score(
    Y_test,
    Y_pred_hard
)

print("Hard Voting Accuracy        :",accuracy_hard * 100, "%")


# ----------------------------------------------------------
# Step 10 : Create Soft Voting Classifier
# ----------------------------------------------------------

soft_voting = VotingClassifier(
    estimators=[
        ("logistic", LogisticRegression()),
        ("decision_tree", DecisionTreeClassifier(random_state=42)),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ],
    voting="soft"
)

soft_voting.fit(X_train_scaled, Y_train)

Y_pred_soft = soft_voting.predict(X_test_scaled)

accuracy_soft = accuracy_score(
    Y_test,
    Y_pred_soft
)

print("Soft Voting Accuracy        :",accuracy_soft * 100, "%")


# ----------------------------------------------------------
# Step 11 : Compare All Models
# ----------------------------------------------------------

print("\n======================================")
print("       MODEL ACCURACY COMPARISON")
print("======================================")

print("Logistic Regression :", accuracy_lr * 100, "%")
print("Decision Tree       :", accuracy_dt * 100, "%")
print("KNN                 :", accuracy_knn * 100, "%")
print("Hard Voting         :", accuracy_hard * 100, "%")
print("Soft Voting         :", accuracy_soft * 100, "%")


# ----------------------------------------------------------
# Step 12 : Display Comparison in Table
# ----------------------------------------------------------

comparison = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],

    "Accuracy": [
        accuracy_lr * 100,
        accuracy_dt * 100,
        accuracy_knn * 100,
        accuracy_hard * 100,
        accuracy_soft * 100
    ]
})

print("\nFinal Comparison :")
print(comparison.to_string(index=False))