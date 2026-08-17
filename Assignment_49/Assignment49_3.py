"""
3. Write a Python program using StandardScaler to perform feature scaling on the following dataset:
[[25,20000],
 [30,40000],
 [35,80000]]

Print the scaled dataset.
"""

from sklearn.preprocessing import StandardScaler

class Dataset:
    def __init__(self):
        self.Data = [
            [25,20000],
            [30,40000],
            [35,80000]
        ]

    def StandardScalar(self):
        scalar = StandardScaler()
        Scaled_Data = scalar.fit_transform(self.Data)

        print("Original Data:\n", self.Data)
        print("\nStandardized Data:\n", Scaled_Data)

def main():
    obj = Dataset()

    obj.StandardScalar()

if __name__ == "__main__":
    main()