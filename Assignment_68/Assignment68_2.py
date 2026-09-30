# Program to demonstrate ReLU and Max Pooling

# Input Feature Map
feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

print("Original Feature Map:")
for row in feature_map:
    print(row)


# Step 1: Apply ReLU Activation Function
relu_output = []

for row in feature_map:
    new_row = []

    for value in row:
        if value < 0:
            new_row.append(0)
        else:
            new_row.append(value)

    relu_output.append(new_row)

print("\nReLU Output:")
for row in relu_output:
    print(row)


# Step 2: Apply 2x2 Max Pooling
pool_size = 2
stride = 2

rows = len(relu_output)
cols = len(relu_output[0])

pooled_rows = (rows - pool_size) // stride + 1
pooled_cols = (cols - pool_size) // stride + 1

max_pool_output = []

for i in range(0, rows - pool_size + 1, stride):
    row = []

    for j in range(0, cols - pool_size + 1, stride):
        region = []

        for x in range(pool_size):
            for y in range(pool_size):
                region.append(relu_output[i + x][j + y])

        maximum = max(region)
        row.append(maximum)

        print("\nPooling Region:", region)
        print("Maximum Value:", maximum)

    max_pool_output.append(row)

# Step 3: Display Max Pooling Output
print("\nMax Pooling Output:")
for row in max_pool_output:
    print(row)

# Step 4: Display Feature Map Sizes
print("\nOriginal Feature Map Size:", rows, "x", cols)
print("Max Pooling Output Size:",
      pooled_rows, "x", pooled_cols)

print("\nPooling reduces the size of the feature map.")