"""
Program which accept one number and return addition of its factors.
"""

def AddFactos(No):
    Ans  = 0
    for i in range(1, No):
        if No % i == 0:
            Ans = Ans + i
    return Ans

def main():
    Value = int(input("Enter a number: "))
    print(AddFactos(Value))

if __name__ == "__main__":
    main()
