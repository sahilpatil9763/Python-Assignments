# Program to accept one number and print reverse of that number

def Reverse(no):
    return str(no)[::-1]                    # This method is called slicing. It is used to reverse the string.

def main():
    Value = int(input("Enter a Number: "))
    
    Ret = int(Reverse(Value))
    print("Reverse of the number:", Ret)
    type_of_Ret = type(Ret)
    print("Type of the reversed number:", type_of_Ret)

if __name__ == "__main__":
    main()