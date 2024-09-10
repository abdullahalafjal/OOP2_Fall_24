#Set

a=(1,3,5,7,4)
b=(1,3,5,7,4)

a={1,3,5,8,3,7}
b={0,False,1,5}
print(a)
print(b)
len=len(a)
tp=type(a)
print(len)
print(tp)
a.add(10)
a.remove(8)
print(a)
c=a|b
print(c)
d=a&b
print(d)
e=a-b
print(e)
for i in a:

    if i==5:
        break
    print(i)
    
a.update([2,3,4])
print("After Join:",a)

