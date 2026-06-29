# Program which accept two numbers and print area of rectangle

AreaOfCircle = lambda PI, r : PI * r * r

def main():
    Value = int(input("Enter Radius of the Circle: "))
    
    PI = 3.14
    
    Ret = AreaOfCircle(PI, Value)
    print(f"Area of Circle is: {Ret} sq units")
        
if __name__ == "__main__":
    main()