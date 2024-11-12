import numpy as np

data = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

row_view = data[1, :]
print(f"Original array: {row_view}")

row_view[0] = 100
print(f"\nModified view of the second row: {row_view}")

print(f"\nOriginal array after modify: {data}")


column_copy = data[:, 2].copy()
print(f"\ncopy of the third column: {column_copy}")


column_copy[0] = 999
print(f"\nModified deep copy of the third column: {column_copy}")

print(f"\nOriginal array (after modifying deep copy): {data}")
