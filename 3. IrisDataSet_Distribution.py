'''
Author: Mohammed Lajam
'''

# Imported Libraries:
import matplotlib.pyplot as plt
from numpy import genfromtxt

# Loading csv file using NumPy
# Caution: change the file path with the one in your directory
file_path = '/Users/mohammedlajam/Desktop/Machine Learning/Iris.csv'
my_data = genfromtxt(file_path, delimiter=',', names=True)

# combining each column in one tuple of a list
iris_data = list(zip(*my_data))

# creating a list of lists for each feature of the iris data set
features = []
for column in range(1, 5):
    feature = iris_data[column]
    features.append(feature)

# creating variables for each feature
sepalLength, sepalWidth, petalLength, petalWidth = features[0: 4]

# Slicing each feature into 3 lists (50 elements each) for the 3 species
sepalLength_species = [sepalLength[0:50], sepalLength[50:100], sepalLength[100:150]]
sepalWidth_species = [sepalWidth[0:50], sepalWidth[50:100], sepalWidth[100:150]]
petalLength_species = [petalLength[0:50], petalLength[50:100], petalLength[100:150]]
petalWidth_species = [petalWidth[0:50], petalWidth[50:100], petalWidth[100:150]]

# creating colors and species variables, to be passed into the for loop for plotting
colors = ['red', 'orange', 'blue']
species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# plotting Sepal length's histogram per species in figure 1
for i in range(0, 3):
    plt.figure(1)
    plt.hist(sepalLength_species[i], bins=10, alpha=0.5, label=species[i], color=colors[i])

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Sepal Length - Histogram')
plt.legend(loc='upper right')
plt.grid(color='gray', lw=0.2)

# plotting Sepal width's histogram per species in figure 2
for i in range(0, 3):
    plt.figure(2)
    plt.hist(sepalWidth_species[i], bins=10, alpha=0.5, label=species[i], color=colors[i])

plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.title('Sepal Width - Histogram')
plt.legend(loc='upper right')
plt.grid(color='gray', lw=0.2)

# plotting Sepal width's histogram per species in figure 3
for i in range(0, 3):
    plt.figure(3)
    plt.hist(petalLength_species[i], bins=10, alpha=0.5, label=species[i], color=colors[i])

plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.title('Petal Length - Histogram')
plt.legend(loc='upper right')
plt.grid(color='gray', lw=0.2)

# plotting Sepal width's histogram per species in figure 4
for i in range(0, 3):
    plt.figure(4)
    plt.hist(petalWidth_species[i], bins=10, alpha=0.5, label=species[i], color=colors[i])

plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.title('Petal Width - Histogram')
plt.legend(loc='upper right')
plt.grid(color='gray', lw=0.2)

# plotting all figures
plt.show()