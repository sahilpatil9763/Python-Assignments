# Program which accept one numberand prints in reverse that many number starting from 1

def ReverseNumberSeries(no):
    for i in range(no, 0, -1):
        print(i, end=" ")

def main():
    Value = int(input("Enter a Number: "))
    
    ReverseNumberSeries(Value)
        
if __name__ == "__main__":
    main()