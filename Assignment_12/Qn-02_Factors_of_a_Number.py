# Program to accept one nuber and prints its factors

def Factors(no):
    for i in range(1, no + 1):
        if no % i == 0:
            print(i, end = " ")

def main():
    Value = int(input("Enter a Number: "))
    
    Factors(Value)
    
if __name__ == "__main__":
    main()