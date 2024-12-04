employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["ios", "android"]},  
    "permanent": True,
    "salary": 30000,
    100: (1, 2, 3),  
    45: [5.6, True, 7, 1]  
}
print("Length: ", len(employee))
print("Type: ", type(employee))
print("Employee: ", employee)

developer = employee["type"]["developer"]
print("\nDeveloper types: ", developer)

employee["permanent"] = False
print("\nUpdated permanent: ", employee)

employee["gender"] = "male"
print("\nAfter adding 'gender': ", employee)


employee.pop("age", None)  
print("\nAfter removing 'age': ", employee)

print("\nKeys in the dictionary: ")
for key in employee.keys():
    print(key)

print("\nValues in the dictionary: ")
for value in employee.values():
    print(value)

print("\nItems in the dictionary (key-value pairs):")
for key, value in employee.items():
    print(key, ":", value)
