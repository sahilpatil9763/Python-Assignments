"""
Design a Python application that creates two threads. 
• Thread 1 should compute the sum of elements from a list. 
• Thread 2 should compute the product of elements from the same list. 
• Return the results to the main thread and display them.
"""

import threading

Sum = 0
Product = 1

def CalculateSum(No):
    global Sum

    for i in No:
        Sum = Sum + i

def CalculateProduct(No):
    global Product

    for i in No:
        Product = Product * i

def main():
    n = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(n):
        data.append(int(input()))

    t1 = threading.Thread(target=CalculateSum, args=(data,))
    t2 = threading.Thread(target=CalculateProduct, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum =", Sum)
    print("Product =", Product)

if __name__ == "__main__":
    main()