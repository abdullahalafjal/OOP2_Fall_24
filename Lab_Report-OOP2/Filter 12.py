import numpy as np

prices = np.array([11,15, 30, 45, 10, 55, 66, 35, 70, 20, 50])

min_price = 20
max_price = 50

filtered_prices = prices[(prices >= min_price) & (prices <= max_price)]

print(f"Filtered prices (between $20 and $50): {filtered_prices}")

