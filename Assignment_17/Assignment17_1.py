"""
Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult) for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation.
Write on python program which call all thefunctions from Arithmetic module by accepting the parameters from user.
"""

from Arithmetic import *

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))

    print("------------------Arithmetic Operations-----------------")
    
    Ret1 = Addition(Value1, Value2)
    print("Addition is: ",Ret1)
    
    Ret2 = Subtraction(Value1, Value2)
    print("Subtraction is: ",Ret2)
    
    Ret3 = Multiplication(Value1, Value2)
    print("Multiplication is: ",Ret3)
    
    Ret4 = Division(Value1, Value2)
    print("Division is: ",Ret4)

    print("--------------------------------------------------------")
    
if __name__ == "__main__":
    main()