# Write a function which accepts two numbers from user and return their multiplication

def Multiplication(a, b):
    Ans = a * b
    return Ans

def main():
    print("Enter First Number: ")
    No1 = int(input())
    
    print("Enter Second Number: ")
    No2 = int(input())
    
    Ret = Multiplication(No1, No2)
    print("Multiplication is: ", Ret)

if __name__ == "__main__":
    main()