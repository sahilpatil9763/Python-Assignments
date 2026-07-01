# Write a lambda function using reduce() which accepts a list of numbers and returns Multiplication of all elements.

from functools import reduce

Product = lambda No1, No2 : No1 * No2

def main():
    
    Data = list(int(x) for x in input("Enter numbers separated by space: ").split())
    
    RData = reduce(Product, Data)
    
    print("Product of all elements is:", RData)
    

if __name__ == "__main__":
    main()