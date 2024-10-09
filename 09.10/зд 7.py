elist=[]
from random import randint
for i in range (10):
    elist.append(randint(1,100))
print(elist)
elist.sort()
elist.reverse()
print(elist[0])