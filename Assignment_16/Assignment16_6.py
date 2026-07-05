"""
Accept a number from user and check whether that number is positive, negative or zero.
"""

def CheckNumber(No):
    if (No > 0):
        print("Positive Number")
    elif (No < 0):
        print("Negative Number")
    else:
        print("Zero")

def main():
    Value = int(input("Enter a number: "))

    Ret = CheckNumber(Value)
    
if __name__ == "__main__":
    main()