
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
sum_even = 0
sum_odd = 0
even_count = 0
odd_count = 0

for i in lst:
    if i % 2 == 0:
        sum_even += i
        even_count += 1
    else:
        sum_odd += i
        odd_count += 1

print(f"Sum of even numbers = {sum_even}")
print(f"Sum of odd numbers = {sum_odd}")
print(f"Number of even numbers = {even_count}")
print(f"Number of odd numbers = {odd_count}")
       