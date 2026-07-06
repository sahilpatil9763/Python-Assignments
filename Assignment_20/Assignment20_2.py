"""
Design a Python application that creates two threads named EvenFactor and OddFactor.
• Both threads should accept one integer number as a parameter.
• The EvenFactor thread should:
    • Identify all even factors of the given number.
    • Calculate and display the sum of even factors.
• The OddFactor thread should:
    • Identify all odd factors of the given number.
    • Calculate and display the sum of odd factors.
• After both threads complete execution, the main thread should display the message:
  "Exit from main"
"""

import threading
import time

def EvenFactor(No):

    Even = []
    Sum = 0

    for i in range(1, No + 1):
        if (No % i == 0 and No % 2 == 0):
            Even.append(i)
            Sum = Sum + i

    print(f"Even Factors are : {Even}")
    print("Sum of Even Factors : ",Sum)

def OddFactor(No):

    Odd = []
    Sum = 0
    for i in range(1, No + 1):
        if (No % i == 0 and No % 2 != 0):
            Odd.append(i)
            Sum = Sum + i

    print("Odd Factors are : ",Odd)
    print("Sum of Odd Factors : ",Sum)

def main():

    Value = int(input("\nEnter an integer number : "))

    start_time = time.perf_counter()
    
    print("\n-------- EvenFactor --------")

    t1 = threading.Thread(target=EvenFactor, args=(Value,))
    t1.start()
    t1.join()

    print("----------------------------\n")

    print("\n-------- OddFactor ---------")

    t2 = threading.Thread(target=OddFactor, args=(Value,))
    t2.start()
    t2.join()

    print("----------------------------\n")

    print("\n----------------------------")

    print("Exit from main")

    print("----------------------------\n")

    end_time = time.perf_counter()

    print(f"Time is {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()