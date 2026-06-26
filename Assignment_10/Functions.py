def MultiplicationTable(No):
    for i in range(1,11):
        Ans = No * i
        print(Ans, end=" ")
        
def SumOfNaturalNumber(No):
    Sum = 0
    for i in range(1, No + 1):
        Sum = Sum + i
    return Sum

def Factorial(No):
    Ans = 1
    for i in range(1, No + 1):
        Ans = Ans * i
    return Ans  

def Even(No):
    for i in range(1, No + 1):
        if i % 2 == 0:
            print(i, end=" ")
            
def Odd(No):
    for i in range(No):
        if i % 2 != 0:
            print(i, end=" ")