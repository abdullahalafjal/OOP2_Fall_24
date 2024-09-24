square = lambda x: x**2  # one argument
print(square(5))
add = lambda a, b: a + b  # Multiple arguments
print(add(7, 13))
# map() function to apply an operation to every element
num = [1, 2, 3, 4]
mapped = list(map(lambda x: x * 2, num))
print(mapped)

# filter() function to filter even num
num2 = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, num2))
print(even)

# List comprehension
x = [10, 3, 5, 6]
even_num = [num for num in x if num % 2 == 0]
print(even_num)

from functools import reduce

# Using reduce() to multiply
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Sorting list of tuples using a lambda
pairs = [(1, "one"), (2, "two"), (3, "three")]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

# if-else condition lambda
max_value = lambda a, b: a if a > b else b
print(max_value(10, 20))

# List comprehension with lambda
numbers = [1, 2, 3, 4, 5]
squared = [(lambda x: x**2)(x) for x in numbers]
print(squared)

# Using all() to check if all numbers are even
numbers = [1, 2, 3, 4, 5]
all_even = all(map(lambda x: x % 2 == 0, numbers))
print(all_even)

# Using lambda functions in dictionaries
actions = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else None,
}
print(actions["add"](5, 3))
print(actions["multiply"](5, 3))

# Sorting dictionary items by value using lambda
scores = {"Alice": 50, "Bob": 75, "Charlie": 60}
sorted_scores = sorted(scores.items(), key=lambda item: item[1])
print(sorted_scores)

# Function composition with lambda
f = lambda x: x * 2
g = lambda x: x + 3
h = lambda x: f(g(x))  # h(x) = f(g(x)) = (x + 3) * 2
print(h(4))


# Lambda inside a class
class Math:
    double = lambda self, x: x * 2
    triple = lambda self, x: x * 3


math = Math()
print(math.double(4))
print(math.triple(4))


# Using lambda as a callback function
def apply_operation(func, a, b):
    return func(a, b)


result = apply_operation(lambda x, y: x * y, 3, 4)
print(result)

# Variable capture with lambda
multiplier = 10
multiply = lambda x: x * multiplier
print(multiply(5))
