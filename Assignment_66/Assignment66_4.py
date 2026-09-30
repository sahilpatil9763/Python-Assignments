"""
4: Write a Python program to show how weights are updated in ANN.

Tasks:
1. Take input, weight, bias, target, output, and learning rate.
2. Calculate prediction.
3. Calculate error.
4. Update weight using gradient descent logic.
5. Display old weight and updated weight.
"""

# Function to update weight using gradient descent
def update_weight(x, weight, bias, target, learning_rate):

    # Calculate prediction
    output = (x * weight) + bias

    # Calculate error
    error = target - output

    # Calculate gradient
    gradient = -2 * x * error

    # Update weight using gradient descent
    new_weight = weight - (learning_rate * gradient)

    # Update bias
    new_bias = bias + (learning_rate * 2 * error)

    # Display results
    print("\nPrediction:", output)
    print("Error:", error)
    print("Old Weight:", weight)
    print("Updated Weight:", new_weight)
    print("Old Bias:", bias)
    print("Updated Bias:", new_bias)


# Take input from user
x = float(input("Enter input: "))
weight = float(input("Enter weight: "))
bias = float(input("Enter bias: "))
target = float(input("Enter target: "))
learning_rate = float(input("Enter learning rate: "))

# Call function
update_weight(x, weight, bias, target, learning_rate)