# Program which accept a number and checks it is perfect number or not

def PerfectNumOrNot(no):
    Sum = 0
    for i in range(1, no):
        if no % i == 0:
            Sum = Sum + i
    if Sum == no:
        return print("It is a Perfect number")
    else:
        print("It is a Not Perfect number") 

def main():
    Value = int(input("Enter a number: "))
    
    PerfectNumOrNot(Value)
    
if __name__ == "__main__":
    main()