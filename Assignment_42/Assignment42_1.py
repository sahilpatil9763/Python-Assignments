"""
1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
The algorithm should be implemented manually without using any machine learning library.

The program should:
• Calculate Euclidean distance
• Sort distances
• Select K nearest neighbors
• Predict the class based on majority voting

Dataset:
_ _ _ _ _ _ _ _ _ _ _ _ _ _
| Point |  X | Y  | Label |
- - - - - - - - - - - - - - 
|   A   | 1  | 2  |  Red  |
|   B   | 2  | 3  |  Red  |
|   C   | 3  | 1  |  Blue |  
|   D   | 6  | 5  |  Blue |
- - - - - - - - - - - - - -

Tasks:
1. Accept X and Y coordinates of a new point from the user.
2. Compute Euclidean distance from all dataset points.
3. Sort the distances.
4. Select K = 3 nearest neighbors.
5. Predict the class label.

Input Format:
Enter X coordinate: 2
Enter Y coordinate: 2

Expected Output:

Nearest Neignbors:
A - Distance: 1.0
B - Distance: 1.0
C - Distance: 1.41

Predicted Class. Red
"""

import math

def EuclidianDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def KNNClassifier():
    border = "-"*60

    Data = (
        {'Point':'A', 'X':1, 'Y':2, 'Label':'Red'},
        {'Point':'B', 'X':2, 'Y':3, 'Label':'Red'},
        {'Point':'C', 'X':3, 'Y':1, 'Label':'Blue'},
        {'Point':'D', 'X':6, 'Y':5, 'Label':'Blue'},
    )

    print(border)

    print("Dataset is : ")

    for i in Data:
        print(i)

    print(border)
    print(border)

    X_Value = float(input("Enter X coordinate : "))
    Y_Value = float(input("Enter Y coordinate : "))

    print(border)
    print(border)

    new_point = {'X':X_Value, 'Y':Y_Value}

    print("Distances of all points : ")

    for d in Data:
        d['distance'] = EuclidianDistance(d, new_point)

    for d in Data:
        print(d)

    print(border)
    print(border)

    sorted_data = sorted(Data, key = lambda item : item['distance'])

    print("Sorted Data is : ")

    for d in sorted_data:
        print(d)

    print(border)
    print(border)

    k = 3

    nearest = sorted_data[:k]               # First Three

    print("Nearest 3 Members are : ")

    for d in nearest:
        print(d)

    print(border)
    print(border)

    votes = {}

    for neighbours in nearest:
        label = neighbours['Label']
        votes[label] = votes.get(label,0)+1

    print("Majority Voting is : ")

    for d in votes:
        print("Names : ",d,"Number of votes : ",votes[d])

    print(border)
    print(border)

    iMax = 0

    Name = ""

    for d in votes:
        if votes[d] > iMax:
            iMax = votes[d]
            Name = d

    print("Nearest Neignbors:")

    for d in nearest:
        print(d['Point'], "- Distance:", round(d['distance'], 2))

    print("\nPredicted Class is : ",Name)

    print(border)
    print(border)


def main():
    KNNClassifier()

if __name__ == "__main__":
    main()