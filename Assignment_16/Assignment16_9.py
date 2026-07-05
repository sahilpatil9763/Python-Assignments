"""
Program to display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20
"""

def DisplayEvenNum(No):
    for i in range(1, No + 1):
        print(i * 2, end=" ")

def main():
    DisplayEvenNum(10)

if __name__ == "__main__":
    main()
