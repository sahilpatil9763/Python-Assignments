# Write a lambda function which accepts two numbers and returns the maximum of those numbers.

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
        
    Ret = Maximum(Value1, Value2)
    print("Maximum of the two numbers is:", Ret)

if __name__ == "__main__":
    main()