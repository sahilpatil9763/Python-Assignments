"""
4. Write a Python program to calculate the Euclidean distance between
two feature scaling, and explain the difference in results.

[[25,20000],
 [30,40000],
 [35,80000]]
"""

from sklearn.preprocessing import StandardScaler


class EuclideanDistance:

    def __init__(self):

        self.Data = [
            [25, 20000],
            [30, 40000],
            [35, 80000]
        ]

    def CalculateDistance(self, Point1, Point2):

        Sum = 0

        for i in range(len(Point1)):
            Sum = Sum + ((Point1[i] - Point2[i]) ** 2)

        Distance = Sum ** 0.5

        return Distance

    def FeatureScaling(self):

        Scaler = StandardScaler()

        ScaledData = Scaler.fit_transform(self.Data)

        return ScaledData


def main():

    obj = EuclideanDistance()

    # Points before scaling
    Point1 = obj.Data[0]
    Point2 = obj.Data[1]

    Distance = obj.CalculateDistance(Point1, Point2)

    print("Distance before scaling : ", Distance)

    # Feature Scaling
    ScaledData = obj.FeatureScaling()

    print("\nData after feature scaling : ")
    print(ScaledData)

    # Points after scaling
    ScaledPoint1 = ScaledData[0]
    ScaledPoint2 = ScaledData[1]

    ScaledDistance = obj.CalculateDistance(
        ScaledPoint1,
        ScaledPoint2
    )

    print("\nDistance after scaling : ", ScaledDistance)


if __name__ == "__main__":
    main()