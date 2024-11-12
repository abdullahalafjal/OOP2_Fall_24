import numpy as np

sales_data = np.array(
    [
        [10, 20, 30, 40, 50],
        [50, 50, 50, 10, 50],
        [20, 20, 20, 20, 20],
        [10, 20, 30, 70, 70],
        [90, 29, 90, 90, 59],
    ]
)

first_three_products = sales_data[:3, :]
print("Sales data for the first three products:")
print(first_three_products)

last_two_months = sales_data[:, -2:]
print("\nSales data for all products in the last two months:")
print(last_two_months)

specific_product_month = sales_data[1, 3]
print("\nSales data for the 2nd product in the 4th month:")
print(specific_product_month)
