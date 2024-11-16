import numpy as np

data = np.array([[[3, 10], [15, 20]], [[25, 30], [35, 40]], [[45, 50], [55, 60]]])

print(f"Original 3D Array:\n {data}")
# Using flatten function
flattened_data = data.flatten()

print(f"\nFlattened 1D Array: {flattened_data}")
