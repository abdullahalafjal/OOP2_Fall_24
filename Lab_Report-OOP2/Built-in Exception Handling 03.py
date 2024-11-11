def divide_elements(values, divisor):

    try:

        if not isinstance(divisor, (int, float)):
            raise TypeError("The divisor must be a numeric value.")

        results = []
        for value in values:
            try:
                result = value / divisor
                results.append(result)
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
            except TypeError:
                print(f"Error: Value '{value}' is not numeric and cannot be divided.")

        return results

    except TypeError as a:
        print(f"Error: {a}")


values = [10, 20, 30, 0]
divisor = input("Enter the divisor: ")

try:

    divisor = float(divisor)
except ValueError:
    print("Invalid input. Please enter a numeric value for the divisor.")
else:
    results = divide_elements(values, divisor)
    print("Results : ", results)
