"""
8. Using the regression model created in the previous question, write a Python program to predict marks for 6
study hours and display the predicted value.
"""

from sklearn.linear_model import LinearRegression
import numpy as np


def main():

    # Dataset
    X = np.array([[1], [2], [3], [4], [5]])
    Y = np.array([50, 55, 60, 65, 70])

    # Create Linear Regression model
    Model = LinearRegression()

    # Train the model
    Model.fit(X, Y)

    # Predict marks for 6 study hours
    PredictedMarks = Model.predict([[6]])

    print("Predicted Marks for 6 Study Hours :",
          int(PredictedMarks[0]))


if __name__ == "__main__":
    main()