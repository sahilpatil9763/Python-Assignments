# Employee Attrition Prediction System

## Overview

This project is a **Deep Learning-based Employee Attrition Prediction
System** developed in Python.

A software company is experiencing high employee turnover. The purpose
of this project is to build an intelligent system that can identify
employees who are likely to leave the company using historical employee
information.

The project uses the **MLPClassifier** to build and train a Multi-Layer
Perceptron neural network.

## Dataset

The program uses:

``` text
Employee_Attrition.csv
```

The CSV contains historical employee information used to train the
prediction model.

### Features

  Feature                   Description
  ------------------------- -------------------------------
  `Age`                     Employee age
  `MonthlyIncome`           Monthly salary
  `YearsAtCompany`          Experience in current company
  `TotalWorkingYears`       Total professional experience
  `DistanceFromHome`        Distance from home to office
  `JobSatisfaction`         Rating from 1--4
  `WorkLifeBalance`         Rating from 1--4
  `OverTime`                Yes/No
  `NumCompaniesWorked`      Previous companies
  `TrainingTimesLastYear`   Number of trainings
  `Attrition`               Yes/No --- target variable

## Prediction

The `Attrition` target is converted into:

``` text
0 → Employee is likely to stay
1 → Employee is likely to leave
```

The categorical `OverTime` feature is also converted into a numerical
representation before training.

## Project Workflow

The program performs the following tasks:

1.  Load the dataset using Pandas.
2.  Display the dataset shape, columns, and first five records.
3.  Check for missing values.
4.  Identify numerical and categorical features.
5.  Convert categorical features such as `OverTime` into numerical
    representation.
6.  Convert `Attrition` into `0` and `1`.
7.  Separate independent and dependent variables.
8.  Divide the dataset into training and testing data.
9.  Apply feature scaling.
10. Design an MLP with at least two hidden layers.
11. Train the neural network.
12. Display the number of training iterations.
13. Calculate training accuracy.
14. Calculate testing accuracy.
15. Generate a confusion matrix.
16. Plot the loss curve.
17. Create the `PredictAttrition(employee_data)` function.
18. Test the system using at least five new employee records.
19. Determine whether the model shows signs of overfitting or
    underfitting.

## Deep Learning Model

The project uses Scikit-learn's:

``` python
from sklearn.neural_network import MLPClassifier
```

The MLP contains at least two hidden layers as required by the
assignment.

## OOP Design

The Python program is implemented using **Object-Oriented Programming**.

The main class is:

``` text
EmployeeAttritionSystem
```

Important methods include:

``` text
LoadData()
CheckMissingValues()
IdentifyFeatures()
PreprocessData()
SplitFeaturesTarget()
SplitData()
ScaleData()
CreateModel()
TrainModel()
TrainingAccuracy()
TestingAccuracy()
ConfusionMatrix()
PlotLossCurve()
PredictAttrition()
```

This organization keeps data loading, preprocessing, model training,
evaluation, and prediction together in a reusable class.

## Model Evaluation

### Training Accuracy

Measures the model's prediction accuracy on the training data.

### Testing Accuracy

Measures the model's prediction accuracy on unseen testing data.

### Confusion Matrix

Displays classification results for employees predicted as likely to
**stay** or **leave**.

### Loss Curve

Shows how the training loss changes across the model's training
iterations.

## New Employee Prediction

The program provides:

``` python
PredictAttrition(employee_data)
```

This function accepts the details of a new employee and predicts:

``` text
Employee is likely to stay
```

or:

``` text
Employee is likely to leave
```

The assignment requires testing the system with at least five new
employee records.

## Requirements

Install the required libraries:

``` bash
pip install pandas scikit-learn matplotlib
```

## Project Structure

``` text
Employee-Attrition-Prediction/
│
├── Employee_Attrition.csv
├── Employee_Attrition_OOP.py
└── README.md
```

### Employee_Attrition.csv

Historical employee data used to train and test the model.

### Employee_Attrition_OOP.py

Python OOP implementation of the Employee Attrition Prediction System.

### README.md

Documentation explaining the dataset, purpose, workflow, model, and how
to run the program.

## How to Run

Keep `Employee_Attrition.csv` and `Employee_Attrition_OOP.py` in the
same directory.

Run:

``` bash
python3 Employee_Attrition_OOP.py
```

The program will load the data, preprocess it, train the MLP model,
calculate training and testing accuracy, generate a confusion matrix,
plot the loss curve, and test predictions on new employee records.

## Purpose

The purpose of this project is to demonstrate how **Deep Learning and
Python OOP** can be used to create an Employee Attrition Prediction
System.

The system learns from historical employee information and predicts
whether a new employee is likely to stay or leave.

> **Note:** This is an educational machine learning project. Predictions
> should not be treated as a definitive assessment of an individual
> employee.
