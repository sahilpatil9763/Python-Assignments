# Accepts one number and prints the factorial of that number

import Functions as Func

def main():
    print("Enter a number: ")
    Value = int(input())
    
    Ret = Func.Factorial(Value)
    print(Ret)

if __name__ == "__main__":
    main()