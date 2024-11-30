a=[1,3,5,7,4]

# 1. Access a[-2], a[2], find length and type
print(a[-2])
print(a[2])
print("Length of a: ",len(a))
print("Type of a: ",type(a))

# 2. Change a[-3] = 50, a[2:4]
a[-3]=50
a[2:4]=[10,20]
print("Updated a after Changes: ",a)

# 3. Add 100 in last index and add 200 in index=2
a.append(100)
a.insert(2,200)
print("Updated a after adding: ",a)

# 4. Remove last element and remove element at index 1
a.pop()
a.pop(1)
print("Updated a after removing: ",a)

# 5. Join a new list [2, 4, 6] with a
new_list=[2,4,6]
a.extend(new_list)
print("Updated a after Joining : ",a)

# 6. Copy all values in a to a new list b
b=a.copy()
print("Copied lsit b: ",b)

# 7. Sort the elements of b
b.sort()
print("Sorted List B: ",b)

# 8. Print all elements using loop and break if get 5
for item in a:
    print(item)
    if item==5:
        break

# 9. Find the largest number in a
largest_num=max(a)
print("The largest number in A: ",largest_num)

    