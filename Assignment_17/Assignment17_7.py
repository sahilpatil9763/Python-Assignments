"""
Accept a number from user and display below pattern.
Output:
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

def DisplayPattern(No):
    for i in range(No):
        for j in range(1, No + 1):
            print(j, end=" ")
        print()

def main():
    Value = int(input("Enter a number: "))

    DisplayPattern(Value)

if __name__ == "__main__":
    main()