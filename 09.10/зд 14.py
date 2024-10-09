elist=[]
b=0
from random import randint
for i in range(10):
    elist.append(randint(1,10))
for i in range(1):
    print(elist)
for i in elist:
    if elist.count(i)>1:
        elist.remove(i)
print(len(elist))