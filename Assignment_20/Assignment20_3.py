"""
Design a Python application that creates two threads named EvenList and OddList.
• Both threads should accept a list of integers as input.
• The EvenList thread should:
    • Extract all even elements from the list.
    • Calculate and display their sum.
• The OddList thread should:
    • Extract all odd elements from the list.
    • Calculate and display their sum.
Threads should run concurrently.
"""

import threading
import time

def EvenFactor(No):

    Even = []
    Sum = 0

    for i in No:
        if i % 2 == 0:
            Even.append(i)
            Sum = Sum + i

    print(f"Extracted Even elements are : {Even}")
    print("Sum of Even numbers : ",Sum)

def OddFactor(No):

    Odd = []
    Sum = 0
    for i in No:
        if i % 2 != 0:
            Odd.append(i)
            Sum = Sum + i

    print("Extracted Odd elements are : ",Odd)
    print("Sum of Odd Numbers : ",Sum)

def main():

    UserInput = input("Enter integer seperated by space : ")
    Data = list(map(int, UserInput.split()))

    start_time = time.perf_counter()

    t1 = threading.Thread(target=EvenFactor, args=(Data,))
    t2 = threading.Thread(target=OddFactor, args=(Data,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()