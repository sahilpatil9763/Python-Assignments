# Program which accept marks and displays grade
def Grades(no):
    if no >= 75:
        print("Distinction")
    elif no >= 60 and no < 75:
        print("First Class")
    elif no >= 50 and no < 60:
        print("Second Class")
    elif no < 50:
        print("Fail")

def main():
    Value = int(input("Enter marks: "))
    
    Grades(Value)
        
if __name__ == "__main__":
    main()