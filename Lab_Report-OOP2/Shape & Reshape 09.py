import numpy as np


def reshape_sensor_data(data, num_rows):
    num_elements = data.size
    num_cols = num_elements // num_rows

    if num_elements % num_rows != 0:
        padded_size = num_rows * (num_cols + 1)
        padded_data = np.pad(
            data, (0, padded_size - num_elements), mode="constant", constant_values=0
        )
        print(f"Data padded with zeros to match size: {padded_data}")
        reshaped_data = padded_data.reshape(num_rows, -1)
    else:
        reshaped_data = data.reshape(num_rows, num_cols)

    return reshaped_data


sensor_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

reshaped = reshape_sensor_data(sensor_data, num_rows=3)
print("Reshaped Data:")
print(reshaped)
