# Program to accept one number and check whether that number is palindrome or not

def Pallindrome(no):
    if str(no) == str(no)[::-1]:
        return True
    else:
        return False

def main():
    Value = int(input("Enter a Number: "))
    
    Ret = Pallindrome(Value)
    
    if (Ret == True):
        print("It is a Pallindrome Number")
    else:
        print("It is not a Pallindrome Number")
    

if __name__ == "__main__":
    main()