"""
3: Write a Python program to calculate loss manually

Tasks:
1. Implement Mean Squared Error.
2. Implement Binary Cross Entropy.
3. Take actual and predicted values.
4. Display the calculated loss.
5. Explain which loss function is used for regression and classification.
"""

import math

# Function to calculate Mean Squared Error
def MSE(actual, predicted):
    total = 0

    for i in range(len(actual)):
        total = total + (actual[i] - predicted[i]) ** 2

    loss = total / len(actual)
    return loss


# Function to calculate Binary Cross Entropy
def BCE(actual, predicted):
    total = 0
    epsilon = 1e-15

    for i in range(len(actual)):
        p = max(epsilon, min(1 - epsilon, predicted[i]))

        total = total - (
            actual[i] * math.log(p) +
            (1 - actual[i]) * math.log(1 - p)
        )

    loss = total / len(actual)
    return loss


# Accept input from user
n = int(input("Enter number of values: "))

actual = []
predicted = []

print("Enter actual values (0 or 1 for BCE):")
for i in range(n):
    value = float(input(f"Actual value {i+1}: "))
    actual.append(value)

print("Enter predicted values (between 0 and 1):")
for i in range(n):
    value = float(input(f"Predicted value {i+1}: "))
    predicted.append(value)

# Calculate losses
mse_loss = MSE(actual, predicted)
bce_loss = BCE(actual, predicted)

# Display results
print("\nMean Squared Error:", mse_loss)
print("Binary Cross Entropy:", bce_loss)