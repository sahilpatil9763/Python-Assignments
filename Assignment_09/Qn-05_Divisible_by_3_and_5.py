# Accept one number and check whether it is divisible by 3 and 5

def ChkDivisible(No):
    if No % 3 == 0 and No % 5 == 0:
        return print("Divisible by 3 and 5")
    else:
        return print("Not Divisible by 3 and 5")

def main():
    print("Enter a number:")
    Value = int(input())
    
    ChkDivisible(Value)
    
if __name__ == "__main__":
    main()