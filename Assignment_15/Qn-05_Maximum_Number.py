# Write a lambda function using reduce() which accepts a list of numbers and returns Maximum elements.

from functools import reduce

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    
    Data = list(int(x) for x in input("Enter numbers separated by space: ").split())
    
    RData = reduce(Maximum, Data)
    
    print("Maximum element is:", RData)
    

if __name__ == "__main__":
    main()