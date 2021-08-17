'''
Author: Mohammed Lajam
'''

# Imported Library:
import pandas as pd

# Load the data from CSV file
iris = pd.read_csv('/Users/mohammedlajam/Desktop/Machine Learning/Iris.csv')
iris_df = pd.DataFrame(iris)

# a. To get the number of observations, missing values, and nan (Not a Number) values.
print(iris_df.info)  # To display the dataset and general information
print(iris_df.count())  # To know the number of observation
print(iris_df.isnull())  # To know the missing Value in a boolean format (True, False)
print(iris_df.isnull().sum())  # To know the number of missing values per column
print(iris_df.isnull().sum().sum())  # To know the number of missing values in the entire dataset

# b. To view the following statistical details of the Iris data set:
columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
for column in columns:
    print(iris_df[column].describe())
    print(iris_df[column].median())

# c. Statistical details of each species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’
for column in columns:
    print(iris_df[[column, 'Species']].groupby('Species').describe())
    print(iris_df[[column, 'Species']].groupby('Species').median())