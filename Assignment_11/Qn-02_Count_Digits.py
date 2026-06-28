# Program to count digits in a number

def Count(no):
    return len(str(no))

def main():
    Value = int(input("Enter a Number: "))
    
    Ret = Count(Value)
    print("Number of digits:", Ret)

if __name__ == "__main__":
    main()