# Write a lambda function which accepts one number and returns square of that number.

Square = lambda No : No ** 2

def main():
    Value = int(input("Enter a number: "))
    
    Ret = Square(Value)
    print("Square of the number is:", Ret)

if __name__ == "__main__":
    main()