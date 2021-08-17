'''
Author: Mohammed Lajam
'''

# Imported Libraries:
import matplotlib.pyplot as plt
import pandas as pd

# Loading csv file and creating a dataframe
iris = pd.read_csv('/Users/mohammedlajam/Desktop/Machine Learning/Iris.csv')
iris_df = pd.DataFrame(iris)

# Creating variables for colors and species to be passed into a for loop
color = ['red', 'orange', 'blue']
species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Plotting the Sepal width and Sepal length for each species
for i in range(0, 3):
    species_df = iris_df[iris_df['Species'] == species[i]]  # specifying one type of the 3 species
    plt.figure(1)  # Saving the current plot in figure 1
    plt.scatter(species_df['SepalWidthCm'],
                species_df['SepalLengthCm'],
                color=color[i],
                alpha=0.5,
                label=species[i]
                )

plt.xlabel('sepal width (cm)')
plt.ylabel('sepal length (cm)')
plt.title('Iris dataset: Sepal width vs Sepal length')
plt.legend(loc='lower right')
plt.grid(color='gray', lw=0.2)

# Plotting the Petal width and Petal length for each species
for i in range(0, 3):
    species_df = iris_df[iris_df['Species'] == species[i]]  # specifying one type of the 3 species
    plt.figure(2)  # Saving the current plot in figure 2
    plt.scatter(species_df['PetalWidthCm'],
                species_df['PetalLengthCm'],
                color=color[i],
                alpha=0.5,
                label=species[i]
                )

plt.xlabel('Petal width (cm)')
plt.ylabel('Petal length (cm)')
plt.title('Iris dataset: Petal width vs Petal length')
plt.legend(loc='lower right')
plt.grid(color='gray', lw=0.2)

# plotting the figure 1 & 2
plt.show()