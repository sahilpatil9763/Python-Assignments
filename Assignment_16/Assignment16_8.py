"""
Accept a number from user and pritnt that number of "*" on screen.
"""

def PrintStar(No):
    for i in range(No):
        print("*", end=" ")

def main():
    Value = int(input("Enter a number: "))

    PrintStar(Value)

if __name__ == "__main__":
    main()