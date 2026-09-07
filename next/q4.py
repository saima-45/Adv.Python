import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Complete array:")
print(arr)

print("50:", arr[1, 1])
print("10:", arr[0, 0])
print("90:", arr[2, 2])

print("First row:", arr[0])
print("Second row:", arr[1])
print("Third column:", arr[:, 2])