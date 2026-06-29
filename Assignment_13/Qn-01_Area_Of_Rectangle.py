# Program which accept two numbers and print area of rectangle

AreaOfRectangle = lambda l, b : l *b

def main():
    Value1 = int(input("Enter Length of th Rectangle: "))
    Value2 = int(input("Enter Breadth of th Rectangle: "))
    
    Ret = AreaOfRectangle(Value1, Value1)
    print(f"Area of Rectangle is: {Ret} sq units")
        
if __name__ == "__main__":
    main()