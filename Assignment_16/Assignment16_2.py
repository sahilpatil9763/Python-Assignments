"""
Accept number from user and check whether it is even or odd.
"""

def ChkNum(No):
    if (No % 2 == 0):
        print("Even number")
    else:
        print("Odd number")

def main():
    Value = int(input("Enter a number: "))

    Ret = ChkNum(Value)
    
if __name__ == "__main__":
    main()