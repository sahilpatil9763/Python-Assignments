"""
Design a Python application that creates two threads.
• Thread 1 should calculate and display the maximum element from an list.
• Thread 2 should calculate and display the minimum element from the same list.
• The list should be accepted from the user.
"""

import threading


def Maximum(No):
    print("Maximum element is : ",max(No))

def Minimum(No):
    print("Minimum element is : ",min(No))

def main():
    n = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(n):
        data.append(int(input()))

    t1 = threading.Thread(target=Maximum, args=(data,), name="Thread1")
    t2 = threading.Thread(target=Minimum, args=(data,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()