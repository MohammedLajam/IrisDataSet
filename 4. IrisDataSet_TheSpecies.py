'''
Author: Mohammed Lajam
'''

# To make it easier and faster, the user will enter only petal length and width
PetalLength = float(input("Enter the Petal Length in Cm: "))
PetalWidth = float(input("Enter the Petal Width in Cm: "))

# From statistic: we use the max and min values
if 1.9 >= PetalLength >= 1 and 0.6 >= PetalWidth >= 0.1:
    print("The species is Setosa")
elif (4.4 >= PetalLength >= 3 and 1.3 >= PetalWidth >= 1)\
        or (4.5 > PetalLength >= 3 and 1.8 >= PetalWidth >= 1)\
        or (5.1 > PetalLength > 3 and 1.4 > PetalWidth >= 1):
    print("The species is Versicolor")
elif (6.9 >= PetalLength >= 5.2 and 2.5 >= PetalWidth >= 1.9)\
        or (6.5 >= PetalLength > 5.1 and 2.5 >= PetalWidth > 1.4)\
        or (6.5 >= PetalLength > 4.5 and 2.5 >= PetalWidth > 1.8):
    print("The species is Virginica")

# Now, the rang of petal length (4.5-5.1) and petal width (1.4-1.8)
# is a common area between Versicolor and Virginica
# Therefore we need more info from the user
# The user will enter the values of Sepal length and width

else:
    SepalWidth = float(input("Enter the Sepal Width in Cm: "))
    # From statistic: we use the max and min values
    if 2.2 > SepalWidth >= 2:
        print("The species is Versicolor")
    elif 3.8 >= SepalWidth > 3.4:
        print("The species is Virginica")
    elif 3.4 >= SepalWidth >= 2.2:
        SepalLength = float(input("Enter the Sepal Length in Cm: "))
        if 7.9 >= SepalLength > 7:
            print("The species is Virginica")
        else:
            print("The species could be Versicolor or Virginica")
    else:
        print("Undefined Species")