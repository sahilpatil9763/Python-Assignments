"""
2. Using the same dataset from above question, calculate model performance.

Tasks
1. Predict all Y values using regression equation.
2. Calculate:
• Mean Squared Error (MSE)
• R^2 Score

Show all intermediate calculations.
"""

class LinearRegression:

    def __init__(self):
        self.X = [1,2,3,4,5]
        self.Y = [3,4,2,4,5]

    def CalculateXbar_Ybar(self):
        sum_x = 0
        sum_y = 0

        for i in range(len(self.X)):
            sum_x = sum_x + self.X[i]
            sum_y = sum_y + self.Y[i]

        mean_x = sum_x / len(self.X)
        mean_y = sum_y / len(self.Y)

        print("Mean_X is : ",mean_x)
        print("Mean_Y is : ",mean_y)

        return mean_x, mean_y

    def Slope(self, mean_x, mean_y):
        n = len(self.X)

        numerator = 0
        denominator = 0

        # m = (Sum(x - xbar) * (y - ybar)) /  Sum(x - xbar) ** 2
        # Calculate slope i.e. m

        for i in range(n):
            numerator = numerator + ((self.X[i] - mean_x) * (self.Y[i] - mean_y))
            denominator = denominator + ((self.X[i] - mean_x) ** 2)

        m = numerator / denominator

        print("\nSlope of line i.e. m : ",m)
        return m

    def Intercept(self, m, mean_y, mean_x):
        # Calculate y intercept i.e. c
        # y = mx + c
        # c = y - mx
        # c = ymean - m * xmean

        c = mean_y - (m * mean_x)

        print("\nY intercept i.e. c : ",c)
        return c

    def Predict(self, m, c):

        Predicted_Y = []

        print("\nPredicted Y values : ")

        for x in self.X:
            y = m * x + c
            Predicted_Y.append(y)
            print("X = ", x, "Predicted Y = ", y)

        return Predicted_Y

    def CalculateMSE(self, Predicted_Y):
        Sum_Error = 0

        print("\nMSE Intermediate Calculations : ")

        for i in range(len(self.Y)):
            Error = self.Y[i] - Predicted_Y[i]
            Squared_Error = Error ** 2
            Sum_Error = Sum_Error + Squared_Error

            print(
                "Actual =", self.Y[i],
                "Predicted =", Predicted_Y[i],
                "Error =", Error,
                "Squared Error =", Squared_Error
            )

        MSE = Sum_Error / len(self.Y)

        print("\nSum of Squared Errors =", Sum_Error)
        print("Mean Squared Error (MSE) =", MSE)

        return MSE

    def CalculateRScore(self, Predicted_Y, mean_y):

        Sum_Squared_Error = 0
        Total_Sum_Squares = 0

        for i in range(len(self.Y)):

            # Squared error
            Sum_Squared_Error = Sum_Squared_Error + (
                (self.Y[i] - Predicted_Y[i]) ** 2
            )

            # Total variation
            Total_Sum_Squares = Total_Sum_Squares + (
                (self.Y[i] - mean_y) ** 2
            )

        RScore = 1 - (
            Sum_Squared_Error / Total_Sum_Squares
        )

        print("\nR Score Intermediate Calculations:")
        print("Sum Squared Error =", Sum_Squared_Error)
        print("Total Sum of Squares =", Total_Sum_Squares)

        print("R Score =", RScore)

        return RScore

def main():
    obj = LinearRegression()

    # Calculate Mean
    mean_x, mean_y = obj.CalculateXbar_Ybar()

    # Calculate Slope
    m = obj.Slope(mean_x, mean_y)

    # Calculate Intercept
    c = obj.Intercept(mean_x, mean_y, m)

    print("\nRegression Equation:")
    print("Y =", m, "x +", c)

    # Predict all Y values
    Predicted_Y = obj.Predict(m, c)

    # Calculate MSE
    MSE = obj.CalculateMSE(Predicted_Y)

    # Calculate R Score
    RScore = obj.CalculateRScore(Predicted_Y, mean_y)

    print("\nFinal Results :")
    print("Mean Squared Error (MSE) =", MSE)
    print("R Score =", RScore)


if __name__ == "__main__":
    main()