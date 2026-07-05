"""
Accept a number from user and return addition of digits in that number.
Input: 5187934
Output: 37
"""

def DigitSum(No):
    Sum = 0
    while No != 0:
        Sum += No % 10
        No = No // 10
    return Sum

def main():
    Value = int(input("Enter a number: "))
    print(DigitSum(Value))

    Sum = 0

if __name__ == "__main__":
    main()