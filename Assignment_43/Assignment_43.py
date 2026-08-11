"""
Design machine learning application which follows below steps as

Step 1:
Get Data
Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.

Step 2:
Clean, Prepare and Manipulate data
As we want to use the above data into machine learning application we have prepare
that in the format which is accepted by the algorithms.
As our dataset contains two features as Wether and Temperature. We have to replace each string field into numeric constants by using LabelEncoder from processing module of sklearn.

Step 3:
Train Data
Now we want to train our data for that we have to select the Machine learning algorithm.
For that we select K Nearest Neighbour algorithm.
use fit method for training purpose. For training use whole dataset.

Step 4:
Test Data
After successful training now we can test our trained data
by passing some value of
wether and temperature.
As we are using KNN algorithm use value of K as 3.
After providing the values check the result and display on screen.
Result may be Yes or No.

Step 5:
Calculate Accuracy
Write one function as CheckAccuracy() which calculate the accuracy of our algorithm.
For calculating the accuracy divide the dataset into two equal parts as Training data and
Testing data.
Calculate Accuracy by changing value of K.
"""


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# ----------------------------------------------------------
# Function Name : CheckAccuracy
# Description   : Calculate accuracy for different K values
# ----------------------------------------------------------

def CheckAccuracy(X, Y):

    # Divide dataset into two equal parts

    X_Train = X[:20]
    X_Test = X[20:]

    Y_Train = Y[:20]
    Y_Test = Y[20:]

    print("\nAccuracy Results")
    print("-" * 40)

    for K in [1, 3, 5, 7]:

        Model = KNeighborsClassifier(
            n_neighbors=K
        )

        # Train model

        Model.fit(X_Train, Y_Train)

        # Test model

        Y_Predicted = Model.predict(X_Test)

        # Calculate accuracy

        Accuracy = accuracy_score(
            Y_Test,
            Y_Predicted
        )

        print(
            "K =", K,
            "Accuracy =", Accuracy * 100, "%"
        )


# ----------------------------------------------------------
# Function Name : PlayPredictor
# Description   : Train and test KNN model
# ----------------------------------------------------------

def PlayPredictor(DataPath):

    # ------------------------------------------------------
    # Step 1 : Get Data
    # ------------------------------------------------------

    Data = pd.read_csv(DataPath)

    print("Dataset :")
    print(Data)

    print("-" * 60)

    # ------------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate Data
    # ------------------------------------------------------

    WetherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    Data['Wether'] = WetherEncoder.fit_transform(
        Data['Wether']
    )

    Data['Temperature'] = TemperatureEncoder.fit_transform(
        Data['Temperature']
    )

    Data['Play'] = PlayEncoder.fit_transform(
        Data['Play']
    )

    print("Encoded Dataset :")
    print(Data)

    print("-" * 60)

    # Features

    X = Data[
        ['Wether', 'Temperature']
    ]

    # Target

    Y = Data['Play']

    # ------------------------------------------------------
    # Step 3 : Train Data
    # ------------------------------------------------------

    Model = KNeighborsClassifier(
        n_neighbors=3
    )

    # Train using whole dataset

    Model.fit(X, Y)

    print("Model trained successfully.")

    print("-" * 60)

    # ------------------------------------------------------
    # Step 4 : Test Data
    # ------------------------------------------------------

    print("Enter Weather and Temperature")

    Wether = input(
        "Enter Weather : "
    )

    Temperature = input(
        "Enter Temperature : "
    )

    # Encode user input

    Wether_Value = WetherEncoder.transform(
        [Wether]
    )[0]

    Temperature_Value = TemperatureEncoder.transform(
        [Temperature]
    )[0]

    New_Data = [[
        Wether_Value,
        Temperature_Value
    ]]

    # Predict result

    Result = Model.predict(New_Data)

    # Convert numeric result back to Yes / No

    Prediction = PlayEncoder.inverse_transform(
        Result
    )

    print("-" * 60)

    print("Predicted Result:", Prediction[0])

    print("-" * 60)

    # ------------------------------------------------------
    # Step 5 : Calculate Accuracy
    # ------------------------------------------------------

    CheckAccuracy(X, Y)


# ----------------------------------------------------------
# Main Function
# ----------------------------------------------------------

def main():

    PlayPredictor(
        "MarvellousInfosystems_PlayPredictor.csv"
    )


# ----------------------------------------------------------
# Starter
# ----------------------------------------------------------

if __name__ == "__main__":

    main()