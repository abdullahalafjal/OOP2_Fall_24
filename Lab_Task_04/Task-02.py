#Tupple 
a=(1,3,5,7,4)
b=(1,3,5,7,4)
len=len(b)
tp=type(b)
print(len)
print(tp)
print(b)
print(b[-2])
print(b[2])

#task-2

a=list(b)
a[-3]=50
print(a[-3])
print(a)

#task-3

print(a[2:4])
print(a[:3])
print(a[-4:-1])

#task-4

a.append(100)
print(a)
a.insert(2,200)
print(a)

#task-5

a.pop()
a.pop(1)
print(a)

#task-6

a.extend([2,4,6])
print(a)

#task-7

b=a.copy()
b.sort()
print(b)

#task-8

c=tuple(list (a))
for i in c:

    if i==7:
        break
    print(i,end=" ")
      
print("\n")
print(c)

