"""
Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that numbers.

Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""

from functools import reduce

GreaterThanLessThan = lambda No : (No >= 70 and No <= 90)
IcreamnetByTen = lambda No : No + 10
Multiplication = lambda No1, No2 : No1 * No2

def main():

    Data = list(map(int, input(f"Input List : ").split(",")))

    FData = list(filter(GreaterThanLessThan, Data))
    print("List after filter :", FData)

    MData = list(map(IcreamnetByTen, FData))
    print("List after map :", MData)

    RData = reduce(Multiplication, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()