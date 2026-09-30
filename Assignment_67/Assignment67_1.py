import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Set random seed
np.random.seed(42)
tf.random.set_seed(42)

# Step 1: Create dataset
X = [
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
]

Y = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]

# Step 2: Create DataFrame
df = pd.DataFrame(X, columns=[
    "Income",
    "CreditScore",
    "LoanAmount",
    "ExistingEMI",
    "EmploymentStatus"
])

df["Approval"] = Y

# Step 3: Clean dataset
df = df.drop_duplicates()
df = df.dropna()

X = df.drop("Approval", axis=1).values
Y = df["Approval"].values

# Step 4: Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

# Step 5: Apply StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 6: Create FNN model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(5,)),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# Step 7: Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Step 8: Train model
model.fit(
    X_train,
    Y_train,
    epochs=100,
    batch_size=2,
    verbose=1
)

# Step 9: Evaluate model
loss, accuracy = model.evaluate(X_test, Y_test, verbose=0)

print("\nModel Evaluation")
print("Test Loss:", loss)
print("Test Accuracy:", accuracy * 100, "%")

# Step 10: Predict new applicant
new_applicant = np.array([[55000, 720, 400000, 10000, 1]])

new_applicant = scaler.transform(new_applicant)

prediction = model.predict(new_applicant, verbose=0)

print("\nPrediction Probability:", prediction[0][0])

if prediction[0][0] >= 0.5:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")