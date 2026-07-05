""" 
Program to check whether a entered number is prime or not
"""

def PrimeOrNot(no):
    for i in range(2, no):
        if no % i == 0:
            return False
        else:
            return True

def main():
    Value = int(input("Enter a Number: "))
    
    Ret = PrimeOrNot(Value)
    
    if (Ret == True):
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

if __name__ == "__main__":
    main()