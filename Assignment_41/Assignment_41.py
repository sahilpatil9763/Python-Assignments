import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def knnClassifier(DataPath):
    border = "-" * 65

    print(border)
    print("Step 1 : Get Data")
    print(border)

    df = pd.read_csv(DataPath)

    print("Some entries from the dataset are : ")
    print(df.head())

    print(border)

    print(border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(border)

    df.dropna(inplace=True)                                     # Removes the rows which contains missing values

    print("Shape of Dataset : ",df.shape)
    print("Total Records : ",df.shape[0])
    print("Total columns : ",df.shape[1])

    print("\nCleaning of Data is done.")

    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print("\nData is prepared.")

    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42, stratify=Y)

    print("Details of Traing and Testing Data")

    print("Shape of X_train",X_train.shape)
    print("Shape of X_test",X_test.shape)

    print("Shape of Y_train",Y_train.shape)
    print("Shape of Y_test",Y_test.shape)

    print("\nData is Manipulated.")
    
    print(border)

    print(border)
    print("Step 3 : Train Data")
    print(border)

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature scaling is done")

    model = KNeighborsClassifier(n_neighbors=5)

    print("Model created.")

    model = model.fit(X_train_scaled, Y_test)

    print("Data is Trained")

    print(border)

    print(border)
    print("Step 4 : Test")
    print(border)

    Y_pred = model.predict(X_train_scaled)

    print("Data is Tested")
    
    print(border)

    print(border)
    print("Step 5 : Calculate Accuracy")
    print(border)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print(f"Model Accuracy is : {Accuracy * 100}%")

    print(border)
        

def main():
    knnClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()