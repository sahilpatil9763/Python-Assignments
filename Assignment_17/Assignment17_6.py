"""
Accept a number from user and pritnt that number of "*" on screen.
Output:
* * * * *
* * * *
* * *
* *
*
"""

def DisplayPattern(No):
    for i in range(No, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    Value = int(input("Enter a number: "))

    DisplayPattern(Value)

if __name__ == "__main__":
    main()