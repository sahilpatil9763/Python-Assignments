"""
Design a Python application that creates two threads named Prime and NonPrime.
• Both threads should accept a list of integers.
• The Prime thread should display all prime numbers from the list.
• The NonPrime thread should display all non-prime numbers from the list.
"""

import threading

# Function to check whether a number is prime
def isPrime(no):
    if no <= 1:
        return False

    for i in range(2, int(no ** 0.5) + 1):
        if no % i == 0:
            return False

    return True


# Thread function to display prime numbers
def DisplayPrime(lst):
    print("Prime Numbers:")
    for num in lst:
        if isPrime(num):
            print(num, end=" ")
    print()


# Thread function to display non-prime numbers
def DisplayNonPrime(lst):
    print("Non-Prime Numbers:")
    for num in lst:
        if not isPrime(num):
            print(num, end=" ")
    print()


def main():
    n = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(n):
        data.append(int(input()))

    t1 = threading.Thread(target=DisplayPrime, args=(data,), name="Prime")
    t2 = threading.Thread(target=DisplayNonPrime, args=(data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()