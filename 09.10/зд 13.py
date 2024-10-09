elist=[]
from random import randint
for i in range(20):
    elist.append(randint(1,200))
elist.sort()
elist.reverse()
print(elist)
print(elist[1])