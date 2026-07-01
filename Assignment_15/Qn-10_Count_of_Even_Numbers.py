"""
Write a lambda function using filter() which accepts a list of numbers and returns count of even numbers.
"""
    
Even = lambda No : (No % 2 == 0)

def main():
    
    Data = list(int(x) for x in input("Enter numbers separated by space: ").split())
    
    FData = list(filter(Even, Data))
    
    Length = len(FData)
    
    print("Count of even numbers is: ", Length)
    

if __name__ == "__main__":
    main()