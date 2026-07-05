"""
Program which accept one number and return its factorial.
"""

def Factorial(No):
    Ans  = 1
    for i in range(1, No + 1):
        Ans = Ans * i
    return Ans

def main():
    Value = int(input("Enter a number: "))
    print(Factorial(Value))

if __name__ == "__main__":
    main()
