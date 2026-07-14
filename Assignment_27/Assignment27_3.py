"""
Write a Python program to implement a class named Numbers with the following specifications:
• The class should contain one instance variable:
    • Value
• Define a constructor (__init__) that accepts a number from the user and initializes Value.
• Implement the following instance methods:
    • ChkPrime () - returns True if the number is prime, otherwise returns False
    • ChkPerfect () - returns True if the number is perfect, otherwise returns False
    • Factors () - displays all factors of the number
    • SumFactors () - returns the sum of all factors
• Create multiple objects and call all methods.
"""

class Numbers:
    def __init__(self, Value):
        self.Value = Value

    # Check whether the number is Prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    # Check whether the number is Perfect
    def ChkPerfect(self):
        sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i

        if sum == self.Value:
            return True
        else:
            return False

    # Display all factors
    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Return the sum of all factors
    def SumFactors(self):
        sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum = sum + i

        return sum


# Main
print("Enter number of objects:")
n = int(input())

obj = []

for i in range(n):
    print("\nEnter number:")
    no = int(input())
    obj.append(Numbers(no))

for i in obj:
    print("\n----------------------------")
    print("Number :", i.Value)

    if i.ChkPrime():
        print("Prime Number")
    else:
        print("Not a Prime Number")

    if i.ChkPerfect():
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

    i.Factors()
    print("Sum of Factors :", i.SumFactors())