"""
Accept 2 number from user and return addition of that two numbers.
"""

def Add(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans


def main():
    Value1, Value2 = map(int, input("Enter two numbers separated by space: ").split())

    Ret = Add(Value1, Value2)

    print(f"Addition of {Value1} and {Value2} is {Ret}")

if __name__ == "__main__":
    main()