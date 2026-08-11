"""
2. The value of K plays an important role in the KNN algorithm.
Write a Python program that demonstrates how prediction changes when K changes.

Dataset
Use the same dataset as Assignment 1.

Tasks
Predict the class of the same new point using:
• K = 1
• K = 3
• K = 5

Expected Output
Prediction Results
K = 1 → Red
K = 3 → Red
K = 5 → Blue

Explain why the prediction changes when K increases.
Ans : When K increases, more neighboring points participate in the voting. Therefore, farther points can influence the result, which can change the predicted class.
"""

import math
import csv
import pandas as pd


border = "-" * 60


# ----------------------------------------------------------
# Function Name : EuclideanDistance
# Description   : Calculate Euclidean distance
# ----------------------------------------------------------

def EuclidianDistance(P1, P2):

    Ans = math.sqrt(
        (P1['X'] - P2['X']) ** 2 +
        (P1['Y'] - P2['Y']) ** 2
    )

    return Ans


# ----------------------------------------------------------
# Function Name : PredictClass
# Description   : Predict class using K nearest neighbors
# ----------------------------------------------------------

def PredictClass(Data, k):

    nearest = Data[:k]

    votes = {}

    for neighbours in nearest:

        label = neighbours['Label']

        votes[label] = votes.get(label, 0) + 1

    iMax = 0

    Predicted_Class = ""

    for label in votes:

        if votes[label] > iMax:

            iMax = votes[label]

            Predicted_Class = label

    return Predicted_Class


# ----------------------------------------------------------
# Function Name : KNNClassifier
# Description   : Implement KNN algorithm
# ----------------------------------------------------------

def KNNClassifier(DataPath):

    Info = (
        {'Point': 'A', 'X': 1, 'Y': 2, 'Label': 'Red'},
        {'Point': 'B', 'X': 2, 'Y': 3, 'Label': 'Red'},
        {'Point': 'C', 'X': 3, 'Y': 1, 'Label': 'Blue'},
        {'Point': 'D', 'X': 6, 'Y': 5, 'Label': 'Blue'},
        {'Point': 'E', 'X': 4, 'Y': 3, 'Label': 'Blue'}
    )

    # Create CSV file

    headers = ['Point', 'X', 'Y', 'Label']

    with open(DataPath, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=headers
        )

        writer.writeheader()
        writer.writerows(Info)


    # Read CSV using Pandas

    df = pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset :")
    print(df.head())
    print(border)


    # Accept new point

    X_Value = float(input("Enter X coordinate : "))
    Y_Value = float(input("Enter Y coordinate : "))

    new_point = {
        'X': X_Value,
        'Y': Y_Value
    }


    # Convert DataFrame into list of dictionaries

    Data = df.to_dict('records')


    # Calculate distance

    for d in Data:

        d['distance'] = EuclidianDistance(
            d,
            new_point
        )


    # Sort according to distance

    sorted_data = sorted(
        Data,
        key=lambda item: item['distance']
    )


    # Different K values

    k_values = [1, 3, 5]

    print(border)
    print("Prediction Results : ")

    for k in k_values:

        Prediction = PredictClass(
            sorted_data,
            k
        )

        print("K =", k, "→", Prediction)

    print(border)


# ----------------------------------------------------------
# Main Function
# ----------------------------------------------------------

def main():

    KNNClassifier("class_prediction.csv")


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":

    main()