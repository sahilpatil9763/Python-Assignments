"""
4. Use value_counts() to analyze the distribution of FinalResult.
Calculate the percentage of Pass and Fail students.
Is the dataset balanced? Justify your answer.
"""

import pandas as pd

def Import_csv():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    return df

def main():

    df = Import_csv()

    print("Distribution of FinalResult : ")
    print(df["FinalResult"].value_counts())

    # Calculate percentage
    ResultPercentage = df["FinalResult"].value_counts(normalize=True) * 100

    print("\nPercentage of Pass and Fail Students:")
    print(ResultPercentage)

if __name__ == "__main__":
    main()


"""
Is the dataset balanced? Justify your answer.
Ans : Yes, the dataset is considered reasonably balanced.

Justification:
While the classes are not in a perfect 50/50 split, a 60/40 ratio provides a solid representation of both outcomes. In machine learning, a dataset is typically only considered "imbalanced" when one class heavily outnumbers the other (for example, an 80/20 or 90/10 split). Because the minority class here (Fail) still makes up 40% of the data, predictive models will have sufficient examples to learn the underlying patterns for both passing and failing students without being severely biased toward the majority class.
"""