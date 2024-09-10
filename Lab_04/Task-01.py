#List
a=[1,3,5,7,4]

len=len(a)
tp=type(a)
print(len)
print(tp)
print(a)

print(a[-2])
print(a[2])

#Task-2

a[-3]=50
print(a[-3])
print(a)

#Task-3

print(a[2:4])
print(a[:3])
print(a[-4:-1])

#Task-4

a.append(100)
print(a)
a.insert(2,200)
print(a)

#Task-5

a.pop()
a.pop(1)
print(a)

#Task-6

a2=[2,4,6]
a3=a+a2
print(a3)

#Task-7

b=a.copy()
b.sort(b)
print(b)

#Task-8

for i in a:
    if i==7:
        break
    print(i,end=" ")
a.clear()
print("After Clear:",a)
    