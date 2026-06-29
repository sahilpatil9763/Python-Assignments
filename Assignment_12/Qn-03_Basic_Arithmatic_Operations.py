# Program to accept two numbers and print Addition, Subtraction, Multiplication and Division

Addition = lambda a, b : a + b
SUbtraction = lambda a, b : a - b
Multiplication = lambda a, b : a * b
Division = lambda a, b: a / b

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    
    Ret1 = Addition(Value1, Value2)
    print("Addition is: ",Ret1)
    
    Ret2 = SUbtraction(Value1, Value2)
    print("Subtarction is: ",Ret2)
    
    Ret3 = Multiplication(Value1, Value2)
    print("Multiplication is: ",Ret3)
    
    Ret4 = Division(Value1, Value2)
    print("Division is: ",Ret4)
    
    
    
if __name__ == "__main__":
    main()