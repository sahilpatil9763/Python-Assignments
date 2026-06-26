# Accept one number and returns its cube

def Cube(No):
    return No * No * No

def main():
    print("Enter a number:")
    Value = int(input())
    
    Ret = Cube(Value)
    
    print(Ret)
    
if __name__ == "__main__":
    main()