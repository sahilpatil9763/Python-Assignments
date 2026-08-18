"""
7. Write a Python program using LinearRegression to train a regression model using the dataset below.

Study Hours     Marks
        1         50
        2         55
        3         60
        4         65
        7         70

Your program should:
    • Train the regression model
    • Print the coefficient
    • Print the intercept
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

    # Print coefficient
    print("Coefficient :", Model.coef_[0])

    # Print intercept
    print("Intercept :", Model.intercept_)


if __name__ == "__main__":
    main()