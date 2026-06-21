# Write a program to display :

import sys

no = 11

# 1) Data Type
print("Data Type of no is: ", type(no))                 # Data Type of no is:  <class 'int'>

# 2) Memory Address
print("Memory Address of no is: ", id(no))              # Memory Address of no is:  140714449487288

# 3) Size in Bytes of a Variable enterd by User
print("Enter a Variable: ")
Var = input()                                           # By default input() function takes input as string
size = sys.getsizeof(Var)
print("Size of Variable is: ", size)                    # Size of Variable is:  50 