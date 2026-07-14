"""
Write a Python program to implement a class named BankAccount with the following requirements:
• The class should contain two instance variables:
    • Name (Account holder name)
    • Amount (Account balance)
• The class should contain one class variable:
    • ROI (Rate of Interest), initialized to 10.5
• Define a constructor (__init__) that accepts Name and initial Amount.
• Implement the following instance methods:
    • Display () - displays account holder name and current balance
    • Deposit () - accepts an amount from the user and adds it to balance
    • Withdraw() - accepts an amount from the user and subtracts it from balance 
      (Ensure withdrawal is allowed only if sufficient balance exists)
    • CalculateInterest () - calculates and returns interest using formula:
      Interest = (Amount * ROI) / 100
• Create multiple objects and demonstrate all methods.
"""

class BankAccount:

    # Class Variable
    ROI = 10.5

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Instance Method

    # Display Account Details
    def Display(self):
        print("\nAccount Holder Name : ",self.Name)
        print("Current Balance       : ",self.Amount)

    # Deposit money
    def Deposit(self):
        DepositAmount = float(input("Enter amount to deposit : "))
        self.Amount = self.Amount + DepositAmount
        print("Amount Deposited Successfully..")
    
    # Withdraw money
    def Withdraw(self):
        WithdrawAmount = float(input("Enter amount to withdraw : "))

        if WithdrawAmount <= self.Amount:
            self.Amount = self.Amount - WithdrawAmount
            print("Amount Withdrawn Successfully..")
        else:
            print("Insufficient balance!")

    # Calculate Interest
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

print("\nEnter Account Details : ")

Name = input("Enter Account Holder Name : ")
Amount = float(input("Enter Initial Balance : "))

# Object creation of the class Demo
Obj = BankAccount(Name, Amount)    

# Calling the instance methods
Obj.Display()

Obj.Deposit()
Obj.Display()

Obj.Withdraw()
Obj.Display()

print(f"Interest : {Obj.CalculateInterest()}\n")