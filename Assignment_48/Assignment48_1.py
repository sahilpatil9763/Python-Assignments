"""
1. Implement Simple Linear Regression manually without using any ML library.

Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

Tasks

Calculate
    1. Mean of X (X)
    2. Mean of Y (Y)
    3. Slope (m)
    4. Intercept (c)

Expected Output Example

Mean of X = 3
Mean of Y = 3.6

Slope (m) = 0.4
Intercept (c) = 2.4

Regression Equation:
Y = 0.4x + 2.4

Predicted Y for X = 6 : 4.8
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

    def Slop(self, mean_x, mean_y):
        n = len(self.X)                         # 5

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

    def Yintercept(self, m, mean_y, mean_x):
        # Calculate y intercept i.e. c
        # y = mx + c
        # c = y - mx
        # c = ymean - m * xmean

        c = mean_y - (m * mean_x)

        print("\nY intercept i.e. c : ",c)
        return c

    def Predict(self, m, x, c):
        # y = mx + c
        
        y = m * x + c

        return y


def main():
    obj = LinearRegression()

    mean_x, mean_y =  obj.CalculateXbar_Ybar()

    m = obj.Slop(mean_x, mean_y)

    c = obj.Yintercept(m, mean_x, mean_y)

    print("\nRegression Equation:")
    print("Y = ", m, "x +", c)

    X = 6
    Y = obj.Predict(X , m, c)
    print("\nPredicted Y for X = 6 : ",Y)

if __name__ == "__main__":
    main()