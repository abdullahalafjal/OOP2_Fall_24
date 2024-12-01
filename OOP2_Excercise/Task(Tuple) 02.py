a = (1, 3, 5, 6, 4)

# a. Find the sum of all odd numbers in a
sum_of_odds = sum(x for x in a if x % 2 != 0)
print("Sum of odd numbers in a:", sum_of_odds)

# b. Find the sum of all index elements in a
sum_of_all_elements = sum(a)
print("Sum of all elements in a:", sum_of_all_elements)

# c. Count the number of odd and even numbers separately
odd_count = sum(1 for x in a if x % 2 != 0)
even_count = sum(1 for x in a if x % 2 == 0)
print(f"Odd numbers count: {odd_count}")
print(f"Even numbers count: {even_count}")

# d. Extend the tuple with (2, 4, 6)
a = a + (2, 4, 6)
print("Tuple after extending:", a)

# e. Add a new item in index 2 (400)
a_list = list(a)
a_list.insert(2, 400)
a = tuple(a_list)
print("Tuple after inserting: ", a)

# f. Remove the last element
a_list = list(a)
a_list.pop()
a = tuple(a_list)
print("Tuple after removing the last element:", a)

# g. Perform slicing [-4:-1]
sliced_tuple = a[-4:-1]
print("Sliced tuple: ", sliced_tuple)

# h. Print the tuple using loop and use continue if get 5
print("Printing tuple with continue if 5:")
for item in a:
    if item == 5:
        continue
    print(item)
