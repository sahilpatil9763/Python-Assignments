"""
3. Use KNN to predict whether a student passes or fails based on study hours and attendance.

Dataset:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
| Study Hours | Attendance | Result |
- - - - - - - - - - - - - - - - - - -
|           2 |         60 |   Fail |
|           5 |         80 |   Pass |
|           6 |         85 |   Pass |
|           1 |         50 |   Fail |
- - - - - - - - - - - - - - - - - - -

Tasks
1. Accept input from user:
    • Study hours
    • Attendance percentage
2. Apply KNN algorithm
3. Predict whether the student Passes or Fails

Input Example : 
Enter Study Hours: 4
Enter Attendance: 70

Expected Output :
Predicted Result: Pass
"""

from sklearn.neighbors import KNeighborsClassifier

def Main():

    # Training Dataset
    
    StudyHours = [[2], [5], [6], [1]]
    Attendance = [60, 80, 85, 50]
    Result = ["Fail", "Pass", "Pass", "Fail"]

    # Combine Study Hours and Attendance
    X = [
        [2, 60],
        [5, 80],
        [6, 85],
        [1, 50]
    ]

    Y = Result

    # Create KNN model
    Model = KNeighborsClassifier(n_neighbors=3)

    # Train the model
    Model.fit(X, Y)

    # Accept input from user
    Study = int(input("Enter Study Hours: "))
    Attend = int(input("Enter Attendance: "))

    # Predict result
    Prediction = Model.predict([[Study, Attend]])

    print("Predicted Result:", Prediction[0])


if __name__ == "__main__":
    Main()