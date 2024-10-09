elist=[]
from random import randint
for i in range (10):
    elist.append(randint(1,100))
print(elist)
elist.sort()
print(elist[0])