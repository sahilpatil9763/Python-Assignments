# Program which accept one numberand prints that many number starting from 1

def NumberSeries(no):
    for i in range(1, no + 1):
        print(i, end = " ")

def main():
    Value = int(input("Enter a Number: "))
    
    NumberSeries(Value)
    
if __name__ == "__main__":
    main()