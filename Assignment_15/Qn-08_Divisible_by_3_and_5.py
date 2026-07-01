"""
Write a lambda function using filter() which accepts a list of numbers and returns numbers divisible by both 3 and 5.
"""
    
Divisible_By_3_and_5 = lambda No : (No % 3 == 0 and No % 5 == 0)

def main():
    
    Data = list(int(x) for x in input("Enter numbers separated by space: ").split())
    
    FData = list(filter(Divisible_By_3_and_5, Data))
    
    print("Numbers divisible by both 3 and 5 are: ", FData)
    

if __name__ == "__main__":
    main()