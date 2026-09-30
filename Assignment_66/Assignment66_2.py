"""
2: Write a Python program to demonstrate different activation functions.

Functions to implement:
1. Sigmoid
2. ReLU
3. Tanh

Tasks:
1. Accept input values from -10 to 10.
2. Plot all activation functions using Matplotlib.
3. Explain the use of each activation function.
"""

import numpy as np
import matplotlib.pyplot as plt

# Accept input from user
start = float(input("Enter starting value (-10 to 10): "))
end = float(input("Enter ending value (-10 to 10): "))

# Validate input
if start < -10 or end > 10 or start >= end:
    print("Invalid input! Enter values between -10 and 10.")

else:
    # Generate input values
    x = np.linspace(start, end, 100)

    # Sigmoid activation function
    sigmoid = 1 / (1 + np.exp(-x))

    # ReLU activation function
    relu = np.maximum(0, x)

    # Tanh activation function
    tanh = np.tanh(x)

    # Plot activation functions
    plt.figure(figsize=(10, 6))

    plt.plot(x, sigmoid, label="Sigmoid")
    plt.plot(x, relu, label="ReLU")
    plt.plot(x, tanh, label="Tanh")

    plt.title("Activation Functions")
    plt.xlabel("Input Values")
    plt.ylabel("Output Values")

    plt.legend()
    plt.grid()

    plt.show()

"""
Explanation of Activation Functions

1. Sigmoid Activation Function

Formula:
f(x) = 1/(1+e^(-x))

The output ranges between 0 and 1.
It converts input values into probabilities.
It is commonly used in the output layer of binary classification models.
It can suffer from the vanishing gradient problem.


2. ReLU Activation Function

Formula:
f(x) = max(0,z)

If the input is negative, the output is 0.
If the input is positive, the output is equal to the input.
It is computationally simple and efficient.
It is commonly used in hidden layers of neural networks.
It can suffer from the dying ReLU problem.


3. Tanh Activation Function

Formula:
f(x) = {e^x - e^{-x}} / {e^x + e^{-x}}

The output ranges between -1 and 1.
Negative inputs produce negative outputs.
A zero input produces zero output.
It is commonly used in hidden layers.
It can also suffer from the vanishing gradient problem.

"""