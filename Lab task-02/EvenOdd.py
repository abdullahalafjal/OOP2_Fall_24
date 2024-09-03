
def check_even_or_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

num = int(input("Enter a number: "))
result = check_even_or_odd(num)
print(result)



    
