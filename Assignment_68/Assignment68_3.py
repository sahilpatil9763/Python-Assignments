# Program to demonstrate Flattening in CNN

# Step 1: Input Matrix
matrix = [
    [6, 4],
    [8, 6]
]

print("Original Matrix:")
for row in matrix:
    print(row)


# Step 2: Flatten the 2D Matrix into 1D Vector
flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("\nFlatten Output:")
print(flatten_output)


# Step 3: Take Weights and Bias as Input
print("\nEnter weights for the Fully Connected Layer:")

weights = []

for i in range(len(flatten_output)):
    weight = float(input(f"Enter weight {i + 1}: "))
    weights.append(weight)

bias = float(input("Enter bias: "))


# Step 4: Calculate Fully Connected Layer Output
output = 0

for i in range(len(flatten_output)):
    output += flatten_output[i] * weights[i]

output += bias

# Step 5: Display Final Output
print("\nFully Connected Layer Calculation:")

for i in range(len(flatten_output)):
    print(f"{flatten_output[i]} * {weights[i]}")

print("Bias =", bias)
print("Final Output =", output)

"""
Why is the Flatten Layer Required in CNN?

• Convolutional and pooling layers produce multidimensional feature maps.
• Flattening converts these feature maps into a one-dimensional vector.
• The vector can then be passed to a fully connected layer.
• The fully connected layer uses the extracted features to calculate the final prediction.
"""