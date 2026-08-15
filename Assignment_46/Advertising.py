"""
Design machine learning application which follows below steps as

Step 1:
Get Data
Load data from MarvellousAdvertising.csv file into python application.

Step 2:
Clean, Prepare and Manipulate data
As we want to use the above data into machine learning application we have prepare
that in the format which is accepted by the algorithms.

Step 3:
Train Data
Now we want to train our data for that we have to select the Machine learning.
For that we select Linear Regression algorithm from sykit learn library.
For training purpose divide the dataset into half part.
Use train method to train our dataset
algorithm.

Step 4:
Test the data
Test data by passing the remaining half part of the data set.

Step 5:
Display predicted values of Linear regression algorithms as well as expected values
which are provided by the data set
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# ----------------------------------------------------------
# Function Name : ImportData
# Description   : Load data from CSV file
# ----------------------------------------------------------

def ImportData():
    Data = pd.read_csv("Advertising.csv")

    return Data


# ----------------------------------------------------------
# Function Name : PrepareData
# Description   : Prepare input and output data
# ----------------------------------------------------------

def PrepareData(Data):
    X = Data[["TV", "Radio", "Newspaper"]]
    Y = Data["Sales"]

    return X, Y


# ----------------------------------------------------------
# Function Name : TrainData
# Description   : Train Linear Regression model
# ----------------------------------------------------------

def TrainData(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    Model = LinearRegression()

    Model.fit(X_train, Y_train)

    return Model, X_test, Y_test


# ----------------------------------------------------------
# Function Name : main
# Description   : main function
# ----------------------------------------------------------

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def main():

    print("---------------------------------------------")
    print("----- Marvellous Advertising Prediction -----")
    print("---------------------------------------------")

    # Step 1 : Get Data
    Data = pd.read_csv("Advertising.csv")

    print("Dataset loaded successfully.")

    # Step 2 : Clean, Prepare and Manipulate Data
    X = Data[["TV", "radio", "newspaper"]]
    Y = Data["sales"]

    # Step 3 : Train Data
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    Model = LinearRegression()

    Model.fit(X_train, Y_train)

    print("Model trained successfully.")

    # Step 4 : Test Data
    Y_predicted = Model.predict(X_test)

    # Step 5 : Display Predicted and Expected Values
    Result = pd.DataFrame({
        "Predicted": Y_predicted,
        "Expected": Y_test.values
    })

    print("\n---------------------------------------------")
    print("Predicted Values and Expected Values")
    print("---------------------------------------------")

    print(Result)

if __name__ == "__main__":
    main()