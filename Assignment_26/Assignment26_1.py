"""
Write a Python program to implement a class named Demo with the following specifications:
• The class should contain two instance variables: no1 and no 2.
• The class should contain one class variable named Value.
• Define a constructor (__init_ that accepts two parameters and initializes the instance variables).
• Implement two instance methods:
    • Fun () - displays the values of instance variables no1 and no2.
    • Gun () - displays the values of instance variables no1 and no2.

Create two objects of the Demo class as follows:

Obj1 = Demo (11, 21)
Obj2 = Demo (51, 101)

Call the instance methods in the given sequence:

Obj1.Fun ()

Obj2.Fun ()
Obj1.Gun ()
Obj2.Gun ()
"""

class Demo:

    # Class Variable
    Value = 100

    # Constructor
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B

    # Instance Method
    def Fun(self):
        print("Inside instance method named as Fun()")
        print("No1 = ",self.No1)
        print("No2 = ",self.No2)

    def Gun(self):
        print("Inside instance method named as Gun()")
        print("No1 = ",self.No1)
        print("No2 = ",self.No2)

# Object creation of the class Demo
Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

# Calling the instance methods
Obj1.Fun ()
Obj2.Fun ()

Obj1.Gun ()
Obj2.Gun ()