n=5

for i in range(1,11):
    if i==6:
        continue
    if i>11:
        break
    multiplier = n*i
    print(multiplier,'x','=',n*i)