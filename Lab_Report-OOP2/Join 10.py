import numpy as np

branch1 = np.array([5, 10, 15, 20])
branch2 = np.array([25, 30, 35, 40])

horizontal_join = np.column_stack((branch1, branch2))

vertical_join = np.vstack((branch1, branch2))

print(f"Horizontal Join Columns:\n {horizontal_join}")

print(f"\nVertical Join Rows:\n {vertical_join}")
