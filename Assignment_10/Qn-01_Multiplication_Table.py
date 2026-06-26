# Accept one number and prints multiplication table of that number output should be horizontally and no none in the end

import Functions as Func

def main():
    print("Enter a number:")
    Value = int(input())
    
    Func.MultiplicationTable(Value)

if __name__ == "__main__":
    main()