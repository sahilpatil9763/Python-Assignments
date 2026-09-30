"""
1: Write a Python program to simulate a single artificial neuron.

Input:
x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

Tasks:
1. Calculate weighted sum.
2. Apply sigmoid activation function.
3. Display final output.
4. Explain whether output is close to 0 or 1.
"""

import math

class ArtificialNeuron:

    def __init__(self, x1, x2, w1, w2, bias):
        self.x1 = x1
        self.x2 = x2
        self.w1 = w1
        self.w2 = w2
        self.bias = bias

    # Calculate weighted sum
    def CalculateWeightedSum(self):
        return (self.x1 * self.w1) + (self.x2 * self.w2) + self.bias

    # Apply sigmoid activation function
    def Sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    # Display final output
    def DisplayOutput(self):
        weighted_sum = self.CalculateWeightedSum()
        output = self.Sigmoid(weighted_sum)

        print("Weighted Sum:", weighted_sum)
        print("Sigmoid Output:", output)

        if output >= 0.5:
            print("Output is close to 1 (High Activation)")
        else:
            print("Output is close to 0 (Low Activation)")


# Create object
obj = ArtificialNeuron(2, 3, 0.4, 0.6, 0.5)

# Display result
obj.DisplayOutput()