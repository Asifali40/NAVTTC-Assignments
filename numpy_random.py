import numpy as np

arr = np.random.randint(500, size=(100))
print(arr)

# delete duplication
x = np.unique(arr)
print(x)

# sort the array
y = np.sort(x)
print(y)
