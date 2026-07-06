"""
Program which accept one lambda function which accepts two parameters and returns power of its multiplication.
"""

Multiplication = lambda No1, No2 : No1 * No2

def main():
    #Value1 = int(input())
    #Value2 = int(input())

    Value1, Value2 = list(map(int, input("Input : ").split()))

    RValue = Multiplication(Value1, Value2)

    print("Output :",RValue)

if __name__ == "__main__":
    main()