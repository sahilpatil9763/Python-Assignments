"""
3. Consider below task
    1. Train linear regression model.
    2. Predict salary for 6 years of experience.
    3. Plot regression line using matplotlib.

Dataset :

Experience      Salary
    1           20000
    2           25000
    3           30000
    4           35000
    5           40000

Expected Output:

Predicted Salary for 6 Years Experience: ₹45000
Graph should display:
• Data points
• Regression line
"""

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Dataset
    X = np.array([[1],[2],[3],[4],[5]])
    Y = np.array([20000,25000,30000,35000,40000])

    # Create the model
    model = LinearRegression()

    # Train the model
    model = model.fit(X,Y)

    # Predict the model
    Salary = int(model.predict([[6]])[0])
    print(f"Predicted salary for 6 years for experience is : ₹ {Salary}.")

    # Visualizaton

    # Predict values for regression line
    Y_Predicted = model.predict(X)

    # Display data points
    plt.scatter(X, Y, label="Data Points")

    # Display regression line
    plt.plot(X, Y_Predicted, label="Regression Line")

    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()