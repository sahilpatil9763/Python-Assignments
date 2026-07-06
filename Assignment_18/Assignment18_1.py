"""
Accept N number from user and store it into List. Return addition of digits of all elements from that List.
Input: Number of elements: 6
Input Elements: 13 5 45 7 4 56
Output: 130
"""

def ListSum(Data):
    total_sum = 0
    for num in Data:
        total_sum += num
    return total_sum


def main():
    Size = int(input("Number of elements: "))

    Arr = []
    
    print(f"Enter {Size} numbers:")
    for i in range(Size):
        num = int(input())
        Arr.append(num)

    Ans = ListSum(Arr)

    print("Output:", Ans)


if __name__ == "__main__":
    main()