"""
Program which contains a function that accept a number from user and returns true if number is divisible by 5 otherwise false.
"""

def CheckNumber(No):
    if (No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter a number: "))

    Ret = CheckNumber(Value)
    print(Ret)

if __name__ == "__main__":
    main()