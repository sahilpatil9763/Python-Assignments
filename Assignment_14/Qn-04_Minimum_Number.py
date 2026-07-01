# Write a lambda function which accepts two numbers and returns the minimum of those numbers.

Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
        
    Ret = Minimum(Value1, Value2)
    print("Minimum of the two numbers is:", Ret)

if __name__ == "__main__":
    main()