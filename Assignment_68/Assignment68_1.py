# Program to manually perform convolution

# Input Image
image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# 3x3 Edge Detection Kernel
kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

# Get image and kernel dimensions
image_rows = len(image)
image_cols = len(image[0])

kernel_rows = len(kernel)
kernel_cols = len(kernel[0])

# Calculate feature map dimensions
output_rows = image_rows - kernel_rows + 1
output_cols = image_cols - kernel_cols + 1

# Initialize feature map
feature_map = []

# Move kernel over the image
for i in range(output_rows):
    row = []

    for j in range(output_cols):
        total = 0

        print("\nRegion:")
        
        # Perform multiplication and addition
        for x in range(kernel_rows):
            for y in range(kernel_cols):
                image_value = image[i + x][j + y]
                kernel_value = kernel[x][y]

                print(image_value, end=" ")

                total += image_value * kernel_value

            print()

        row.append(total)

        print("Output =", total)

    feature_map.append(row)

# Display the final feature map
print("\nFinal Feature Map:")

for row in feature_map:
    print(row)
