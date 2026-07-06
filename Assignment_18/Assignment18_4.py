"""
Accept N number from user and store it into List. Accept one another number from user and return frequency of that number from List.
Input: Number of elements: 11
Input Elements: 13 5 45 7 4 56 5 34 2 5 65
Elements to search: 5
Output: 3
"""

def ListFrequency(Data, Search):
    frequency = 0
    for num in Data:
        if num == Search:
            frequency += 1
    return frequency


def main():
    Size = int(input("Number of elements: "))

    Arr = []
    
    print("Input Elements: ", end="")
    numbers = input().split()

    for i in range(Size):
        num = int(numbers[i])
        Arr.append(num)

    Search = int(input("Elements to search: "))

    Ans = ListFrequency(Arr, Search)

    print("Output:", Ans)


if __name__ == "__main__":
    main()
        