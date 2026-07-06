"""
Accept N number from user and store it into List. Return minimum element from that List.
Input: Number of elements: 4
Input Elements: 13 5 45 7
Output: 4
"""

def ListMinimum(Data):
    minimum = Data[0]
    for num in Data:
        if num < minimum:
            minimum = num
    return minimum


def main():
    Size = int(input("Number of elements: "))

    Arr = []
    
    print("Input Elements: ", end="")
    numbers = input().split()

    for i in range(Size):
        num = int(numbers[i])
        Arr.append(num)

    Ans = ListMinimum(Arr)

    print("Output:", Ans)


if __name__ == "__main__":
    main()