a = "hello"
b = "b2b2b2"
c = "3g3g."

d = a + b + c
print("Concatenated string: ", d)

print("Length: ", len(d))
print(d[:-1])

if "a2" in d:
    print('"a2" is present in d.')
else:
    print('"a2" is not present in d.')

print("upper():", d.upper())
print("lower():", d.lower())
print("title():", d.title())
print("strip():", d.strip())
print("isdigit():", d.isdigit())
print('find("3g"):', d.find("3g"))
print("capitalize():", d.capitalize())
print("isalnum():", d.isalnum())
print('count("b2"):', d.count("b2"))
print("split():", d.split())
print("swapcase():", d.swapcase())
print("lstrip():", d.lstrip())
print('replace("hello", "python"):', d.replace("hello", "python"))
