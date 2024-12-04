a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}

# 1. Print a, b
print("Set a:", a)
print("Set b:", b)

# 2. Print the length and their type
print("Length of a:", len(a))
print("Length of b:", len(b))
print("Type of a:", type(a))
print("Type of b:", type(b))

# 3. Add a new element 10 in set a
a.add(10)
print("After adding 10: ", a)

# 4. Remove 8 from the set a
a.remove(8)
print("After removing 8: ", a)

# 5. Perform union, intersection, difference, symmetric difference, issubset operation on set a and set b
union_ab = a.union(b)
intersection_ab = a.intersection(b)
difference_ab = a.difference(b)
symmetric_difference_ab = a.symmetric_difference(b)
issubset_ab = a.issubset(b)

print("Union of a and b:", union_ab)
print("Intersection of a and b:", intersection_ab)
print("Difference of a and b:", difference_ab)
print("Symmetric difference of a and b:", symmetric_difference_ab)
print("Is a subset of b?", issubset_ab)

# 6. Join a new list [2, 3, 4] with set a
a.update([2, 3, 4])
print("After joining: ", a)
