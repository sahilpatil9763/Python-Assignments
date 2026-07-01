# Write a lambda function which accepts one number and returns True if it is even, otherwise False.

IsEven = lambda No : True if No % 2 == 0 else False

def main():
    Value = int(input("Enter a number: "))
        
    Ret = IsEven(Value)
    #print(Ret)

if __name__ == "__main__":
    main()