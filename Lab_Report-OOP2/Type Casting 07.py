import numpy as np

data = np.array(
    [
        ["Abdullah", "23", "75000.75"],
        ["Hira", "23", "70000.50"],
        ["jim", "24", "67000.10"],
    ]
)

ages = data[:, 1].astype(int)
print(f"Ages as integers: {ages}")


salaries = data[:, 2].astype(float)
print(f"\nSalaries as floats: {salaries}")


data[:, 1] = ages.astype(str)
data[:, 2] = salaries.astype(str)

print("\nUpdated Data: ")
print(data)
