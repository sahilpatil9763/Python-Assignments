# Write a lambda function which accepts one number and returns True if it is divisible by 5.

IsDivisibleBy5 = lambda No : True if No % 5 == 0 else False

def main():
    Value = int(input("Enter a number: "))
        
    Ret = IsDivisibleBy5(Value)
    print(Ret)

if __name__ == "__main__":
    main()