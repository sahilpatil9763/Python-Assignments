"""
Program which accept one lambda function which accepts one parameter and returns power of two.
"""

Power = lambda No : No ** 2

def main():
    Value = int(input())
    RValue = Power(Value)

    print(RValue)

if __name__ == "__main__":
    main()