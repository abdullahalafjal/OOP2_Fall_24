import numpy as np

temp = np.array([15, 22, 18, 30, 12, 25, 28, 10, 33, 14])


threshold = 20

min_value = 20

exceed_indices = np.where(temp > threshold)
print("Indices where temperature exceeds the threshold of 20 degree C: ")
print(exceed_indices[0])

adjusted_temperatures = np.where(temp < threshold, min_value, temp)
print("\nTemperatures after replacing values below 20 degree C with 20°C: ")
print(adjusted_temperatures)
