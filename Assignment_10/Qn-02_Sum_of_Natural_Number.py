# Accept a number ad print sum of first N natural numbers

import Functions as Func

def main():
    print("Enter a number: ")
    Value = int(input())
    Ret = Func.SumOfNaturalNumber(Value)
    print(Ret)
    
if __name__ == "__main__":
    main() 