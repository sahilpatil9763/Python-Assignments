"""
consider the catacet helow
Study Hours     Marks
        1         50
        2         55
        3         60
        4         65
        7         70
Write a Python program to:
• Train a regression model using this dataset
• Print the coefficients for both features
• Print the intercept
"""

from sklearn.linear_model import LinearRegression
import numpy as np


def main():

    # Dataset
    X = np.array([
        [1, 7],
        [2, 6],
        [3, 7],
        [4, 6],
        [5, 8]
    ])

    Y = np.array([50, 55, 60, 65, 70])

    # Create model
    Model = LinearRegression()

    # Train model
    Model.fit(X, Y)

    # Print coefficients
    print("Coefficient for Study Hours :", Model.coef_[0])
    print("Coefficient for Sleep Hours :", Model.coef_[1])

    # Print intercept
    print("Intercept :", Model.intercept_)


if __name__ == "__main__":
    main()