b=0
elist=[]
from random import randint
for i in range(10):
    elist.append(randint(1,9))
for i in elist:
    b=elist.count(i)
for i in range(1):
    print(elist)
print(b)