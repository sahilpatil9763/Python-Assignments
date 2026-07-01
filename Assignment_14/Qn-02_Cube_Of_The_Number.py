# Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda No : No ** 3

def main():
    Value = int(input("Enter a number: "))
    
    Ret = Cube(Value)
    print("Cube of the number is:", Ret)

if __name__ == "__main__":
    main()