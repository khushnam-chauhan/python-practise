import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

sum_result = arr1 + arr2
dot_product = np.dot(arr1, arr2)
print(dot_product)
print(sum_result)

# creating arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(matrix)


#mean of numbers
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(numbers)
std_deviation = np.std(numbers)
print(mean_value)
print(std_deviation)
#pandas dataframe
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)
print(df)