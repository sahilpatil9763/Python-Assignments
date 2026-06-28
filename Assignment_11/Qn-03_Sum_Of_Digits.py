# Program to accept one number and print sum of digits of that number

def SumOfDigits(no):
    Sum = 0
    
    for i in str(no):
        Sum = Sum + int(i)
        
    return Sum    

def main():
    Value = int(input("Enter a Number: "))
    
    Ret = SumOfDigits(Value)
    print("Sum of digits:", Ret)

if __name__ == "__main__":
    main()