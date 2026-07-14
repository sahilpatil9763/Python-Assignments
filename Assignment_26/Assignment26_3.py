"""
Write a Python program to implement a class named Arithmetic with the following characteristics:
• The class should contain two instance variables: Valuel and Value2.
• Define a constructor (__init__ that initializes all instance variables to O)
• Implement the following instance methods:
    • Accept () - accepts values for Valuel and Value2 from the user.
    • Addition () - returns the addition of Valuel and Value2.
    • Subtraction () - returns the subtraction of Value1 and Value2.
    • Multiplication () - returns the multiplication of Valuel and Value2.
    • Division () - returns the division of Valuel and Value2 (handle division by zero properly).
• Create multiple objects of the Arithmetic class and invoke all the instance methods.
"""

class Arithmetic:

    # Constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # Instance Method
    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))
        
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not possible"
        else:
            return self.Value1 / self.Value2

No = int(input("Enter the number of objects : "))

for i in range(No):
    print(f"\nEnter values for Object {i + 1}")

    # Object creation of the class Demo
    Obj = Arithmetic()

    # Calling the instance methods
    Obj.Accept()
    
    print("Addtion is        : ",Obj.Addition())
    print("Subtraction is    : ",Obj.Subtraction())
    print("Multiplication is : ",Obj.Multiplication())
    print("Division is       : ",Obj.Division())