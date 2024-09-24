a = "hello abdullah"
b = "br22"
c = "3gh"
d = a + "  " + b + "  " + c + "  "  # concatenation

print(d)
print(d[:-3])
print(d[::-1])  # hg3  22rb  halludba olleh
print(d.upper())
print(d.lower())
print(d.title())
print(d.isdigit())  # False
print(d.find("39"))
print(d.find("a22"))
print(d.capitalize())  # the first letter of the string
print(d.isalnum())  # False
print(d.count("a"))
print(d.split(","))  # ['hello abdullah  br22  3gh  ']
print(d.replace("abdullah", "Python"))  # str.replace(old, new)
print(d.swapcase())  # HELLO ABDULLAH  BR22  3GH
print("a2" in d)  # False
print("\n")

# All Methods
txt = "HELLO WORLD"
print(txt.isupper())
print(txt.istitle())  # Abdulla Al hoile True
print(txt.casefold())  # Convert string to lowercase
txt = "Abdullah Al Afjal"
print(txt.rfind("Afjal"))
print(txt.center(30, "-"))
print(txt.encode())  # Encodes the string into bytes.
print(txt.endswith("Afjal"))  # Checks if the string ends with the specified suffix
print(txt.find("Afjal"))
print(txt.isalpha())  # Checks if all characters in the string are alphabetic
print(txt.islower())
print(txt.isnumeric())  # txt ="13234" output:true

text = "Hello, {}!"
print(text.format("Afjal"))
text = "   "
print(text.isspace())  # he string are whitespace.

txt = "           abdullah"
print(txt.lstrip())

txt = "apple,banana,orange"
print(txt.rsplit(","))  # ['apple', 'banana', 'orange']
