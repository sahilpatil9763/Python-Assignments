"""
Accept N number from user and store it into List. Return maximum element from that List.
Input: Number of elements: 6
Input Elements: 13 5 45 7 4 56
Output: 56
"""

def ListMaximum(Data):
    maximum = Data[0]
    for num in Data:
        if num > maximum:
            maximum = num
    return maximum


def main():
    Size = int(input("Number of elements: "))

    Arr = []
    
    print(f"Enter {Size} numbers in space-separated format: ", end="")
    numbers = input().split()

    for i in range(Size):
        num = int(numbers[i])
        Arr.append(num)

    Ans = ListMaximum(Arr)

    print("Output:", Ans)


if __name__ == "__main__":
    main()