# Write a progam to accept 2 numbers from the user and display their:

# Accepting 2 numbers from the user

x = int(input("Enter first number: "))                          # Enter first number: 5
y = int(input("Enter second number: "))                         # Enter second number: 2

print("\n -- Displaying the results -- \n")

# Addition
Addition = x + y
print(f"Addition is: {x} + {y} = {Addition}")                   # Addition is: 5 + 2 = 7

# Subtraction
Subtraction = x - y
print(f"Subtraction is: {x} - {y} = {Subtraction}")             # Subtraction is: 5 - 2 = 3

# Multiplication
Multiplication = x * y
print(f"Multiplication is: {x} * {y} = {Multiplication}")       # Multiplication is: 5 * 2 = 10

# Division
if y != 0:
    Division = x / y
    print(f"Division is: {x} / {y} = {Division}")                   # Division is: 5 / 2 = 2.5
else:
    print("Error: Division by zero is not allowed.")