a=[1,2,3,4,5,6,7,8,9,10]
b=[2,4,6,8,10]
for i in a:
    if i in b:
        (a.remove(i))
for j in range(1):
    print(a)