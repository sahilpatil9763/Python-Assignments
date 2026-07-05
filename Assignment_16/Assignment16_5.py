"""
Program to display 10 to 1 on screen in reverse order.
"""

def DisplayReverse():
    for i in range(10, 0, -1):
        print(i, end=" ")

def main():
    DisplayReverse()
    
if __name__ == "__main__":
    main()