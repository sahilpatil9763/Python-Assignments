"""
Write a Python program to implement a class named Circle with the following requirements:
• The class should contain three instance variables: Radius, Area, and Circumference.
• The class should contain one class variable named PI, initialized to 3.14.
• Define a constructor (init_ that initializes all instance variables to O. O.
• Implement the following instance methods:
    • Accept () - accepts the radius of the circle from the user.
    • CalculateArea () - calculates the area of the circle and stores it in the Area variable.
    • CalculateCircumference () - calculates the circumference of the circle and stores it in the Circumference variable.
    • Display () - displays the values of Radius, Area, and Circumference.
• Create multiple objects of the Circle class and invoke all the instance methods for each object.
"""

class Circle:

    # Class Variable
    PI = 3.14

    # Constructor
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # Instance Method
    def Accept(self):
        self.Radius = float(input("Enter Radius : "))
        
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
    
    def Display(self):
        print("\nAll the values are : ")
        print("Radius         : ",self.Radius)
        print("Area           : ",self.Area)
        print("Circumference  : ",self.Circumference)

No = int(input("Enter the number of circles : "))

for i in range(No):
    print(f"\nEnter details for Circle {i + 1}")

    # Object creation of the class Demo
    Obj = Circle()

    # Calling the instance methods
    Obj.Accept()
    Obj.CalculateArea()
    Obj.CalculateCircumference()
    Obj.Display()