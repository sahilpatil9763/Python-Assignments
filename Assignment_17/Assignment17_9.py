"""
Accept a number from user and return number of digits in that number.
Input: 5187934
Output: 7
"""

def DigitCount(No):
    Count = 0
    while No != 0:
        Count += 1
        No = No // 10
    return Count

def main():
    Value = int(input("Enter a number: ")) 
    print(DigitCount(Value))

if __name__ == "__main__":
    main()