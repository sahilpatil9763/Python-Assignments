# Accept one number and returns its square

def Square(No):
    return No * No

def main():
    print("Enter a number:")
    Value = int(input())
    
    Ret = Square(Value)
    
    print(Ret)
    
if __name__ == "__main__":
    main()