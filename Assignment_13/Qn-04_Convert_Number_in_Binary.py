# Program which accept a number and give its binary number

def BinaryNumber(no):
    if no == 0:
        print("Binary equivalent: 0")
    else:
        binary = ""

    while no > 0:
        remainder = no % 2
        binary = str(remainder) + binary
        no = no // 2
    return binary

def main():
    Value = int(input("Enter a number: "))
    
    Ret = BinaryNumber(Value)
    print("Binary equivalent is: ",Ret)  
        
if __name__ == "__main__":
    main()