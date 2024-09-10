employee={
    "name":"Abdullah Al Afjal",
    "age":23,
    "type":{
        "developer":["ios","android"]
    },

    "parmanent":True,
    "slary":300000,
    100:(1,2,3),
    4.5:{5,6,True,7,1}
}
ln=len(employee)
tp=type(employee)
print(ln)
print(tp)
print(employee["type"])
employee["parmanent"]=False
employee["gender"]="male"
employee.pop("age")
print(employee)
print(employee.keys())
print(employee.values())
print(employee.items())
for x in employee.keys():
    print(x)
for x in employee.values():
    print(x)  
for x, y in employee.items():
    print(x,y)